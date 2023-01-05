---
title: Ta bort skyddet av ett arbetsblad på Python
type: docs
weight: 20
url: /sv/java/unprotect-a-worksheet-in-python/
---
## **Aspose.Cells - Ta bort skyddet av ett arbetsblad**
 För att skydda kalkylblad med hjälp av**Aspose.Cells Java for Python** , ringa upp**unprotect_worksheet** metod av**skydd** modul.

**Python Kod**

{{< highlight "java" >}}

 filesFormatType = self.FileFormatType

# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

# The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

# Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

# Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Ta bort skyddet av ett kalkylblad (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
