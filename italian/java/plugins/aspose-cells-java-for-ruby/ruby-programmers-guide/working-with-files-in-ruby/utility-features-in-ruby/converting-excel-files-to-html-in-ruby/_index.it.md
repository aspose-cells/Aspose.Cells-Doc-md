---
title: Conversione di file Excel in HTML in Ruby
type: docs
weight: 20
url: /it/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Conversione di file Excel in HTML**
Per convertire Excel in HTML utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il foglio di lavoro_a_html() del modulo Converter.

**Codice Rubino**

{{< highlight "ruby" >}}

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
Scaricamento**Conversione di file Excel in HTML (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
