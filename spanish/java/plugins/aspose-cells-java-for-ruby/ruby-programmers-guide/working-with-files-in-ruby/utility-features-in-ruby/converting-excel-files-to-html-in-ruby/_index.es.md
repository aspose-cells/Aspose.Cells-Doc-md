---
title: Convertir archivos de Excel a HTML en Ruby
type: docs
weight: 20
url: /es/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Conversión de archivos de Excel a HTML**
Para convertir Excel a HTML usando Aspose.Cells for Java en Ruby, simplemente invoque la hoja de trabajo_a_método html() del módulo Converter.

**código rubí**

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
## **Descargar código de ejecución**
Descargar**Conversión de archivos de Excel a HTML (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
