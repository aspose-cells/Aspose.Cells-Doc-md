---
title: Convertir hoja de trabajo a imagen en Ruby
type: docs
weight: 60
url: /es/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Conversión de hoja de trabajo en imagen**
Para convertir una hoja de trabajo en una imagen usando Aspose.Cells for Java en Ruby, simplemente invoque el módulo Converter.

**código rubí**

{{< highlight "ruby" >}}

 hoja de trabajo de definición_a_imagen (libro de trabajo)

#Crear un objeto para ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').nuevo



# Establecer el tipo de imagen

formato_imagen = Rjb::import('com.aspose.cells.ImageFormat')

imagen_opciones.setImageFormat(imagen_formato.getPng())



# Obtenga la primera hoja de trabajo.

hoja = libro de trabajo.getWorksheets().get(0)

# Crear un objeto SheetRender para la hoja de destino

sr = Rjb::import('com.aspose.cells.SheetRender').new(hoja, img_options)



j = 0

 mientras j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Conversión de hoja de trabajo en imagen (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
