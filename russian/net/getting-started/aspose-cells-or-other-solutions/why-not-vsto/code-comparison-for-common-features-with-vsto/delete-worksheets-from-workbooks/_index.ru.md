---
title: Удалить Листы из Книги
type: docs
weight: 100
url: /ru/net/delete-worksheets-from-workbooks/
---

Вы можете удалить любой лист в книге. Чтобы удалить лист, используйте элемент-владелец листа или получите доступ к листу, используя коллекцию листов книги.
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
## **Загрузка**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
