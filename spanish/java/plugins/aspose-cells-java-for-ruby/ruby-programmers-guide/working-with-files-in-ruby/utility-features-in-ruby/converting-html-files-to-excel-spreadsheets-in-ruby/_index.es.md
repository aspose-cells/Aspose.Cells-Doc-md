---
title: Convertir archivos HTML en hojas de cálculo de Excel en Ruby
type: docs
weight: 40
url: /es/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - Convertir archivos HTML en hojas de cálculo de Excel**
Para convertir HTML a hoja de cálculo usando Aspose.Cells for Java en Ruby, simplemente invoque el método html_to_excel() del módulo del Convertidor.

**Código Ruby**

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
## **Descargar Código en Ejecución**
Descargar **Convertir archivos HTML a Hojas de cálculo de Excel (Aspose.Cells)** desde alguno de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
