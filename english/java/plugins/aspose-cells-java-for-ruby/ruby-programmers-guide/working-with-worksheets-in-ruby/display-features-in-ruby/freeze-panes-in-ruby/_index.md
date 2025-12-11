---
title: Freeze Panes in Ruby
type: docs
weight: 50
url: /java/freeze-panes-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Freeze Panes**
To freeze panes in a spreadsheet document using **Aspose.Cells Java for Ruby**, simply invoke the **FreezePanes** module.

**Ruby Code**

{{< highlight ruby >}}

data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

# Instantiating a Workbook object by an Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)

# Applying freeze pane settings
worksheet.freezePanes(3, 2, 3, 2)

# Saving the modified Excel file in the default (Excel 2003) format
workbook.save(data_dir + "output.xls")
puts "Applied freeze pane settings; please check the output file."

{{< /highlight >}}

## **Download Sample Code**
Download **Freeze Panes (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
