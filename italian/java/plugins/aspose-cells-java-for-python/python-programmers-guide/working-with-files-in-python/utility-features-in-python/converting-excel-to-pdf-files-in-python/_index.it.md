---
title: Conversione di Excel in file PDF in Python
type: docs
weight: 20
url: /it/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Conversione da Excel a Pdf**
Per convertire Excel in file Pdf utilizzando Aspose.Cells for Java in Python, basta invocare excel_a_pdf() del modulo Converter.

**Python Cod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Conversione da Excel a PDF (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
