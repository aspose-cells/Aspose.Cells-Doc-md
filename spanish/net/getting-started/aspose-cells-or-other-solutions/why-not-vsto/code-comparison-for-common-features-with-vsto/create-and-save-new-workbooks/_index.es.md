---
title: Crear y guardar nuevos libros de trabajo
type: docs
weight: 70
url: /es/net/create-and-save-new-workbooks/
---
## **Consejos de migración:**
\1. Crear objeto de libro de trabajo
\2. Obtenga la hoja de trabajo actual.
\3. Inserta algún texto en cualquier celda.
\4. Guarde el libro de trabajo.
### **VSTO**
A continuación se muestra un ejemplo de código para VSTO

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
A continuación se muestra un ejemplo de código para Aspose.Cells

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Descargar**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
