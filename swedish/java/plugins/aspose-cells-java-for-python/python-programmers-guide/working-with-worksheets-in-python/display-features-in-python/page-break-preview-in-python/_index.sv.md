---
title: Förhandsvisning av sidbrytning i Python
type: docs
weight: 60
url: /sv/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 För att ställa in kalkylblad till förhandsgranskning av sidbrytning med**Aspose.Cells Java for Python** , helt enkelt åberopa**PageBreakPreview** modul.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Förhandsgranskning av sidbrytning (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
