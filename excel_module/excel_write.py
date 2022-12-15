import xlsxwriter


def export(session):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('employees.xlsx')
    worksheet = workbook.add_worksheet('employees')

    # Create style for cells
    header_cell_format = workbook.add_format({'bold': True, 'border': True})

    row_index = 0
    row_names = ['ФИО', 'Дата рождения', 'Наименование роли']
    worksheet.write_row('A1', row_names, header_cell_format)
    row_index += 1

    rows = session.execute('SELECT users.fio, users.datar, roles.name as id_role FROM users INNER JOIN roles'
                           ' ON users.id_role = roles.id ORDER BY users.ROWID DESC LIMIT 5')

    for i, row in enumerate(rows.fetchall(), start=row_index):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)

    workbook.close()
