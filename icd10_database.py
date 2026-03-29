# ICD-10 Procedure Code Database

# This code contains a database of ICD-10 procedure codes and matching logic.

class ICD10Database:
    def __init__(self):
        self.codes = {
            '0CB00Z0': 'Surgical procedure to excise tissue',
            '0D000Z0': 'Open reduction of fracture',
            '0FB00Z0': 'Endoscopic examination',
            # Add more codes as needed
        }

    def get_description(self, code):
        return self.codes.get(code, 'Code not found')

    def add_code(self, code, description):
        self.codes[code] = description

    def remove_code(self, code):
        if code in self.codes:
            del self.codes[code]
        else:
            return 'Code not found'

# Example Usage:
if __name__ == '__main__':
    database = ICD10Database()
    print(database.get_description('0CB00Z0'))  # Outputs: Surgical procedure to excise tissue