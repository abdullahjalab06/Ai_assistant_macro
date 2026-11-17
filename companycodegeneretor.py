import uuid

def generate_company_code():
    return f"COMP-{str(uuid.uuid4())[:8].upper()}"

