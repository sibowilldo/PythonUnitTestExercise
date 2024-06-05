import unittest

from notes import Note


class TestNotes(unittest.TestCase):
    def setUp(self):
        self.notes = Note()

    def test_creates_a_note(self):
        _id = self.notes.size() + 1
        current_size = self.notes.size()
        self.notes.create_note('My note', 'Note Content')
        self.assertEqual(self.notes.size(), current_size + 1)  # add assertion here

    def test_can_view_notes(self):
        note = self.notes.create_note('My note', 'Note Content')
        self.assertDictEqual(self.notes.view_note(note["id"]), note)

    def test_can_list_all_notes(self):
        note1 = self.notes.create_note('My note 1', 'Note Content')
        note2 = self.notes.create_note('My note 2', 'Note Content')
        note3 = self.notes.create_note('My note 3', 'Note Content')

        self.assertEqual(self.notes.size(), 3)
        self.assertListEqual(self.notes.list_notes(), [note1, note2, note3])

    def test_can_edit_existing_note(self):
        note1 = self.notes.create_note('My note 1', 'Note Content')
        edited_note = self.notes.edit_note(note1["id"], "Edited Title", note1['content'])
        self.assertEqual(edited_note['id'], note1['id'])
        self.assertEqual("Edited Title", edited_note['title'])


if __name__ == '__main__':
    unittest.main()
