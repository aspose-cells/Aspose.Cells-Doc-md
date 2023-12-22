---
title: Отобразить или скрыть линии сетки в Python
type: docs
weight: 10
url: /ru/java/display-or-hide-gridlines-in-python/
description: Узнайте, как отображать или скрывать линии сетки с помощью Aspose.Cells for Python и Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - Как отобразить или скрыть линии сетки**
###  **Как скрыть линии сетки**
 Чтобы скрыть рабочий лист, используя**Aspose.Cells Java для Ruby**, позвоните **displayhidegridlines** модуль.

**Код Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
###  **Как отобразить линии сетки**
Чтобы сделать линии сетки видимыми, используйте метод setGridlinesVisible(true) класса Worksheet.

**Код Python**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Загрузить рабочий код**
 Скачать**DisplayHideGridlines (Aspose.Cells)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
