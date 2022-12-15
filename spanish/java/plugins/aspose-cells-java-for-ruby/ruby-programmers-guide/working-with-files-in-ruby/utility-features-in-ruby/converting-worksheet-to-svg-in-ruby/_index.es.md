---
title: Convertir hoja de trabajo a SVG en Ruby
type: docs
weight: 70
url: /es/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Conversión de hoja de trabajo a SVG**
Para convertir la hoja de trabajo a SVG usando Aspose.Cells for Java en Ruby, simplemente invoque la hoja de trabajo_a_Método svg() del módulo Converter.

**código rubí**

{{< highlight "ruby" >}}

 hoja de trabajo de definición_a_svg (libro de trabajo)

# Convierta cada hoja de trabajo en formato svg en una sola página.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').nuevo

save_format = Rjb::import('com.aspose.cells.SaveFormat')

imagen_opciones.setSaveFormat(guardar_formato.SVG)

img_options.setOnePagePerSheet(verdadero)



# Convierta cada hoja de trabajo en formato svg

sheet_count = libro de trabajo.getWorksheets().getCount()

yo=0

 mientras yo< sheet_count

        sheet = workbook.getWorksheets().get(i)

        sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)

        k=0

        while sr.getPageCount()

            # Output the worksheet into Svg image format

            sr.toImage(k, @data_dir + sheet.getName() + "#{k}.svg")

        end

    end

    puts "SVG saved successfully."

end 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Conversión de hoja de trabajo a SVG (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
