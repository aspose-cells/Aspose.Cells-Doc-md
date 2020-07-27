+++
title = "Unprotect a Worksheet in Ruby" 
description = "" 
weight = 24726 
+++

Aspose.Cells for Java : Unprotect a Worksheet in Ruby  

# Aspose.Cells for Java : Unprotect a Worksheet in Ruby


## Aspose.Cells - Unprotect a Worksheet

To protect worksheet using **Aspose.Cells Java for Ruby**, call **unprotect\_worksheet** method of **protection** module.

**Ruby Code**

{{< code lang="cs" >}}
def unprotect_worksheet()
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

    # Unprotecting the worksheet with a password
    worksheet.unprotect("1234")
    
    # Saving the modified Excel file in default (that is Excel 2003) format
    workbook.save(data_dir + "Unprotect Worksheet.xls")

    puts "Unprotect a Worksheet, please check the output file."
end   
{{< /code >}}

## Download Running Code

Download **Unprotect a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)

