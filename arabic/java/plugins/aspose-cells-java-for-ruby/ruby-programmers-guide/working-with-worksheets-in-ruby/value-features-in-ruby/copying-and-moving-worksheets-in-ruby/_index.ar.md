---
title: نسخ وتحريك أوراق العمل في روبي
type: docs
weight: 10
url: /ar/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - نسخ أوراق العمل ونقلها**
### **نسخ أوراق العمل داخل مصنف**
 لنسخ ورقة العمل باستخدام**Aspose.Cells for Java في روبي** ، مكالمة**نسخة_ورقة عمل** طريقة**أوراق العمل** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود روبي**

{{< highlight "ruby" >}}

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
### **انقل أوراق العمل داخل مصنف**
 لنقل ورقة العمل باستخدام**Aspose.Cells for Java في روبي** ، مكالمة**نقل ورقة العمل** طريقة**أوراق العمل** وحدة. أدناه يمكنك مشاهدة مثال رمز.

**كود روبي**

{{< highlight "ruby" >}}

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
## **قم بتنزيل كود التشغيل**
تحميل**نسخ أوراق العمل ونقلها (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
