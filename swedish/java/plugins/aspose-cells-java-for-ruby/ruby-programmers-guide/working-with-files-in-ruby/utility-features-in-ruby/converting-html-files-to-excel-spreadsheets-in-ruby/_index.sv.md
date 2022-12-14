---
title: Konvertera HTML-filer till Excel-kalkylblad i Ruby
type: docs
weight: 40
url: /sv/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells - Konvertera HTML-filer till Excel-kalkylblad**
För att konvertera HTML till kalkylblad med Aspose.Cells för Java i Ruby, anropa helt enkelt html_till_excel()-metoden för omvandlarmodulen.

**Ruby kod**

{{< highlight "ruby" >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Konvertera HTML-filer till Excel-kalkylblad (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
