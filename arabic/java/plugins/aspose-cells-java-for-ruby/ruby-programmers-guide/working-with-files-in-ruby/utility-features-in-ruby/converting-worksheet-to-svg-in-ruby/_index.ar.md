---
title: تحويل ورقة العمل إلى SVG في روبي
type: docs
weight: 70
url: /ar/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - تحويل ورقة العمل إلى SVG**
لتحويل ورقة العمل إلى SVG باستخدام Aspose.Cells for Java في روبي ، ما عليك سوى استدعاء ورقة العمل_إلى_svg () طريقة وحدة المحول.

**كود روبي**

{{< highlight "ruby" >}}

 ورقة عمل def_إلى_svg (مصنف)

# تحويل كل ورقة عمل إلى تنسيق svg في صفحة واحدة.

img_options = Rjb :: import ('com.aspose.cells.ImageOrPrintOptions'). جديد

save_format = Rjb :: import ('com.aspose.cells.SaveFormat')

IMG_options.setSaveFormat (حفظ_التنسيق. SVG)

img_options.setOnePagePerSheet (صحيح)



# تحويل كل ورقة عمل إلى تنسيق svg

sheet_count = workbook.getWorksheets (). getCount ()

أنا = 0

 عندما أنا< sheet_count

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
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ورقة العمل إلى SVG (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
