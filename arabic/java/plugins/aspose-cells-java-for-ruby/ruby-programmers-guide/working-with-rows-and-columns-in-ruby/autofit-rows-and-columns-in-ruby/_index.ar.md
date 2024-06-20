---
title: ضبط تناسب الصفوف والأعمدة في Ruby
type: docs
weight: 20
url: /ar/java/autofit-rows-and-columns-in-ruby/
---

## **Aspose.Cells - تناسب الصفوف والأعمدة**
### **تناسب تلقائي للصف**
أبسط نهج لتغيير حجم العرض والارتفاع للصف هو استدعاء طريقة autoFitRow من فئة Worksheet. تأخذ طريقة autoFitRow مؤشر الصف (الذي سيتم تغيير حجمه) كمعلمة.

**كود Ruby**

{{< highlight ruby >}}

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
### **تكبير العرض تلقائيًا**
أسهل طريقة لتغيير حجم العرض والارتفاع للعمود هي استدعاء طريقة autoFitColumn من فئة Worksheet. تأخذ طريقة autoFitColumn الفهرس العمود (الذي سيتم تغيير حجمه) كمعلمة.

**كود Ruby**

{{< highlight ruby >}}

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
## **تحميل رمز التشغيل**
تحميل ** تكبير الصفوف والأعمدة (Aspose.Cells) ** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
