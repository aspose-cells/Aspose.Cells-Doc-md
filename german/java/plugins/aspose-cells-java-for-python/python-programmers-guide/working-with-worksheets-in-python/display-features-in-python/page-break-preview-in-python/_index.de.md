---
title: Seitenumbruchvorschau in Python
type: docs
weight: 60
url: /de/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
Um das Arbeitsblatt mit **Aspose.Cells Java für Python** auf Seitenumbruchvorschau zu setzen, rufen Sie einfach das Modul **PageBreakPreview** auf.

**Python-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Page Break Preview (Aspose.Cells)** von einer der unten genannten Coding-Plattformen herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
