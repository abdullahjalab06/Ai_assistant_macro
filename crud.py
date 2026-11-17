from database import Companies
from database import Session
from sqlalchemy import update



def CompanyAdd():

    session = Session()

    name = input("Company Name: ")
    business_type = input("Business type: ")
    email = input("Company email: ")
    contactnumber = input("Contact Number: ")


    company = Companies(
        name=name,
        business_type=business_type,
        email=email,
        contactnumber=contactnumber
    )

    session.add(company)
    session.commit()
    session.close()

    print("Company added successfully.")

#CompanyAdd()


def delete_company_by_code(code):
    session = Session()
    company = session.query(Companies).filter(Companies.companycode == code).first()
    
    if company:
        session.delete(company)
        session.commit()
        print(f"تم حذف الشركة ذات الكود {code} بنجاح.")
        session.close()
        return True
    else:
        print("كود الشركة غير صحيح أو غير موجود!")
        session.close()
        return False
#delete_company_by_code("COMP-7C2BBD1E") # للتجريب لازم تدخل كود الشركة اللي بدك تحذفها

def get_company_by_code(company_code):

    session = Session()

    company = session.query(
        Companies
    ).filter(
        Companies.companycode == company_code
    ).first()

    session.close()

    return company
company = get_company_by_code("COMP-0158BB7F")

if company:
    print(f"ID: {company.id}")
    print(f"Name: {company.name}")
    print(f"Business Type: {company.business_type}")
    print(f"Email: {company.email}")
    print(f"Phone: {company.contactnumber}")

else:
    print("Company not found")


def update_company(company_id):
    session = Session()
    company = session.query(Companies).filter(Companies.id == company_id).first()

    if company:
        new_email = input("New Email: ")
        new_contact = input("New Contact: ")
        company.email = new_email
        company.contactnumber = new_contact
        session.commit()
        print("Company updated successfully.")
    else:
        print("Company not found.")

    session.close()
update_company(4)

