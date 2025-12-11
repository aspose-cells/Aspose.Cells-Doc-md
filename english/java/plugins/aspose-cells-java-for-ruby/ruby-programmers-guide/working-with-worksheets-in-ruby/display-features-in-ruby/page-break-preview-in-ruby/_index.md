---
title: Page Break Preview in Ruby
type: docs
weight: 70
url: /java/page-break-preview-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Page Break Preview**
To set a worksheet to page break preview using **Aspose.Cells for Java in Ruby**, simply invoke the **PageBreakPreview** module.

**Ruby Code**

{{< highlight ruby >}}

data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

# Instantiating a Workbook object by Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
sheet_index = worksheets.add()
worksheet = worksheets.get(sheet_index)

# Displaying the worksheet in page break preview
worksheet.setPageBreakPreview(true)

# Saving the modified Excel file in the default (that is Excel 2003) format
workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}

## **Download Runnable Code**
Download **Page Break Preview (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
