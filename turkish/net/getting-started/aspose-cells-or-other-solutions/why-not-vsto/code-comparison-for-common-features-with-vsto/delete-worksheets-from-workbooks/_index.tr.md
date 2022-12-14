---
title: Çalışma Kitaplarından Çalışma Sayfalarını Sil
type: docs
weight: 100
url: /tr/net/delete-worksheets-from-workbooks/
---
Bir çalışma kitabındaki herhangi bir çalışma sayfasını silebilirsiniz. Bir çalışma sayfasını silmek için çalışma sayfası ana bilgisayar öğesini kullanın veya çalışma kitabının sayfalar koleksiyonunu kullanarak çalışma sayfasına erişin.
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
## **İndirmek**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
