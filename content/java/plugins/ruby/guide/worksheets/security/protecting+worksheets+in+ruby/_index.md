---
title : "Protecting Worksheets in Ruby" 
description : "" 
weight : 24725 
toc : false
type: docs
url: /java/plugins/ruby/guide/worksheets/security/protecting+worksheets+in+ruby/
---

# Aspose.Cells for Java : Protecting Worksheets in Ruby


## Aspose.Cells - Protecting Worksheets

To protect worksheet using **Aspose.Cells Java for Ruby**, call **protect\_worksheet** method of **protection** module.

**Ruby Code**

{{< code lang="cs" >}}
def protect_worksheet()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')
    
    # Accessing the first worksheet in the Excel file
    worksheets = workbook.getWorksheets()
    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats
    protection.setAllowEditingContent(false)
    protection.setAllowEditingObject(false)
    protection.setAllowEditingScenario(false)

    # Protects the first worksheet with a password "1234"
    protection.setPassword("1234")
    
    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Protect Worksheet.xls")

    puts "Protect a Worksheet, please check the output file."
end   
{{< /code >}}

## Download Running Code

Download **Protecting Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)

