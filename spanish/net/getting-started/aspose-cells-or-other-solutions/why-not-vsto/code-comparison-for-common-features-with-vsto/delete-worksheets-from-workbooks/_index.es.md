---
title: Eliminar hojas de trabajo de libros de trabajo
type: docs
weight: 100
url: /es/net/delete-worksheets-from-workbooks/
---
Puede eliminar cualquier hoja de trabajo en un libro de trabajo. Para eliminar una hoja de trabajo, use el elemento host de la hoja de trabajo o acceda a la hoja de trabajo usando la colección de hojas del libro de trabajo.
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
## **Descargar**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
