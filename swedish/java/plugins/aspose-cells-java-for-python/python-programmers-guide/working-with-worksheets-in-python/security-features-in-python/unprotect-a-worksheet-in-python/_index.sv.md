---
title: Avskydda ett arbetsblad i Python
type: docs
weight: 20
url: /sv/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - Avskydda ett kalkylblad**
För att skydda ett arbetsblad med **Aspose.Cells Java för Python**, anropa metoden **unprotect_worksheet** inom modulen **protection**.

**Python-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Avskydda ett arbetsblad (Aspose.Cells)** från någon av de nedan angivna sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
