---
title: Konvertera arbetsblad till bild i Ruby
type: docs
weight: 60
url: /sv/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Konvertera arbetsblad till bild**
För att konvertera kalkylblad till bild med Aspose.Cells för Java i Ruby, anropa omvandlarmodulen.

**Ruby kod**

{{< highlight "ruby" >}}

 def arbetsblad_till_bild (arbetsbok)

#Skapa ett objekt för ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# Ställ in bildtyp

image_format = Rjb::import('com.aspose.cells.ImageFormat')

img_options.setImageFormat(image_format.getPng())



# Skaffa det första arbetsbladet.

ark = workbook.getWorksheets().get(0)

# Skapa ett SheetRender-objekt för målarket

sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)



j = 0

 medan j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Konvertera kalkylblad till bild (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
