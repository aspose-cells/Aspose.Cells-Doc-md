---
title: Rimuovere la protezione di un foglio di lavoro in Python
type: docs
weight: 20
url: /it/java/unprotect-a-worksheet-in-python/
---
## **Aspose.Cells - Rimuovere la protezione di un foglio di lavoro**
 Per proteggere il foglio di lavoro utilizzando**Aspose.Cells Giava for Python** , chiamata**unprotect_worksheet** metodo di**protezione** modulo.

**Codice Pitone**

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
## **Scarica il codice in esecuzione**
 Scarica**Rimuovere la protezione di un foglio di lavoro (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
