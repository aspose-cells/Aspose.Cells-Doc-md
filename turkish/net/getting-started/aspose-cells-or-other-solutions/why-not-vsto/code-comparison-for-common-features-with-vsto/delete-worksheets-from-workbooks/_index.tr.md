---
title: Çalışma Kitaplarından Çalışsayfalarını Sil
type: docs
weight: 100
url: /tr/net/delete-worksheets-from-workbooks/
---

Bir çalışma kitabında herhangi bir çalışsayfayı silebilirsiniz. Bir çalışsayfayı silmek için, çalışsayfa ana öğesini kullanın veya çalışma kitabının çalışsayfalar koleksiyonunu kullanarak çalışsayfaya erişin.
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
## **İndir**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
