---
title: Copiare e spostare fogli di lavoro in Ruby
type: docs
weight: 10
url: /it/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Copiare e spostare fogli di lavoro**
### **Copiare i Fogli di Lavoro all'interno di una Cartella di Lavoro**
Per copiare il foglio di lavoro utilizzando **Aspose.Cells for Java in Ruby**, chiama il metodo **copy_worksheet** del modulo **copyworksheets**. Di seguito puoi vedere un esempio di codice.

**Codice Ruby**

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
### **Spostare i fogli di lavoro all'interno di un libro**
Per spostare il foglio di lavoro utilizzando **Aspose.Cells for Java in Ruby**, chiama il metodo **move_worksheet** del modulo **copyworksheets**. Di seguito puoi vedere un esempio di codice.

**Codice Ruby**

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
## **Scarica il codice in esecuzione**
Scarica **Copia e Spostamento dei fogli di lavoro (Aspose.Cells)** da uno dei siti di codice sociale di seguito indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
