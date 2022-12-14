---
title: Conversione di file Excel in HTML in Python
type: docs
weight: 10
url: /it/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - Conversione file Excel in HTML**
Per convertire Excel in HTML utilizzando Aspose.Cells for Java in Python, è sufficiente richiamare il foglio di lavoro_a_html() del modulo Converter.

**Python Cod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Conversione di file Excel in HTML (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
