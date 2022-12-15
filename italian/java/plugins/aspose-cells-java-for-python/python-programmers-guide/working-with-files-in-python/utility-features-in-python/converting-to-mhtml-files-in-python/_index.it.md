---
title: Conversione in file MHTML in Python
type: docs
weight: 30
url: /it/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - Conversione in MHTML**
Per convertire il foglio di lavoro in un file MHTML utilizzando Aspose.Cells for Java in Python, è sufficiente richiamare il foglio di lavoro_a_mhtml() del modulo Converter.

**Codice Pitone**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Conversione in MHTML (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
