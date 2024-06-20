---
title: Conversione dei file Excel in HTML in Python
type: docs
weight: 10
url: /it/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Conversione del file Excel in HTML**
Per convertire Excel in HTML utilizzando Aspose.Cells for Java in Python, basta invocare il metodo worksheet_to_html() del modulo Converter.

**Codice Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Conversione del File Excel in HTML (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
