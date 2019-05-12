class FileObj:
    def __init__(self):
        self.name
        self.fileID
        self.path
        self.server_modified
        self.shared_folder_id



class TreeStack:
    def __init__(self, dbx):
        self.dbx = dbx
        self.path = []

    def push(self, new_path):
        f = self.dbx.files_list_folder(path="/movies").entries
        
        from pprint import pprint
        pprint(f)

        self.path.append(new_path)
        return True

    def pop(self):
        self.path.pop(-1) if len(self.path) else None

    def current_path(self):
        return self.path[0]

    def print_path(self):
        return "/".join(self.path) if len(self.path) else '/'
