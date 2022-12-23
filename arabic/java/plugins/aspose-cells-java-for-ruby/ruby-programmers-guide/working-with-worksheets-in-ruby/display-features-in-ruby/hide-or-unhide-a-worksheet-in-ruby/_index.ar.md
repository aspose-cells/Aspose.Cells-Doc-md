---
title: إخفاء أو إظهار ورقة عمل في روبي
type: docs
weight: 60
url: /ar/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - إخفاء أو إظهار ورقة عمل**
### **إخفاء ورقة العمل**
 لإخفاء ورقة العمل باستخدام Aspose.Cells Java لروبي ، اتصل**ورقة عمل** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **عرض ورقة عمل**
يمكن للمطورين جعل ورقة العمل مرئية عن طريق تعيين*setVisible (* *حقيقي* *)*طريقة**ورقة عمل**صف دراسي.

**كود روبي**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**إخفاء أو إظهار ورقة عمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
