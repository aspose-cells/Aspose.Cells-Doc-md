---
title: Скрытие и показ строк и столбцов в Python
type: docs
weight: 50
url: /ru/java/hiding-and-showing-rows-and-columns-in-python/
description: Узнайте, как скрывать и показывать строки и столбцы через Aspose.Cells для Python через API Java.
keywords: Как скрывать и показывать строки и столбцы в Python через Java, скрыть строки и столбцы с помощью Python через Java, показать строки и столбцы через Python через Java, скрыть строки и столбцы. 
---

## **Aspose.Cells - Управление видимостью строк и столбцов**
### **Как скрыть строки и столбцы**
Разработчики могут скрыть строку или столбец, вызвав методы HideRow и HideColumn соответственно коллекции Cells. Оба метода принимают индекс строки/столбца в качестве параметра, чтобы скрыть конкретную строку или столбец.

**Код на Ruby**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Как показать строки и столбцы**
Разработчики могут отобразить скрытую строку или столбец, вызвав методы UnhideRow и UnhideColumn соответственно коллекции Cells. Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после ее отображения.

**Код на Ruby**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Управление видимостью строк и столбцов (Aspose.Cells)** с любого из нижеупомянутых сайтов социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
