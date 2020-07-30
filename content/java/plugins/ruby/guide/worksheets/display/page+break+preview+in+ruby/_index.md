---
title : "Page Break Preview in Ruby" 
description : "" 
weight : 24717 
toc : false
type: docs
url: /java/plugins/ruby/guide/worksheets/display/page+break+preview+in+ruby/
---

# Aspose.Cells for Java : Page Break Preview in Ruby


## Aspose.Cells - Page Break Preview

To set worksheet to page break preview using **Aspose.Cells Java for Ruby**, simply invoke **PageBreakPreview** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()sheet\_index = worksheets.add()worksheet = worksheets.get(sheet\_index)# Displaying the worksheet in page break previewworksheet.setPageBreakPreview(true)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Set page break preview, please check the output file."

## Download Running Code

Download **Page Break Preview (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)

