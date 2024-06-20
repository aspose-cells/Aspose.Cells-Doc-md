---
title: نسخ ونقل أوراق العمل في روبي
type: docs
weight: 10
url: /ar/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - نسخ ونقل أوراق العمل**
### **نسخ أوراق العمل داخل دفتر عمل**
لنسخ ورقة العمل باستخدام **Aspose.Cells for Java في روبي**، اتصل بطريقة **copy_worksheet** في وحدة **copyworksheets**. فيما يلي مثال على الكود.

**كود Ruby**

{{< highlight ruby >}}

 def copy_worksheet(workbook)

    # Create a Worksheets object with reference to the sheets of the Workbook.

    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.

    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."

end 

{{< /highlight >}}
### **نقل ورقات العمل داخل كتاب عمل**
لنقل ورقة العمل باستخدام **Aspose.Cells for Java في روبي**، اتصل بطريقة **move_worksheet** في وحدة **copyworksheets**. فيما يلي مثال على الكود.

**كود Ruby**

{{< highlight ruby >}}

 def move_worksheet(workbook)

    # Get the first worksheet in the book.

    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.

    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."

end 

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **نسخ ونقل أوراق العمل (Aspose.Cells)** من أي مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
