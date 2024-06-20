---
title: Sidbrytningsgranskning i Python
type: docs
weight: 60
url: /sv/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
För att ställa in arbetsblad till sidbrytningsgranskning med **Aspose.Cells Java för Python**, helt enkelt anropa modulen **PageBreakPreview**.

**Python-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Sidbrytningsgranskning (Aspose.Cells)** från någon av de nedan angivna sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
