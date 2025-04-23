---
title: Eliminar Hojas de Cálculo de Libros
type: docs
weight: 100
url: /es/net/delete-worksheets-from-workbooks/
---

Puedes eliminar cualquier hoja de cálculo en un libro. Para eliminar una hoja de cálculo, usa el elemento host de la hoja de trabajo o accede a la hoja de cálculo mediante la colección de hojas del libro.
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
## **Descargar**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
