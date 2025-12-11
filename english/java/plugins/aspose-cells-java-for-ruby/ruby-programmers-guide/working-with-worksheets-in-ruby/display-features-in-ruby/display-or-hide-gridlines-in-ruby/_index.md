---
title: Display or Hide Gridlines in Ruby
type: docs
weight: 10
url: /java/display-or-hide-gridlines-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display or Hide Gridlines**
### **Hiding Gridlines**
To hide a worksheet using **Aspose.Cells for Java in Ruby**, call the **displayhidegridlines** module.

**Ruby Code**

{{< highlight ruby >}}
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

# Instantiating a Workbook object by the Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

# Hiding the gridlines of the first worksheet of the Excel file
worksheet.setGridlinesVisible(false)

# Saving the modified Excel file in the default (i.e., Excel 2003) format
workbook.save(data_dir + "output.xls")

puts "Gridlines are now hidden, please check the output file."
{{< /highlight >}}

### **Making Gridlines Visible**
To make gridlines visible, use the Worksheet class's `setGridlinesVisible(true)` method.

**Ruby Code**

{{< highlight ruby >}}
# Displaying the gridlines of the worksheet
worksheet.setGridlinesVisible(true)
{{< /highlight >}}

## **Download Running Code**
Download **Display or Hide Gridlines (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
