---
title: Split Panes in Ruby
type: docs
weight: 80
url: /java/split-panes-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Split Panes**
To split panes using **Aspose.Cells for Java in Ruby**, simply invoke the **SplitPanes** module.

**Ruby Code**

{{< highlight ruby >}}

data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

# Instantiating a Workbook object by an Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

# Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20")

# Split the worksheet window
workbook.getWorksheets().get(0).split()

# Saving the modified Excel file in the default format (Excel 2003)
workbook.save(data_dir + "SplitPanes output.xls")

puts "Panes split successfully."

{{< /highlight >}}

## **Download Running Code**
Download **Split Panes (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)
