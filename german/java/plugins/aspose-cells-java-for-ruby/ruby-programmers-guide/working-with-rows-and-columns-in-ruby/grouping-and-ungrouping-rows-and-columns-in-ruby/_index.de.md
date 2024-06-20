---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten in Ruby
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Gruppenverwaltung von Zeilen & Spalten**
### **Gruppierung von Zeilen & Spalten**
Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden groupRows und groupColumns der Cells-Sammlung aufgerufen werden. Beide Methoden akzeptieren die folgenden Parameter:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

**Ruby-Code**

{{< highlight ruby >}}

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
### **Zeilen & Spalten aufheben**
Gruppierte Zeilen oder Spalten aufheben, indem die Methoden UngroupRows und UngroupColumns der Cells-Sammlung aufgerufen werden. Beide Methoden akzeptieren die gleichen Parameter:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

**Ruby-Code**

{{< highlight ruby >}}

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
## **Laufenden Code herunterladen**
Gruppierung & Aufhebung der Gruppierung von Zeilen & Spalten (Aspose.Cells) von einer der unten genannten sozialen Codierungsseiten herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
