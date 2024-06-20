---
title: Convertir hoja de trabajo a imagen en Ruby
type: docs
weight: 60
url: /es/java/converting-worksheet-to-image-in-ruby/
---

## **Aspose.Cells - Convertir hoja de trabajo a imagen**
Para convertir una hoja de trabajo a imagen usando Aspose.Cells for Java en Ruby, simplemente invoque el módulo Converter.

**Código Ruby**

{{< highlight ruby >}}

 def worksheet_to_image(workbook)

    #Create an object for ImageOptions

    img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



    # Set the image type

    image_format = Rjb::import('com.aspose.cells.ImageFormat')

    img_options.setImageFormat(image_format.getPng())



    # Get the first worksheet.

    sheet = workbook.getWorksheets().get(0)

    # Create a SheetRender object for the target sheet

    sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)



    j = 0

    while j < sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir hoja de trabajo a imagen (Aspose.Cells)** desde alguno de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
