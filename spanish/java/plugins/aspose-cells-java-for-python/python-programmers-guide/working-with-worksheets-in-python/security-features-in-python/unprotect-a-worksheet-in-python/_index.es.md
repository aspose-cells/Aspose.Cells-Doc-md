---
title: Desproteger una hoja de cálculo en Python
type: docs
weight: 20
url: /es/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - Desproteger una hoja de cálculo**
Para desproteger una hoja de cálculo usando **Aspose.Cells Java para Python**, llame al método **unprotect_worksheet** del módulo **protection**.

**Código Python**

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
## **Descargar Código en Ejecución**
Descargar **Desproteger una hoja de cálculo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
