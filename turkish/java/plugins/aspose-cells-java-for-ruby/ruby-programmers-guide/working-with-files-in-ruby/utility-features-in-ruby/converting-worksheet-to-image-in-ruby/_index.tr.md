---
title: Ruby de Çalışma Sayfasını Resme Dönüştürme
type: docs
weight: 60
url: /tr/java/converting-worksheet-to-image-in-ruby/
---

## **Aspose.Cells - Çalışma Sayfasını Görüntüye Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Çalışma Sayfasını Görüntüye dönüştürmek için, Converter modülünü basitçe çağırın.

**Ruby Kodu**

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
## **Çalışan Kodu İndir**
aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Çalışma Sayfasını Görüntüye Dönüştürme (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
