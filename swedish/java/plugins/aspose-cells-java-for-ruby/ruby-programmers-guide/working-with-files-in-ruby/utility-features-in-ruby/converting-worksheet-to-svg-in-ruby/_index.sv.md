---
title: Konvertera arbetsblad till SVG i Ruby
type: docs
weight: 70
url: /sv/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Konvertera arbetsblad till SVG**
För att konvertera kalkylblad till SVG med Aspose.Cells for Java i Ruby, anropa kalkylblad_till_svg()-metoden för omvandlarmodulen.

**Ruby kod**

{{< highlight "ruby" >}}

 def arbetsblad_till_svg(arbetsbok)

# Konvertera varje kalkylblad till svg-format på en enda sida.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

img_options.setSaveFormat(spara_format.SVG)

img_options.setOnePagePerSheet(true)



# Konvertera varje kalkylblad till svg-format

sheet_count = workbook.getWorksheets().getCount()

i=0

 medan jag< sheet_count

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
## **Ladda ner Running Code**
Ladda ner**Konvertera arbetsblad till SVG (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
