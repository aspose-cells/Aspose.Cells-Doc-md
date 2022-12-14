---
title: Copiar y mover hojas de trabajo en Ruby
type: docs
weight: 10
url: /es/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - Copiar y mover hojas de trabajo**
### **Copiar hojas de trabajo dentro de un libro de trabajo**
 Para copiar la hoja de trabajo usando**Aspose.Cells for Java en rubí** , llamar**copiar_hoja de trabajo** método de**hojas de trabajo** módulo. A continuación puede ver un ejemplo de código.

**código rubí**

{{< highlight "ruby" >}}

 def copy_worksheet(workbook)

    # Create a Worksheets object with reference to the sheets of the Workbook.

    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.

    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."

end 

{{< /highlight >}}
### **Mover hojas de trabajo dentro de un libro de trabajo**
 Para mover la hoja de trabajo usando**Aspose.Cells for Java en rubí** , llamar**mover_hoja de trabajo** método de**hojas de trabajo** módulo. A continuación puede ver un ejemplo de código.

**código rubí**

{{< highlight "ruby" >}}

 def move_worksheet(workbook)

    # Get the first worksheet in the book.

    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.

    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."

end 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Copiar y mover hojas de trabajo (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
