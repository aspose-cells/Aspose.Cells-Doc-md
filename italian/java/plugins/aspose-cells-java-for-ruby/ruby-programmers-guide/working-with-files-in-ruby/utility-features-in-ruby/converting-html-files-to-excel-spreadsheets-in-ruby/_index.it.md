---
title: Conversione di file HTML in fogli Excel in Ruby
type: docs
weight: 40
url: /it/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - Conversione di file HTML in fogli Excel**
Per convertire HTML in foglio di calcolo utilizzando Aspose.Cells for Java in Ruby, basta invocare il metodo html_to_excel() del modulo Converter.

**Codice Ruby**

{{< highlight ruby >}}

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
## **Scarica il codice in esecuzione**
Scarica **Conversione di file HTML in fogli Excel (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
