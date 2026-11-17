import os
from filereader import extract_text
from database import CompaniesData, Session


def upload_file(company_id, file_path):

    session = Session()

    text = extract_text(file_path)
    file_name = os.path.basename(file_path)
    file_type = os.path.splitext(file_path)[1]

    new_file = CompaniesData(
        company_id=company_id,
        file_name=file_name,
        file_type=file_type,
        file_path=file_path,
        content=text
    )

    session.add(new_file)
    session.commit()

    session.close()


#upload_file(4, r"c:\Users\ASUS\Desktop\about macro.docx")



def get_company_files(company_id):
    session = Session()

    files = session.query(CompaniesData).filter(CompaniesData.company_id==company_id).all()

    for file in files:
        print(file.file_name)
#get_company_files((4))


def get_company_content(company_id):
    session = Session()

    files = session.query(CompaniesData).filter(CompaniesData.company_id==company_id).all()

    content = ""

    for file in files:
        content += f"\n===== {file.file_name} =====\n"
        content += file.content
    session.close
    return content
    
#get_company_content(4)

def delete_company_files(company_id, file_name):
    session = Session()
    file = session.query(CompaniesData).filter(
        CompaniesData.company_id == company_id,
        CompaniesData.file_name == file_name,
    ).first()
    if file is None:
        session.close()
        return False

    session.delete(file)
    session.commit()
    session.close()
    return True
#delete_company_files(4, "about macro.docx")
    