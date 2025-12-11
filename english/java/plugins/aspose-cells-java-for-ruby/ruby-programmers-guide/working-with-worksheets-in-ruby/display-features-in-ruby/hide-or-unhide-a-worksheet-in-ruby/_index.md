---
title: Hide or Unhide a Worksheet in Ruby
type: docs
weight: 60
url: /java/hide-or-unhide-a-worksheet-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Hide or Unhide a Worksheet**
### **Hiding a Worksheet**
To hide a worksheet using Aspose.Cells Java for Ruby, call the **hideunhideworksheet** module.

**Ruby Code**

{{< highlight ruby >}}

data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

# Instantiating a Workbook object by Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file
worksheet.setVisible(false)

# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(data_dir + "output.xls")
puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Showing a Worksheet**
Developers can make a worksheet visible by calling the `setVisible(true)` method of the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class.

**Ruby Code**

{{< highlight ruby >}}

# Displaying the worksheet of the Excel file
worksheet.setVisible(true)

{{< /highlight >}}
## **Download Running Code**
Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
