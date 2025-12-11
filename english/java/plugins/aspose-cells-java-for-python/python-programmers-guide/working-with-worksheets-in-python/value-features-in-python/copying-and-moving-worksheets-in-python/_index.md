---
title: Copying and Moving Worksheets in Python
type: docs
weight: 10
url: /java/copying-and-moving-worksheets-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Copying and Moving Worksheets**
### **Copy Worksheets within a Workbook**
To copy a worksheet using **Aspose.Cells for Python**, call the **copy_worksheet** method of the **copyworksheets** module. Below you can see a code example.

**Python Code**

{{< highlight python >}}
def copy_worksheet(self):  
    # Instantiating a Workbook object by Excel file path
    workbook = self.Workbook(self.dataDir + "Book1.xls")

    # Create a Worksheets object with reference to the sheets of the Workbook.
    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.
    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in the default (Excel 2003) format
    workbook.save(self.dataDir + "Copy Worksheet.xls")

    print "Copy worksheet, please check the output file."
{{< /highlight >}}

### **Move Worksheets within a Workbook**
To move a worksheet using **Aspose.Cells for Python**, call the **move_worksheet** method of the **copyworksheets** module. Below you can see a code example.

{{< highlight python >}}
def move_worksheet(self):
    # Instantiating a Workbook object by Excel file path
    workbook = self.Workbook(self.dataDir + "Book1.xls")

    # Get the first worksheet in the workbook.
    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.
    sheet.moveTo(2)

    # Saving the modified Excel file in the default (Excel 2003) format
    workbook.save(self.dataDir + "Move_Worksheet.xls")

    print "Move worksheet, please check the output file."
{{< /highlight >}}

## **Download Running Code**
Download **Copying and Moving Worksheets (Aspose.Cells)** from any of the below-mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
