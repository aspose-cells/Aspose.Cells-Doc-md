---
title: Copiar y Mover hojas de cálculo en Ruby
type: docs
weight: 10
url: /es/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Copiar y Mover hojas de cálculo**
### **Copiar Hojas de Cálculo dentro de un Libro de Trabajo**
Para copiar una hoja de cálculo usando **Aspose.Cells for Java en Ruby**, llama al método **copy_worksheet** del módulo **copyworksheets**. A continuación puedes ver un ejemplo de código.

**Código Ruby**

{{< highlight ruby >}}

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
### **Mover hojas de cálculo dentro de un libro de trabajo**
Para mover una hoja de cálculo usando **Aspose.Cells for Java en Ruby**, llama al método **move_worksheet** del módulo **copyworksheets**. A continuación puedes ver un ejemplo de código.

**Código Ruby**

{{< highlight ruby >}}

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
## **Descargar Código en Ejecución**
Descargar **Copiando y Moviendo Hojas de Cálculo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
