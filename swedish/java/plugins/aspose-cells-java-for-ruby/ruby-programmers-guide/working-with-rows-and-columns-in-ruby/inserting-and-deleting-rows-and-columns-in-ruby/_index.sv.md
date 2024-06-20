---
title: Infoga och ta bort rader och kolumner i Ruby
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Hantera rader/kolumner**
### **Infoga en rad**
Infoga en rad på valfri plats genom att anropa insertRows metoden i Cells-kollektionen. insertRows metoden tar indexet för raden där den nya raden ska infogas som första argument, och antalet rader som ska infogas som andra argument.

**Ruby-kod**

{{< highlight ruby >}}

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
För att infoga flera rader i arket, anropa insertRows metoden i Cells-kollektionen. InsertRows metoden tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, totalt antal rader som behöver infogas.

**Ruby-kod**

{{< highlight ruby >}}

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
För att ta bort en rad på valfri plats, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Ruby-kod**

{{< highlight ruby >}}

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
För att ta bort flera rader från ett kalkylblad, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Ruby-kod**

{{< highlight ruby >}}

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
Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa metoden insertColumns i Cells-samlingen. insertColumns-metoden tar två parametrar:

- Kolumnindex, index av kolumn där kolumnen ska infogas
- Antal kolumner, totalt antal kolumner som behöver infogas

**Ruby-kod**

{{< highlight ruby >}}

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
För att ta bort en kolumn från arbetsbladet på valfri plats, anropas deleteColumns-metoden i Cells-samlingen. deleteColumns-metoden tar följande parametrar:

- Kolumnindex, index av kolumn där kolumnen ska tas bort.
- Antal kolumner, totalt antal kolumner som behöver tas bort.
- Skifta celler, en boolesk parameter för att indikera om cellerna ska skiftas åt vänster efter borttagning.

**Ruby-kod**

{{< highlight ruby >}}

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
## **Ladda ned körbar kod**
Ladda ned **Hantering av rader/kolumner (Aspose.Cells)** från någon av de nämnda sociala kodsajterna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
