﻿---
title: Предварительный просмотр разрыва страницы в Python
type: docs
weight: 60
url: /ru/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 Чтобы настроить рабочий лист для предварительного просмотра разрыва страницы, используя**Aspose.Cells Java for Python** , просто вызовите**PageBreakПредварительный просмотр** модуль.

**Python Код**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Предварительный просмотр разрыва страницы (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
