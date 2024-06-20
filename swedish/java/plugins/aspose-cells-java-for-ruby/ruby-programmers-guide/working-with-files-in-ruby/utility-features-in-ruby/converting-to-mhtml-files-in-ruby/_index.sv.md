---
title: Konvertering till MHTML filer i Ruby
type: docs
weight: 50
url: /sv/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - Konvertering till MHTML-filer**
För att konvertera kalkylblad till MHTML-fil med Aspose.Cells for Java i Ruby, helt enkelt anropa worksheet_to_mhtml() metoden i Converter modulen.

**Ruby-kod**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Konvertera till MHTML-filer (Aspose.Cells)** från någon av nedanstående sociala kodningssajter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
