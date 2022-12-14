---
title: Группировка и разгруппировка строк и столбцов в Ruby
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Групповое управление строками и столбцами**
### **Группировка строк и столбцов**
Можно сгруппировать строки или столбцы, вызвав методы groupRows и groupColumns коллекции Cells. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыт, логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.

**Рубиновый код**

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
### **Разгруппировка строк и столбцов**
Разгруппируйте сгруппированные строки или столбцы, вызвав методы UngroupRows и UngroupColumns коллекции Cells. Оба метода принимают одни и те же параметры:

- Индекс первой строки или столбца, первая строка/столбец, подлежащий разгруппировке.
- Индекс последней строки или столбца, последняя строка/столбец для разгруппировки.

**Рубиновый код**

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
## **Скачать рабочий код**
 Скачать**Группировать и разгруппировать строки и столбцы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
