---
title: Снять защиту листа в Python
type: docs
weight: 20
url: /ru/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - Снять защиту листа**
Для защиты листа с использованием **Aspose.Cells Java для Python** вызовите метод **unprotect_worksheet** модуля **protection**.

**Код Python**

{{< highlight java >}}

 filesFormatType = self.FileFormatType

#Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

#Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Снять защиту листа (Aspose.Cells)** с любого из упомянутых ниже сайтов для социальной разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
