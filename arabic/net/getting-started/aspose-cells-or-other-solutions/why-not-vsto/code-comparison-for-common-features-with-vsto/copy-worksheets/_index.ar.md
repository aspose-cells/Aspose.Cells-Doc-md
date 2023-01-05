---
title: نسخ أوراق العمل
type: docs
weight: 60
url: /ar/net/copy-worksheets/
---
## **نصيحة الهجرة:**
\ 1. إنشاء كائن المصنف والحصول على ورقة العمل.
\ 2. أدخل نصًا في ورقة العمل.
\ 3. قم بإنشاء ورقة عمل جديدة وانسخها إلى ورقة عمل سابقة الصنع.
### **VSTO**
خطأ في عرض الماكرو 'code': تم تحديد قيمة غير صالحة للمعامل lang
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **تحميل**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
