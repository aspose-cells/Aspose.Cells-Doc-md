---
title: Konvertieren von Arbeitsblättern in Bilder in Ruby
type: docs
weight: 60
url: /de/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells – Arbeitsblatt in Bild konvertieren**
Um Worksheet in Image mit Aspose.Cells for Java in Ruby zu konvertieren, rufen Sie einfach das Converter-Modul auf.

**Ruby-Code**

{{< highlight "ruby" >}}

 def Arbeitsblatt_zu_Bild (Arbeitsmappe)

#Erstellen Sie ein Objekt für ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# Legen Sie den Bildtyp fest

image_format = Rjb::import('com.aspose.cells.ImageFormat')

Bild_options.setImageFormat(Bild_format.getPng())



# Holen Sie sich das erste Arbeitsblatt.

Blatt = Arbeitsmappe.getWorksheets().get(0)

# Erstellen Sie ein SheetRender-Objekt für das Zielblatt

sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)



j = 0

 während j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Arbeitsblatt in Bild konvertieren (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
