---
title: Conversione in file MHTML in Ruby
type: docs
weight: 50
url: /it/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Conversione in file MHTML**
Per convertire il foglio di lavoro in un file MHTML utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il foglio di lavoro_a_mhtml() del modulo Converter.

**Codice Rubino**

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
## **Scarica il codice in esecuzione**
Scarica**Conversione in file MHTML (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
