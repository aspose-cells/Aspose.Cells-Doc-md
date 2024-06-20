---
title: إنشاء وحفظ سجلات عمل جديدة
type: docs
weight: 70
url: /ar/net/create-and-save-new-workbooks/
---

## **تلميحات الهجرة:**
\1. إنشاء كائن سجل عمل
\2. الحصول على ورقة عمل حالية.
\3. إدراج نص ما في أي خلية.
\4. حفظ سجل العمل.
### **VSTO**
أدناه مثال على الرمز لـ VSTO

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
أدناه مثال على الرمز لـ Aspose.Cells

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **تحميل**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
