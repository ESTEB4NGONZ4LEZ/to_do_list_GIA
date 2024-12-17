# app.py
import streamlit as st
import json
from sqlalchemy.orm import Session
from database import session, engine
from models import Tarea, base

container_listado = None

# Crear las tablas en la base de datos.
base.metadata.create_all(bind=engine)

def obtener_sesion():
    return session()

def agregar_tarea(titulo: str, descripcion: str):
    db: Session = obtener_sesion()
    nueva_tarea = Tarea(titulo = titulo, descripcion = descripcion)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    db.close()

def listar_tareas():
    db: Session = obtener_sesion()
    tareas = db.query(Tarea).all()
    db.close()
    return tareas

def marcar_tarea_completada(tarea_id: int):
    db: Session = obtener_sesion()
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        tarea.completada = True
        db.commit()
        st.rerun()
    else:
        st.error("Tarea no encontrada.")
    db.close()

def eliminar_tarea(tarea_id: int):
    db: Session = obtener_sesion()
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.completada == True).first()
    if tarea:
        db.delete(tarea)
        db.commit()
        st.rerun()
    else:
        st.error("Tarea no encontrada o no está completada.")
    db.close()

def exportar_tareas_json():
    tareas = listar_tareas()
    # Convertimos las tareas a un formato serializable.
    tareas_json = [
        {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "completada": tarea.completada,
        }
        for tarea in tareas
    ]
    # Convertimos la lista de tareas a JSON.
    return json.dumps(tareas_json, indent=4)

def crear_tabla_tareas():
    tareas = listar_tareas()
    if not tareas:
        container_listado.write("No se encontraron tareas.")
        return

    for tarea in tareas:
        estado = "Completada" if tarea.completada else "Pendiente"
        accion = "COMPLETADA" if not tarea.completada else "ELIMINAR"
        
        container_listado.write(f"{tarea.id}. {tarea.titulo}")
        container_listado.write(f"Estado: {estado}")
        container_listado.write(f"Descripción: {tarea.descripcion}")

        if container_listado.button(accion, key=f"{accion}_{tarea.id}"):
            (marcar_tarea_completada if not tarea.completada else eliminar_tarea)(tarea.id)

def main():
    # Titulo del aplicativo.
    title = '<h1 style="text-align: center;">GESTOR DE TAREAS</h1>'
    st.write(title, unsafe_allow_html = True)

    # Creacion de las columnas de la pagina. 
    col1, col2 = st.columns(2)
    global container_listado
    container_listado = col2

    # Titulo del formulario para crear tareas.
    subtitle1 = '<h4 style="text-align: center;">Agregar Tarea</h4>'
    col1.write(subtitle1, unsafe_allow_html = True)
    
    # Formulario para crear tareas.
    titulo = col1.text_input("Titulo")
    descripcion = col1.text_area("Descripcion")
    
    # Evento para agregar una tarea.
    if col1.button("AGREGAR"):
        if titulo and descripcion:
            agregar_tarea(titulo, descripcion)
        else:
            col1.error("Por favor, complete todos los campos.")

    # Titulo del listado de tareas.
    subtitle2 = '<h4 style="text-align: center;">Listar Tareas</h4>'
    col2.write(subtitle2, unsafe_allow_html = True)
    
    # Exportar tareas a JSON.
    tareas_json = exportar_tareas_json()
    col2.download_button(
        label="DESCARGAR",
        data=tareas_json,
        file_name="tareas.json",
        mime="application/json",
    )

    # Creamos el listado de tareas.
    crear_tabla_tareas()

if __name__ == "__main__":
    main()
