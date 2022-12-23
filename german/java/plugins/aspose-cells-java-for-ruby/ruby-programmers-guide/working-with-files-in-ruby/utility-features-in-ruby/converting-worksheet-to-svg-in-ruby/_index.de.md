---
title: Konvertieren des Arbeitsblatts in SVG in Ruby
type: docs
weight: 70
url: /de/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Konvertieren des Arbeitsblatts in SVG**
Um Worksheet in SVG mit Aspose.Cells for Java in Ruby zu konvertieren, rufen Sie einfach worksheet auf_zu_svg()-Methode des Converter-Moduls.

**Ruby-Code**

{{< highlight "ruby" >}}

 def Arbeitsblatt_zu_svg (Arbeitsmappe)

# Konvertieren Sie jedes Arbeitsblatt auf einer einzigen Seite in das SVG-Format.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

Bild_options.setSaveFormat(speichern_format.SVG)

img_options.setOnePagePerSheet(true)



# Konvertieren Sie jedes Arbeitsblatt in das SVG-Format

sheet_count = arbeitsmappe.getWorksheets().getCount()

ich=0

 während ich< sheet_count

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
## **Laufcode herunterladen**
Download**Konvertieren des Arbeitsblatts in SVG (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
