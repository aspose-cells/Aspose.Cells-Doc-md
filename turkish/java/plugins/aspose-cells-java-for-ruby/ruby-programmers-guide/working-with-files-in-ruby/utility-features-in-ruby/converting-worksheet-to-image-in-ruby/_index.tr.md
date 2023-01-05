---
title: Çalışma Sayfasını Ruby'de Görüntüye Dönüştürme
type: docs
weight: 60
url: /tr/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Çalışma Sayfasını Resme Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Çalışma Sayfasını Görüntüye dönüştürmek için Dönüştürücü modülünü çağırmanız yeterlidir.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def çalışma sayfası_ile_resim(çalışma kitabı)

#ImageOptions için bir nesne oluştur

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# Görüntü türünü ayarlayın

image_format = Rjb::import('com.aspose.cells.ImageFormat')

img_options.setImageFormat(resim_format.getPng())



# İlk çalışma sayfasını alın.

sayfa = workbook.getWorksheets().get(0)

# Hedef sayfa için bir SheetRender nesnesi oluşturun

sr = Rjb::import('com.aspose.cells.SheetRender').new(sayfa, img_options)



j = 0

 j iken< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Çalışma Sayfasını Resme Dönüştürme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
