---
title: حذف الصفحات العمل من الكتب
type: docs
weight: 100
url: /ar/net/delete-worksheets-from-workbooks/
---

يمكنك حذف أي ورقة عمل في كتاب العمل. لحذف ورقة عمل، استخدم عنصر المضيف للورقة العمل أو ادخل إلى الورقة العمل باستخدام مجموعة الصفحات لكتاب العمل.
## **VSTO**
{{< highlight csharp >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **تحميل**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
