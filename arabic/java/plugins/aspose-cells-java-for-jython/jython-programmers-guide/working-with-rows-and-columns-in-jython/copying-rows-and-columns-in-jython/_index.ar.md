---
title: نسخ الصفوف والأعمدة في جايثون
type: docs
weight: 30
url: /ar/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - نسخ الصفوف والأعمدة**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 من إعدادات استيراد الخلايا غير المقصودة

من com.aspose.cells import Workbook

فئة RowsAndColumns:

 def__فيه__(الذات):



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns / RowsAndColumns'



 # نسخ الصفوف

 self.copy_rows ()

 # نسخ الأعمدة

 self.copy_columns ()



 def copy_rows (dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns / RowsAndColumns /'

 # إنشاء كائن مصنف من خلال مسار ملف Excel

 المصنف = المصنف (dataDir + 'Book1.xls')

 الوصول إلى ورقة العمل الأولى في ملف Excel

 ورقة العمل = workbook.getWorksheets (). get (0)

 # انسخ الصف الثاني بالبيانات والتنسيقات والصور والكائنات الرسومية

 # إلى الصف الثاني عشر في ورقة العمل.

 workheet.getCells (). copyRow (workheet.getCells ()، 1،11)

 # حفظ ملف Excel المعدل في تنسيق افتراضي (أي Excel 2003)

 workbook.save (dataDir + "Copy Rows.xls")

 طباعة "نسخ الصفوف بنجاح."



 def copy_columns (dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns / RowsAndColumns /'

 # إنشاء كائن مصنف من خلال مسار ملف Excel

 المصنف = المصنف ()

 الوصول إلى ورقة العمل الأولى في ملف Excel

 ورقة العمل = workbook.getWorksheets (). get (0)

 # ضع بعض البيانات في صفوف الرأس (A1: A4)

 أنا = 0

 عندما أنا< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
