---
title: تحويل ورقة العمل إلى صورة في روبي
type: docs
weight: 60
url: /ar/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - تحويل ورقة العمل إلى صورة**
لتحويل ورقة العمل إلى صورة باستخدام Aspose.Cells for Java في Ruby ، ما عليك سوى استدعاء وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 ورقة عمل def_إلى_صورة (مصنف)

#Create an object for ImageOptions

img_options = Rjb :: import ('com.aspose.cells.ImageOrPrintOptions'). جديد



# تعيين نوع الصورة

image_format = Rjb :: import ('com.aspose.cells.ImageFormat')

IMG_options.setImageFormat (صورة_format.getPng ())



# احصل على ورقة العمل الأولى.

sheet = workbook.getWorksheets (). get (0)

# قم بإنشاء كائن SheetRender للورقة المستهدفة

sr = Rjb :: import ('com.aspose.cells.SheetRender'). new (sheet، img_options)



ي = 0

 بينما ي< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**تحويل ورقة العمل إلى صورة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
