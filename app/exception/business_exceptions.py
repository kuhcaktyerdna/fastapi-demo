class EntityNotFoundException(Exception):

    def __init__(self, entity_name: str | None = None, entity_id: int | None = None, message: str | None = None):
        if message is None:
            self.message = f'{entity_name} with id {entity_id} not found'
        else:
            self.message = message

        super().__init__(self.message)