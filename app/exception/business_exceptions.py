class EntityNotFoundException(Exception):

    def __init__(self, entity_name: str, entity_id: int):
        self.message = f'Entity {entity_name} with id {entity_id} not found'
        super().__init__(self.message)