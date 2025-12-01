---
title: Hide or Unhide a Worksheet in Python
type: docs
weight: 50
url: /java/hide-or-unhide-a-worksheet-in-python/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Hide or Unhide a Worksheet**
### **Hiding a Worksheet**
To hide worksheet using Aspose.Cells Java for Ruby, call **hideunhideworksheet** module.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Showing a Worksheet**
Developers can make a worksheet visible by setting the *setVisible(* *true* *)* method of the **Worksheet** class.

**Python Code**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Download Running Code**
Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
