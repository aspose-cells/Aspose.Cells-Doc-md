---
title: Gestionar Hojas de Cálculo en Ruby
type: docs
weight: 10
url: /es/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Gestionar Hojas de Cálculo**
### **Añadir hojas de cálculo a un nuevo archivo de Excel**
Para agregar una hoja de cálculo a un nuevo archivo de Excel usando **Aspose.Cells Java para Ruby**, simplemente llama al método **add_worksheet** del módulo **MangingWorksheets**.

**Código Ruby**

{{< highlight ruby >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Añadir hojas de cálculo a una hoja de cálculo de diseñador**
El proceso de agregar hojas de cálculo a una hoja de cálculo de diseño es completamente igual al enfoque anterior, excepto que el archivo de Excel ya está creado y necesitamos abrir ese archivo de Excel primero antes de agregar la hoja de cálculo.

**Código Ruby**

{{< highlight ruby >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Acceso a las hojas de cálculo usando el nombre de la hoja**
Para acceder a la hoja de cálculo por el nombre de la hoja usando **Aspose.Cells Java para Ruby**, simplemente llama al método **get_worksheet** del módulo **MangingWorksheets**.

**Código Ruby**

{{< highlight ruby >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Eliminar hojas de cálculo utilizando el nombre de la hoja**
Para eliminar una hoja de cálculo por nombre de hoja usando **Aspose.Cells Java para Ruby**, simplemente llama al método **remove_worksheet_by_name** del módulo **MangingWorksheets**.

**Código Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Eliminar hojas de cálculo utilizando el índice de la hoja**
Para eliminar una hoja de cálculo por índice de hoja usando **Aspose.Cells Java para Ruby**, simplemente llama al método **remove_worksheet_by_index** del módulo **MangingWorksheets**.

**Código Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Gestión de Hojas de Cálculo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
