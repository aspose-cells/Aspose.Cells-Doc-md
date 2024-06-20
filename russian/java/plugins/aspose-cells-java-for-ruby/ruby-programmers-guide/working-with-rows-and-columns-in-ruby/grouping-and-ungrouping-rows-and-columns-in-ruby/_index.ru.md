---
title: Группировка и расгруппировка строк и столбцов в Ruby
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---

## **Aspose.Cells - Управление группировкой строк и столбцов**
### **Группировка строк и столбцов**
Возможно группировать строки или столбцы, вызывая методы groupRows и groupColumns коллекции Cells. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

**Код на Ruby**

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
### **Отмена группировки строк и столбцов**
Расгруппировать сгруппированные строки или столбцы, вызвав методы UngroupRows и UngroupColumns коллекции Cells. Оба методы принимают те же параметры:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

**Код на Ruby**

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
## **Скачать работающий код**
Скачайте **Группировка и расгруппировка строк и столбцов (Aspose.Cells)** с одного из упомянутых ниже социальных сайтов с кодом:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
