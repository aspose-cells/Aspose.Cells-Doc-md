---
title: Konvertering av kalkylblad till bild i Ruby
type: docs
weight: 60
url: /sv/java/converting-worksheet-to-image-in-ruby/
---

## **Aspose.Cells - Konvertering av kalkylblad till bild**
För att konvertera kalkylblad till bild med Aspose.Cells for Java i Ruby, helt enkelt anropa Converter modulen.

**Ruby-kod**

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
## **Ladda ned körbar kod**
Ladda ned **Konvertera kalkylblad till bild (Aspose.Cells)** från någon av nedanstående sociala kodningssajter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
