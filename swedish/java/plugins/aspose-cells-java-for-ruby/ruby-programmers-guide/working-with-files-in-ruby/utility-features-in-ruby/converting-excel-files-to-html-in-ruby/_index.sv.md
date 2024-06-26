---
title: Konvertera Excel filer till HTML i Ruby
type: docs
weight: 20
url: /sv/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Konvertera Excel-filer till HTML**
För att konvertera Excel till HTML med hjälp av Aspose.Cells for Java i Ruby, helt enkelt anropa worksheet_to_html() metoden i Converter modulen.

**Ruby-kod**

{{< highlight ruby >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Konvertera Excel-filer till HTML (Aspose.Cells)** från någon av de sociala kodningssidorna som nämns nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
