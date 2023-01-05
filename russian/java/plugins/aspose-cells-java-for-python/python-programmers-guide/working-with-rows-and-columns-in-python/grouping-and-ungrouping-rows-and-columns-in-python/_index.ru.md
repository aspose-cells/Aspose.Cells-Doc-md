---
title: Группировка и разгруппировка строк и столбцов в Python
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns-in-python/
---
## **Aspose.Cells - Групповое управление строками и столбцами**
### **Группировка строк и столбцов**
Можно сгруппировать строки или столбцы, вызвав методы groupRows и groupColumns коллекции Cells. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца, первая строка или столбец в группе.
- Индекс последней строки/столбца, последняя строка или столбец в группе.
- Скрыт, логический параметр, указывающий, следует ли скрывать строки/столбцы после группировки или нет.

**Python Код**

{{< highlight "python" >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
### **Разгруппировка строк и столбцов**
Разгруппируйте сгруппированные строки или столбцы, вызвав методы UngroupRows и UngroupColumns коллекции Cells. Оба метода принимают одни и те же параметры:

- Индекс первой строки или столбца, первая строка/столбец, подлежащий разгруппировке.
- Индекс последней строки или столбца, последняя строка/столбец для разгруппировки.

**Python Код**

{{< highlight "python" >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Группировать и разгруппировать строки и столбцы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
