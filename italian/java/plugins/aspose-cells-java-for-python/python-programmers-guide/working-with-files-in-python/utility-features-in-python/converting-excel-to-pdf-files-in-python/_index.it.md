---
title: Conversione dei file Excel in PDF in Python
type: docs
weight: 20
url: /it/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Conversione di Excel in Pdf**
Per convertire Excel in file Pdf utilizzando Aspose.Cells for Java in Python, basta invocare il metodo excel_to_pdf() del modulo Converter.

**Codice Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Conversione di Excel in Pdf (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
