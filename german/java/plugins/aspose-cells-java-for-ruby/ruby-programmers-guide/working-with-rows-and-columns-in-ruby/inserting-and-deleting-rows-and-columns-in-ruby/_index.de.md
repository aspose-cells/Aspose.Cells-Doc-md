---
title: Einfügen und Löschen von Zeilen und Spalten in Ruby
type: docs
weight: 60
url: /de/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells – Verwalten von Zeilen/Spalten**
### **Einfügen einer Zeile**
Fügen Sie an einer beliebigen Stelle eine Zeile ein, indem Sie die Methode insertRows der Sammlung Cells aufrufen. Die insertRows-Methode verwendet den Index der Zeile, in die die neue Zeile eingefügt wird, als erstes Argument und die Anzahl der einzufügenden Zeilen als zweites Argument.

**Ruby-Code**

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
### **Mehrere Zeilen einfügen**
Um mehrere Zeilen in das Arbeitsblatt einzufügen, rufen Sie die Methode insertRows der Sammlung Cells auf. Die Methode InsertRows akzeptiert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, Gesamtzahl der Zeilen, die eingefügt werden müssen.

**Ruby-Code**

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
### **Löschen einer Zeile**
Um eine Zeile an einer beliebigen Stelle zu löschen, rufen Sie die Methode deleteRows der Sammlung Cells auf. Die Methode DeleteRows akzeptiert zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtzahl der Zeilen, die gelöscht werden müssen.

**Ruby-Code**

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
### **Löschen mehrerer Zeilen**
Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode deleteRows der Sammlung Cells auf. Die Methode DeleteRows akzeptiert zwei Parameter:

- Zeilenindex, der Index der Zeile, aus der die Zeilen gelöscht werden.
- Anzahl der Zeilen, Gesamtzahl der Zeilen, die gelöscht werden müssen.

**Ruby-Code**

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
### **Einfügen einer Spalte**
Entwickler können auch an beliebiger Stelle eine Spalte in das Arbeitsblatt einfügen, indem sie die Methode insertColumns der Sammlung Cells aufrufen. Die insertColumns-Methode benötigt zwei Parameter:

- Spaltenindex, der Index der Spalte, aus der die Spalte eingefügt wird
- Anzahl der Spalten, Gesamtzahl der Spalten, die eingefügt werden müssen

**Ruby-Code**

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
### **Löschen einer Spalte**
Um eine Spalte an einer beliebigen Stelle aus dem Arbeitsblatt zu löschen, rufen Sie die Methode deleteColumns der Sammlung Cells auf. Die Methode deleteColumns akzeptiert die folgenden Parameter:

- Spaltenindex, der Index der Spalte, aus der die Spalte gelöscht wird.
- Anzahl der Spalten, Gesamtzahl der Spalten, die gelöscht werden müssen.
- Zellen verschieben, boolescher Parameter, der angibt, ob die Zellen nach dem Löschen nach links verschoben werden sollen.

**Ruby-Code**

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
## **Laufcode herunterladen**
 Download**Zeilen/Spalten verwalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
