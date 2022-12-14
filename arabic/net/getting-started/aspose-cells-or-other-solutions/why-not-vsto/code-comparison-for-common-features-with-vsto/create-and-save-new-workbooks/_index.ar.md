---
title: إنشاء وحفظ مصنفات جديدة
type: docs
weight: 70
url: /ar/net/create-and-save-new-workbooks/
---
## **نصائح الهجرة:**
\ 1. إنشاء كائن المصنف
\ 2. احصل على ورقة العمل الحالية.
\ 3. أدخل بعض النص في أي خلية.
\ 4. احفظ المصنف.
### **VSTO**
فيما يلي مثال على رمز VSTO

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
يوجد أدناه مثال رمز لـ Aspose.Cells

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **تحميل**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
