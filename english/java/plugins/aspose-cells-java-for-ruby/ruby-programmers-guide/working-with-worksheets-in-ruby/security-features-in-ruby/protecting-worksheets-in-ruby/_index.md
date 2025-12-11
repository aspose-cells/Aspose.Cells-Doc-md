---
title: Protecting Worksheets in Ruby
type: docs
weight: 10
url: /java/protecting-worksheets-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Protecting Worksheets**
To protect a worksheet using **Aspose.Cells Java for Ruby**, call the **protect_worksheet** method of the **protection** module.

**Ruby Code**

{{< highlight ruby >}}
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
{{< /highlight >}}

## **Download Running Code**
Download **Protecting Worksheets (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
