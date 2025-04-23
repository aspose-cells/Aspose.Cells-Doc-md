---
title: نسخ أوراق العمل
type: docs
weight: 60
url: /ar/net/copy-worksheets/
---

## **نصيحة الهجرة:**
\1.  إنشاء كائن الورقة العمل والحصول على ورقة العمل.
\2.  إدراج نص في ورقة العمل.
\3.  إنشاء ورقة العمل الجديدة ونسخها إلى الورقة السابقة قبل إتمام ورقة العمل.
### **VSTO**
خطا في المقاطعة 'الكود' : قيمة غير صالحة محددة لمعامل اللغة
### **Aspose.Cells**
{{< highlight csharp >}}

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
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
