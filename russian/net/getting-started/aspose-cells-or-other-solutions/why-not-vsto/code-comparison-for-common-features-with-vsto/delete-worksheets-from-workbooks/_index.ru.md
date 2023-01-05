---
title: Удалить рабочие листы из рабочих книг
type: docs
weight: 100
url: /ru/net/delete-worksheets-from-workbooks/
---
Вы можете удалить любой рабочий лист в книге. Чтобы удалить рабочий лист, используйте ведущий элемент рабочего листа или получите доступ к рабочему листу с помощью коллекции листов рабочей книги.
## **ВСТО**
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
## **Скачать**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
