---
title: Çalışma Sayfasını Ruby'de SVG'ye Dönüştürme
type: docs
weight: 70
url: /tr/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Çalışma Sayfasını SVG'ye Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Çalışma Sayfasını SVG'ye dönüştürmek için çalışma sayfasını çağırmanız yeterlidir_ile_Dönüştürücü modülünün svg() yöntemi.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def çalışma sayfası_ile_svg(çalışma kitabı)

# Her çalışma sayfasını tek bir sayfada svg formatına dönüştürün.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

img_options.setSaveFormat(kaydet_biçim.SVG)

img_options.setOnePagePerSheet(doğru)



# Her çalışma sayfasını svg formatına dönüştürün

sheet_count = workbook.getWorksheets().getCount()

ben=0

 ben iken< sheet_count

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
## **Çalışan Kodu İndir**
İndirmek**Çalışma Sayfasını SVG'ye Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
