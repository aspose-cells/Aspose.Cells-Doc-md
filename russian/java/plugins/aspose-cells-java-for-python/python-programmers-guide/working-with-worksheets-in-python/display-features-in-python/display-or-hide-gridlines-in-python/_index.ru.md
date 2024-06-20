---
title: Показать или скрыть сетку в Python
type: docs
weight: 10
url: /ru/java/display-or-hide-gridlines-in-python/
description: Узнайте, как показать или скрыть сетку через Aspose.Cells для Python через Java API.
keywords: Как показать или скрыть сетку в Python через Java, показать или скрыть сетку с помощью Python через Java, Показать или Скрыть сетку на Python. 
---

## **Aspose.Cells - Как показать или скрыть сетку**
### **Как скрыть сетку**
Чтобы скрыть лист с помощью **Aspose.Cells Java для Ruby**, вызовите модуль **displayhidegridlines**.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Как показать сетку**
Чтобы сделать видимыми сетки, используйте метод setGridlinesVisible(true) класса Worksheet.

**Код Python**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Скачать работающий код**
Скачать **DisplayHideGridlines (Aspose.Cells)** с любого из упомянутых ниже социальных сайтов для кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
