---
title: إخفاء وإظهار الصفوف والأعمدة في روبي
type: docs
weight: 50
url: /ar/java/hiding-and-showing-rows-and-columns-in-ruby/
---

## **Aspose.Cells - التحكم في رؤية الصفوف والأعمدة**
### **إخفاء الصفوف والأعمدة**
يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق HideRow و HideColumn لمجموعة Cells على التوالي. تأخذ كلا الطريقتين فهرس الصف/العمود كمعلمة لإخفاء الصف أو العمود المعين.

**كود Ruby**

{{< highlight ruby >}}

 def hide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Hiding the 3rd row of the worksheet

    cells.hideRow(2)

    # Hiding the 2nd column of the worksheet

    cells.hideColumn(1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Hide Rows And Columns.xls")

    puts "Hide Rows And Columns Successfully."

end

{{< /highlight >}}
### **عرض الصفوف والأعمدة**
يمكن للمطورين إظهار أي صف أو عمود مخفي عن طريق استدعاء طرق UnhideRow و UnhideColumn لمجموعة Cells على التوالي. تأخذ كلا الطريقتين معلمين:

- **فهرس الصف أو العمود** - فهرس صف أو عمود يُستخدم لإظهار الصف أو العمود المعين.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين بعد إظهاره.

**كود Ruby**

{{< highlight ruby >}}

 def unhide_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Unhiding the 3rd row and setting its height to 13.5

    cells.unhideRow(2,13.5)

    # Unhiding the 2nd column and setting its width to 8.5

    cells.unhideColumn(1,8.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unhide Rows And Columns.xls")

    puts "Unhide Rows And Columns Successfully."

end

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **التحكم في رؤية الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
