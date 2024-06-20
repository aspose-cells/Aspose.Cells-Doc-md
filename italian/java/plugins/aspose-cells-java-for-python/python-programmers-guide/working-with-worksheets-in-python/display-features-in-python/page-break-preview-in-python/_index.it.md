---
title: Anteprima interruzioni di pagina in Python
type: docs
weight: 60
url: /it/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
Per impostare il foglio di lavoro in anteprima interruzioni di pagina usando **Aspose.Cells Java per Python**, semplicemente invoca il modulo **PageBreakPreview**.

**Codice Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Anteprima interruzioni di pagina (Aspose.Cells)** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
