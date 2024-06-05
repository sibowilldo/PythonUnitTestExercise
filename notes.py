from typing import List


class Note:
    def __init__(self):
        self.notes: List[dict] = []

    def create_note(self, title: str, content: str) -> dict:
        _id = self.size() + 1
        note = {"id": _id, "title": title, "content": content}
        self.notes.append(note)
        return note

    def view_note(self, _id: int) -> dict:
        for note in self.notes:
            if note["id"] == _id:
                return note

        raise ValueError("Note not found")

    def list_notes(self, ) -> List[dict]:
        return self.notes

    def edit_note(self, _id: int, title: str, content: str) -> dict:
        note = self.view_note(_id)
        note["title"] = title
        note["content"] = content
        return note

    def delete_note(self, _id: int) -> None:
        pass

    def size(self) -> int:
        return len(self.notes)
