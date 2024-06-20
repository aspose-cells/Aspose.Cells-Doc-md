---
title: Convertire file Excel in HTML in Ruby
type: docs
weight: 20
url: /it/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Convertire file Excel in HTML**
Per convertire Excel in HTML usando Aspose.Cells for Java in Ruby, basta invocare il metodo worksheet_to_html() del modulo Converter.

**Codice Ruby**

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
## **Scarica il codice in esecuzione**
Scarica **Convertire file Excel in HTML (Aspose.Cells)** da uno dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
