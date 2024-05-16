import streamlit as st
import mysql.connector
#Establish connection to mysql server
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital"
)
cursor=mydb.cursor()
#print("connection Established" )

#create streamlit app
def main():
   st.title("PATIENT RECORD MANAGEMENT")
   st.image(r"C:\Users\mpudi\Downloads\hos.jfif",width=900)
   #display options for crud operations
   menu = ["Create", "Read", "Update", "Delete","ReadAll","ShowTables"]
   choice = st.sidebar.selectbox("Menu", menu)


   if choice == "Create":
        st.subheader("Add New Patient")
        new_name = st.text_input('Name')
        new_age = st.number_input('Age', min_value=0, max_value=150)
        new_gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
        new_mobile = st.text_input('Mobile Number')
        if st.button('Add Patient'):
            add_patient(new_name, new_age, new_gender, new_mobile)
            st.success('Patient added successfully!')
     
   elif choice==  "Read":
       st.subheader("Show the patient record")
       patient_name = st.text_input('Enter Patient Name')
       if st.button('Display Patient'):
         display_patient_by_name(patient_name)
   

   elif choice== "Update":
       st.subheader("Update the patient record") 
       patient_id = st.number_input('Patient ID', min_value=1)
       updated_name = st.text_input('Name')
       updated_age = st.number_input('Age', min_value=0, max_value=150)
       updated_gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
       updated_mobile = st.text_input('Mobile Number')
       if st.button('Update Patient'):
         update_patient(patient_id, updated_name, updated_age, updated_gender, updated_mobile)
         st.success('Patient details updated successfully!')



   elif choice=="Delete":
       st.subheader("Delete the patient record")      
       patient_id = st.number_input('Patient ID', min_value=1)
       if st.button('Delete Patient'):
          delete_patient(patient_id)
          st.success('Patient deleted successfully!')
       else:
           st.success('Patient Details not in Record!')  

   elif choice=="ReadAll":
       st.subheader("Display ALL Patient Details")
       display_patients()  

   elif choice=="ShowTables":
       st.subheader("Displaying All Tables")  
       display_tables()    
#function to add patient details
def add_patient(name, age, gender, mobile):
    query = "INSERT INTO patient_db (name, age, gender, mobile) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, gender, mobile))
    mydb.commit()

#function to display particular patient details
def display_patient_by_name(name):
    query = "SELECT * FROM patient_db WHERE name = %s"
    cursor.execute(query, (name,))
    patient = cursor.fetchone()
    if patient:
        st.write(f"Id: {patient[0]}")
        st.write(f"Name: {patient[1]}")
        st.write(f"Age: {patient[2]}")
        st.write(f"Gender: {patient[3]}")
        st.write(f"Mobile: {patient[4]}")
    else:
        st.write("Patient not found")


    
 #function to update the patient details       
def update_patient(patient_id, name, age, gender, mobile):
    query = "UPDATE patient_db SET name=%s, age=%s, gender=%s, mobile=%s WHERE id=%s"
    cursor.execute(query, (name, age, gender, mobile, patient_id))
    mydb.commit()


#function to delete the patient details
def delete_patient(patient_id):
    query = "DELETE FROM patient_db WHERE id=%s"
    cursor.execute(query, (patient_id,))
    mydb.commit()    
#function to display all patient details
def display_patients():
    query = "SELECT * FROM patient_db"
    cursor.execute(query)
    patients = cursor.fetchall()
    for patient in patients:
        st.write(patient)
#function to display all tables in database        
def  display_tables():
    query="SHOW TABLES" 
    cursor.execute(query)
    tables=cursor.fetchall()
    for table in tables:
        st.write(table[0])
        print("main")      
if __name__=="__main__":
      main()
      cursor.close()
      mydb.close()
      
