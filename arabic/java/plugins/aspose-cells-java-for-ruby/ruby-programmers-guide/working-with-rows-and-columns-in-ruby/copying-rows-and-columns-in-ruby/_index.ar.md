---
title: نسخ الصفوف والأعمدة في روبي
type: docs
weight: 30
url: /ar/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - نسخ الصفوف والأعمدة**
### **نسخ الصفوف**
يوفر Aspose.Cells طريقة copyRow لفئة Cells. تنسخ هذه الطريقة جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الرسومية الأخرى من صف المصدر إلى صف الوجهة.

تأخذ طريقة copyRow المعلمات التالية:

- الكائن المصدر Cells ،
- فهرس صف المصدر و
- فهرس صف الوجهة.

**كود روبي**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **نسخ الأعمدة**
يوفر Aspose.Cells طريقة copyColumn لفئة Cells ، وتقوم هذه الطريقة بنسخ جميع أنواع البيانات ، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور وكائنات الرسم الأخرى من العمود المصدر إلى العمود الوجهة.

تأخذ طريقة copyColumn المعلمات التالية:

- الكائن المصدر Cells ،
- فهرس عمود المصدر و
- فهرس عمود الوجهة.

**كود روبي**

{{< highlight "ruby" >}}

 def copy_columns ()

بيانات_dir = File.dirname (File.dirname (File.dirname (__ملف__))) + '/ بيانات /'



# إنشاء كائن مصنف من خلال مسار ملف Excel

المصنف = Rjb :: import ('com.aspose.cells.Workbook'). new

# الوصول إلى ورقة العمل الأولى في ملف Excel

ورقة العمل = workbook.getWorksheets (). get (0)

# ضع بعض البيانات في صفوف الرأس (A1: A4)

أنا = 0

 عندما أنا< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**نسخ الصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
