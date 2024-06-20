---
title: Группировка и разгруппировка строк и столбцов в Python
type: docs
weight: 40
url: /ru/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Узнайте, как группировать и разгруппировывать строки и столбцы с помощью Aspose.Cells для Python через API Java.
keywords: Как группировать и разгруппировывать строки и столбцы в Python через Java, Группировать строки и столбцы с помощью Python через Java, Разгруппировывать строки и столбцы с помощью Python через Java. 
---

## **Управление группировкой и разгруппировкой строк и столбцов в Aspose.Cells для Python via Java**
### **Как сгруппировать строки и столбцы в Python**
Возможно группировать строки или столбцы, вызывая методы groupRows и groupColumns коллекции Cells. Оба метода принимают следующие параметры:

- Индекс первой строки/столбца в группе.
- Индекс последней строки/столбца в группе.
- Скрыто, логический параметр, указывающий, нужно ли скрыть строки/столбцы после группировки.

**Код Python**

{{< highlight python >}}

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
### **Как отменить группировку строк и столбцов с помощью Python**
Расгруппировать сгруппированные строки или столбцы, вызвав методы UngroupRows и UngroupColumns коллекции Cells. Оба методы принимают те же параметры:

- Индекс первой строки/столбца, которую нужно разгруппировать.
- Индекс последней строки/столбца, которую нужно разгруппировать.

**Код Python**

{{< highlight python >}}

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
## **Скачать работающий код**
Скачайте **Группировка и расгруппировка строк и столбцов (Aspose.Cells)** с одного из упомянутых ниже социальных сайтов с кодом:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
