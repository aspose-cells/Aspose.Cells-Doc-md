---
title: تجميع وإلغاء تجميع الصفوف والأعمدة في الروبي
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns-in-ruby/
---

## **Aspose.Cells - إدارة تجميع الصفوف والأعمدة**
### **تجميع الصفوف والأعمدة**
يمكن تجميع الصفوف أو الأعمدة عن طريق استدعاء أساليب groupRows و groupColumns في مجموعة Cells. تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

**كود Ruby**

{{< highlight ruby >}}

 def group_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true

    cells.groupRows(0,5,true)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true

    cells.groupColumns(0,2,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Group Rows And Columns.xls")

    puts "Group Rows And Columns Successfully."

end  

{{< /highlight >}}
### **إلغاء تجميع الصفوف والأعمدة**
إلغاء تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء أساليب UngroupRows و UngroupColumns لمجموعة Cells. تأخذ كلا الطريقتين نفس المعلمات:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

**كود Ruby**

{{< highlight ruby >}}

 def ungroup_rows_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Group Rows And Columns.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Ungrouping first six rows (from 0 to 5)

    cells.ungroupRows(0,5)

    # Ungrouping first three columns (from 0 to 2)

    cells.ungroupColumns(0,2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Ungroup Rows And Columns.xls")

    puts "Ungroup Rows And Columns Successfully."

end

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **تجميع وفك تجميع الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
