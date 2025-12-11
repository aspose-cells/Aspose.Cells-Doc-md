---
title: Display or Hide Scroll Bars in Ruby
type: docs
weight: 30
url: /java/display-or-hide-scroll-bars-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display or Hide Scroll Bars**
### **Hiding Scroll Bars**
To hide scroll bars using **Aspose.Cells Java for Ruby**, call **the displayhidescrollbars module**.

**Ruby Code**

{{< highlight ruby >}}
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object from an Excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in the default (that is Excel 2003) format
workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."
{{< /highlight >}}

### **Making Scroll Bars Visible**
Make scroll bars visible by setting the Workbook class’s **setVScrollBarVisible()** or **setHScrollBarVisible()** methods to **true**.

**Ruby Code**

{{< highlight ruby >}}
\# Displaying the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(true)
{{< /highlight >}}

## **Download Running Code**
Download **Display or Hide Scroll Bars (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
