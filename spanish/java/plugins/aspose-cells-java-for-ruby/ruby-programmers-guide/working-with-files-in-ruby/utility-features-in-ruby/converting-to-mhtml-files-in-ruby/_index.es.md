---
title: Conversión a archivos MHTML en Ruby
type: docs
weight: 50
url: /es/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Conversión a archivos MHTML**
Para convertir la hoja de trabajo al archivo MHTML usando Aspose.Cells for Java en Ruby, simplemente invoque la hoja de trabajo_a_Método mhtml() del módulo Converter.

**código rubí**

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
## **Descargar código de ejecución**
Descargar**Conversión a archivos MHTML (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
