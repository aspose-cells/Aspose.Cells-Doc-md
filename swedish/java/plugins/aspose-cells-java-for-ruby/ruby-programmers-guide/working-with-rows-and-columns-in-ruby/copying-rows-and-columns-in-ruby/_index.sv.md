---
title: Kopiera rader och kolumner i Ruby
type: docs
weight: 30
url: /sv/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Kopiera rader och kolumner**
### **Kopiera rader**
Aspose.Cells tillhandahåller metoden copyRow för klassen Cells. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till målraden.

Metoden copyRow tar följande parametrar:

- källan Cells objekt,
- källradens index, och
- destinationsradindex.

**Ruby kod**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Kopiera kolumner**
Aspose.Cells tillhandahåller metoden copyColumn för klassen Cells, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till målkolumnen.

Metoden copyColumn använder följande parametrar:

- källan Cells objekt,
- källkolumnindex och
- målkolumnindex.

**Ruby kod**

{{< highlight "ruby" >}}

 def copy_columns()

data_dir = File.dirname(File.dirname(File.dirname(__FIL__))) + '/data/'



# Instantiera ett arbetsboksobjekt med excel-filsökväg

arbetsbok = Rjb::import('com.aspose.cells.Workbook').ny

# Åtkomst till det första kalkylbladet i Excel-filen

arbetsblad = workbook.getWorksheets().get(0)

# Lägg några data i rubrikrader (A1:A4)

= 0

 medan jag< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Kopiera rader och kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
