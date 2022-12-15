---
title: Konvertera till MHTML-filer i Ruby
type: docs
weight: 50
url: /sv/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Konvertering till MHTML-filer**
För att konvertera kalkylblad till MHTML-fil med Aspose.Cells for Java i Ruby, anropa kalkylblad_till_mhtml()-metoden för konverteringsmodulen.

**Ruby kod**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Konvertera till MHTML-filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
