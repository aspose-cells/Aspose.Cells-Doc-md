---
title: احذف أوراق العمل من المصنفات
type: docs
weight: 100
url: /ar/net/delete-worksheets-from-workbooks/
---
يمكنك حذف أي ورقة عمل في مصنف. لحذف ورقة عمل ، استخدم عنصر مضيف ورقة العمل أو قم بالوصول إلى ورقة العمل باستخدام مجموعة أوراق المصنف.
## **VSTO**
{{< highlight "csharp" >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **تحميل**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
