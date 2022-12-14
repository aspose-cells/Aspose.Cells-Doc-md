---
title: Display or Hide Tabs in Python
type: docs
weight: 30
url: /java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Display Hide Tabs**
### **Hiding Tabs**
To hide tabs using **Aspose.Cells Java for Ruby**, call **displayhidetabs** module.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Making Tabs Visible**
Make tabs visible with the Workbook class' setSheetTabBarHidden(false) method.

**Python Code**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
