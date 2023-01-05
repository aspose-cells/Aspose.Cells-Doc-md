---
title: Display or Hide Scroll Bars in Python
type: docs
weight: 20
url: /java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Display or Hide Scroll Bars**
### **Hiding Row/Column Headers**
To hide row/column headers using **Aspose.Cells Java for Python**, call **DisplayHideRowColumnHeaders** module.

**Python Code**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Making Row/Column Headers Visible**
Make row and column headers visible by using the Worksheet class' setRowColumnHeadersVisible(true) method.

**Python Code**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
