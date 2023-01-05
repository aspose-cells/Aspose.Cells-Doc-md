---
title: Copiar hojas de trabajo
type: docs
weight: 60
url: /es/net/copy-worksheets/
---
## **Sugerencia de migración:**
\1. Cree el objeto Libro de trabajo y obtenga la Hoja de trabajo.
\2. Insertar texto en la hoja de trabajo.
\3. Cree una nueva hoja de trabajo y cópiela en la hoja de trabajo anterior antes de hacerla.
### **VSTO**
Error al renderizar macro 'código': valor no válido especificado para el parámetro lang
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Descargar**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
