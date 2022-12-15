---
title: Zoomfaktor på Python
type: docs
weight: 80
url: /sv/java/zoom-factor-in-python/
---
## **Aspose.Cells - Zoomfaktor**
 För att ställa in zoomfaktor med**Aspose.Cells Java for Python** , helt enkelt åberopa**ZoomFactor** modul.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Zoomfaktor (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
