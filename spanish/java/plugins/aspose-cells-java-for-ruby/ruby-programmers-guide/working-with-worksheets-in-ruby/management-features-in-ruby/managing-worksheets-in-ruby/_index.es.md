---
title: Gestión de hojas de trabajo en Ruby
type: docs
weight: 10
url: /es/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - Gestión de hojas de trabajo**
### **Agregar hojas de trabajo a un nuevo archivo de Excel**
 Para agregar una hoja de trabajo a un nuevo archivo de Excel usando**Aspose.Cells Java para rubí** , simplemente llama**añadir_hoja de trabajo** método de**Gestión de hojas de trabajo** módulo.

**código rubí**

{{< highlight "ruby" >}}

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
### **Adición de hojas de trabajo a una hoja de cálculo de Designer**
El proceso de agregar hojas de trabajo a una hoja de cálculo de diseñador es completamente igual al del enfoque anterior, excepto que el archivo de Excel ya está creado y necesitamos abrir ese archivo de Excel primero antes de agregarle la hoja de trabajo.

**código rubí**

{{< highlight "ruby" >}}

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
### **Acceder a las hojas de trabajo usando el nombre de la hoja**
 Para acceder a la hoja de trabajo por nombre de hoja usando**Aspose.Cells Java para rubí** , simplemente llama**obtener_hoja de trabajo** método de**Gestión de hojas de trabajo** módulo.

**código rubí**

{{< highlight "ruby" >}}

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
### **Eliminación de hojas de trabajo usando el nombre de la hoja**
 Para eliminar la hoja de trabajo por nombre de hoja usando**Aspose.Cells Java para rubí** , simplemente llama**remove_worksheet_by_name** método de**Gestión de hojas de trabajo** módulo.

**código rubí**

{{< highlight "ruby" >}}

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
### **Eliminación de hojas de cálculo mediante el índice de hojas**
 Para eliminar hoja de trabajo por índice de hoja usando**Aspose.Cells Java para rubí** , simplemente llama**remove_worksheet_by_index** método de**Gestión de hojas de trabajo** módulo.

**código rubí**

{{< highlight "ruby" >}}

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
## **Descargar código de ejecución**
Descargar**Gestión de hojas de trabajo (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
