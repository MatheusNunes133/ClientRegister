import tkinter as tk
import pandas as pd

from database.database import ConnectDatabase


def save_client():
    name = entry_name.get()
    lastname= entry_lastname.get()
    age = entry_age.get()
    email = entry_email.get()
    phone = entry_phone.get()

    database = ConnectDatabase()
    try:
        if database.check_table_exists():
            database.save(name, lastname, age, email, phone)
            delete_inputs()
        else:
            database.create_table()
            database.save(name, lastname, age, email, phone)
            delete_inputs()
    except Exception as e:
        print(f"Erro ao salvar cliente: {e}")
    finally:
        database.close_connection()


def data_export():
    database_clients = []
    database = ConnectDatabase()
    all_clients = database.get_all_clients()

    for client in all_clients:
        database_clients.append((client.name, client.lastname, client.age, client.email, client.phone))

    excel_clients = pd.DataFrame(database_clients, columns=["Nome", "Sobrenome", "Idade", "Email", "Telefone"])
    excel_clients.to_excel("banco_clientes.xlsx")


def delete_inputs():
    entry_name.delete(0, "end")
    entry_lastname.delete(0, "end")
    entry_age.delete(0, "end")
    entry_email.delete(0, "end")
    entry_phone.delete(0, "end")

window = tk.Tk()

window.title("Cadastro de Clientes")

# Labels
label_name = tk.Label(window, text="Nome:")
label_name.grid(row=0, column=0, padx=10, pady=10,)

label_lastname = tk.Label(window, text="Sobrenome")
label_lastname.grid(row=1, column=0, padx=10, pady=10)

label_age = tk.Label(window, text="Idade")
label_age.grid(row=2, column=0, padx=10, pady=10)

label_email = tk.Label(window, text="Email")
label_email.grid(row=3, column=0, padx=10, pady=10)

label_phone = tk.Label(window, text="Telefone")
label_phone.grid(row=4, column=0, padx=10, pady=10)

# Entry // Inputs

entry_name = tk.Entry(window, text="Nome:", width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

entry_lastname = tk.Entry(window, text="Sobrenome", width=30)
entry_lastname.grid(row=1, column=1, padx=10, pady=10)

entry_age = tk.Entry(window, text="Idade", width=30)
entry_age.grid(row=2, column=1, padx=10, pady=10)

entry_email = tk.Entry(window, text="Email", width=30)
entry_email.grid(row=3, column=1, padx=10, pady=10)

entry_phone = tk.Entry(window, text="Telefone", width=30)
entry_phone.grid(row=4, column=1, padx=10, pady=10)

# Buttons

save_button = tk.Button(window, text="Salvar Cliente", command=save_client)
save_button.grid(row=6, column=0, padx=10, pady=10)

export_button = tk.Button(window, text="Exportar Dados", command=data_export)
export_button.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()