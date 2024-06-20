---
title: Fattore di zoom in Python
type: docs
weight: 80
url: /it/java/zoom-factor-in-python/
---

## **Aspose.Cells - Fattore di zoom**
Per impostare il fattore di zoom con **Aspose.Cells Java per Python**, basta invocare il modulo **ZoomFactor**.

**Codice Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Zoom Factor (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
