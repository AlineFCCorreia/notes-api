from fastapi import APIRouter, HTTPException
from models import Note
from pydantic import BaseModel

router = APIRouter()

notes_db = []


@router.get("/notes")
def get_notes():
    return notes_db


@router.post("/add")
def create_note(note: Note):
    notes_db.append(note)
    return {"message": "Nota criada com sucesso!", "note": note}


@router.get("/notes/search/{note_id}")
def get_note(note_id: int):
    if note_id >= len(notes_db) or note_id < 0:
        raise HTTPException(status_code=404, detail="Note not found.")
    return notes_db[note_id]


@router.put("/notes/update/{note_id}")
def update_note(note_id: int, updated_note: Note):
    if note_id >= len(notes_db) or note_id < 0:
        raise HTTPException(status_code=404, detail="Note not found.")
    notes_db[note_id] = updated_note
    return {"message": "Nota atualizada!", "note": updated_note}


@router.delete("/notes/delete/{note_id}")
def delete_note(note_id: int):
    if note_id >= len(notes_db) or note_id < 0:
        raise HTTPException(status_code=404, detail="Note not found.")
    deleted_note = notes_db.pop(note_id)
    return {"message": "Nota deletada!", "note": deleted_note}
