---
title: احتواء تلقائي للصفوف والأعمدة في روبي
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns-in-ruby/
---
## **Aspose.Cells - احتواء تلقائي للصفوف والأعمدة**
### **صف احتواء تلقائي**
الطريقة الأكثر مباشرة لتغيير حجم عرض الصف وارتفاعه تلقائيًا هي استدعاء طريقة autoFitRow لفئة ورقة العمل. تأخذ طريقة autoFitRow فهرس صف (للصف المراد تغيير حجمه) كمعامل.

**كود روبي**

{{< highlight "ruby" >}}

 def autofit_row()

        data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



        # Instantiating a Workbook object by excel file path

        workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheet = workbook.getWorksheets().get(0)

        # Auto-fitting the 3rd row of the worksheet

        worksheet.autoFitRow(2)

        # Auto-fitting the 3rd row of the worksheet based on the contents in a range of

        # cells (from 1st to 9th column) within the row

        #worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(data_dir + "Autofit Row.xls")

        puts "Autofit Row Successfully."

    end

{{< /highlight >}}
### **عمود الاحتواء التلقائي**
أسهل طريقة لتغيير حجم عرض العمود وارتفاعه تلقائيًا هي استدعاء طريقة autoFitColumn لفئة ورقة العمل. تأخذ طريقة autoFitColumn فهرس العمود (الخاص بالعمود على وشك تغيير حجمه) كمعامل.

**كود روبي**

{{< highlight "ruby" >}}

 def autofit_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Auto-fitting the 4th column of the worksheet

    worksheet.autoFitColumn(3)

    # Auto-fitting the 4th column of the worksheet based on the contents in a range of

    # cells (from 1st to 9th row) within the column

    #worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Autofit Column.xls")

    puts "Autofit Column Successfully."

end

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**احتواء تلقائي للصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
