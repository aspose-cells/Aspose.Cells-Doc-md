---
title: Dölja och visa rader och kolumner i Ruby
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Kontrollera synligheten för rader och kolumner**
### **Döljer rader och kolumner**
Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna HideRow och HideColumn i samlingen Cells. Båda metoderna tar rad/kolumnindex som en parameter för att dölja den specifika raden eller kolumnen.

**Ruby kod**

{{< highlight "ruby" >}}

 def hide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Hiding the 3rd row of the worksheet

    cells.hideRow(2)

    # Hiding the 2nd column of the worksheet

    cells.hideColumn(1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Hide Rows And Columns.xls")

    puts "Hide Rows And Columns Successfully."

end

{{< /highlight >}}
### **Visar rader och kolumner**
Utvecklare kan visa alla dolda rader eller kolumner genom att anropa metoderna UnhideRow och UnhideColumn i samlingen Cells. Båda metoderna tar två parametrar:

- **Rowor kolumnindex**- indexet för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd**- radhöjden eller kolumnbredden som tilldelats raden eller kolumnen efter att den har visats.

**Ruby kod**

{{< highlight "ruby" >}}

 def unhide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Unhiding the 3rd row and setting its height to 13.5

    cells.unhideRow(2,13.5)

    # Unhiding the 2nd column and setting its width to 8.5

    cells.unhideColumn(1,8.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unhide Rows And Columns.xls")

    puts "Unhide Rows And Columns Successfully."

end

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Kontrollera synligheten för rader och kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
