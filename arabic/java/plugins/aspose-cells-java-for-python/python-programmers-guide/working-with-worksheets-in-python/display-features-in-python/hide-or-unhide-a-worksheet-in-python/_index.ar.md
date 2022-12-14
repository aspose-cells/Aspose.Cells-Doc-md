---
title: إخفاء أو إظهار ورقة عمل في Python
type: docs
weight: 50
url: /ar/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - إخفاء أو إظهار ورقة عمل**
### **إخفاء ورقة العمل**
 لإخفاء ورقة العمل باستخدام Aspose.Cells Java لروبي ، اتصل**ورقة عمل** وحدة.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **عرض ورقة عمل**
يمكن للمطورين جعل ورقة العمل مرئية عن طريق تعيين*setVisible (* *حقيقي* *)*طريقة**ورقة عمل**صف دراسي.

**Python كود**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إخفاء أو إظهار ورقة عمل (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
