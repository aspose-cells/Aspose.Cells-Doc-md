---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten in Ruby
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Gruppenverwaltung von Zeilen und Spalten**
### **Gruppieren von Zeilen und Spalten**
Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden groupRows und groupColumns der Sammlung Cells aufgerufen werden. Beide Methoden nehmen die folgenden Parameter:

- Index der ersten Zeile/Spalte, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.

**Ruby-Code**

{{< highlight "ruby" >}}

 def group_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    cells.groupRows(0,5,true)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    cells.groupColumns(0,2,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Group Rows And Columns.xls")

    puts "Group Rows And Columns Successfully."

end  

{{< /highlight >}}
### **Gruppierung von Zeilen und Spalten aufheben**
Heben Sie die Gruppierung gruppierter Zeilen oder Spalten auf, indem Sie die Methoden UngroupRows und UngroupColumns der Sammlung Cells aufrufen. Beide Methoden verwenden die gleichen Parameter:

- Index der ersten Zeile oder Spalte, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.

**Ruby-Code**

{{< highlight "ruby" >}}

 def ungroup_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Ungrouping first six rows (from 0 to 5)

    cells.ungroupRows(0,5)

    # Ungrouping first three columns (from 0 to 2)

    cells.ungroupColumns(0,2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Ungroup Rows And Columns.xls")

    puts "Ungroup Rows And Columns Successfully."

end

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Zeilen und Spalten gruppieren und Gruppierung aufheben (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
