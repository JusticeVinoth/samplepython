class Sample:
    name: str
    id: str

    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id

    def get_details(name=None,id=None) -> 'Sample':
        return Sample(name,id)