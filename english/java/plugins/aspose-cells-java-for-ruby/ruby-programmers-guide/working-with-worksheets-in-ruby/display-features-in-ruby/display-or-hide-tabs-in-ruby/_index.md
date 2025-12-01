---
title: Display or Hide Tabs in Ruby
type: docs
weight: 40
url: /java/display-or-hide-tabs-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display or Hide Tabs**
### **Hiding Tabs**
To hide tabs using **Aspose.Cells Java for Ruby**, call **displayhidetabs** module.

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Making Tabs Visible**
Make tabs visible with the Workbook class' setSheetTabBarHidden(false) method.

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Download Running Code**
Download **Hide or Display or Hide Tabs (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
