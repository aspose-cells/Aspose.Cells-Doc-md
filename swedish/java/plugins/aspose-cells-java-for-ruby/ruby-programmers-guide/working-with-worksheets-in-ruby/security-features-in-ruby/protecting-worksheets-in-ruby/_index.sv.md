---
title: Skydd av kalkylblad i Ruby
type: docs
weight: 10
url: /sv/java/protecting-worksheets-in-ruby/
---

## **Aspose.Cells - Skydd av kalkylblad**
För att skydda kalkylblad med **Aspose.Cells Java för Ruby**, anropa **protect_worksheet**-metoden i **protection**-modulen.

**Ruby-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Skydda kalkylblad (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
