---
title: Infoga och ta bort rader och kolumner i Ruby
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Hantera rader/kolumner**
### **Infoga en rad**
Infoga en rad på valfri plats genom att anropa metoden insertRows i samlingen Cells. Metoden insertRows tar indexet för raden där den nya raden kommer att infogas som det första argumentet, och antalet rader som ska infogas som det andra argumentet.

**Ruby kod**

{{< highlight "ruby" >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **Infoga flera rader**
Om du vill infoga flera rader i kalkylbladet anropar du metoden insertRows i samlingen Cells. Metoden InsertRows tar två parametrar:

- Radindex, indexet för raden varifrån de nya raderna kommer att infogas.
- Antal rader, totalt antal rader som behöver infogas.

**Ruby kod**

{{< highlight "ruby" >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **Ta bort en rad**
För att ta bort en rad på valfri plats, anropa metoden deleteRows för samlingen Cells. Metoden DeleteRows tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Ruby kod**

{{< highlight "ruby" >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **Ta bort flera rader**
Om du vill ta bort flera rader från ett kalkylblad anropar du metoden deleteRows i samlingen Cells. Metoden DeleteRows tar två parametrar:

- Radindex, indexet för raden där raderna kommer att tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Ruby kod**

{{< highlight "ruby" >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i kalkylbladet var som helst genom att anropa metoden insertColumns i samlingen Cells. metoden insertColumns tar två parametrar:

- Kolumnindex, indexet för den kolumn varifrån kolumnen kommer att infogas
- Antal kolumner, totalt antal kolumner som behöver infogas

**Ruby kod**

{{< highlight "ruby" >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **Ta bort en kolumn**
För att ta bort en kolumn från kalkylbladet på valfri plats, anropa metoden deleteColumns i samlingen Cells. Metoden deleteColumns använder följande parametrar:

- Kolumnindex, indexet för den kolumn där kolumnen kommer att tas bort.
- Antal kolumner, totalt antal kolumner som behöver raderas.
- Skift celler, boolesk parameter för att indikera om cellerna ska flyttas åt vänster efter radering.

**Ruby kod**

{{< highlight "ruby" >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Hantera rader/kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
