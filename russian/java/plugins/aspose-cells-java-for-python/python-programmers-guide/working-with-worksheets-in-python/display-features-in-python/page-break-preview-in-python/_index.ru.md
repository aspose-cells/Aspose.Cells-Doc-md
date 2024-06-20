---
title: Просмотр разрыва страницы в Python
type: docs
weight: 60
url: /ru/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
Чтобы установить лист в режим предварительного просмотра разрыва страницы с использованием **Aspose.Cells Java для Python**, просто вызовите модуль **PageBreakPreview**.

**Код Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Предварительный просмотр разрыва страницы (Aspose.Cells)** с любого из упомянутых ниже сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
