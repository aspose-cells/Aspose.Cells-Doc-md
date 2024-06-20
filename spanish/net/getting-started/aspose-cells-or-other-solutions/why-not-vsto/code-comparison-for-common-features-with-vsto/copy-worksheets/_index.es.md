---
title: Copiar Hojas de Cálculo
type: docs
weight: 60
url: /es/net/copy-worksheets/
---

## **Consejo de Migración:**
\1. Crear objeto Workbook y obtener hoja de cálculo.
\2. Insertar texto en la hoja de cálculo.
\3. Crear nueva hoja de cálculo y copiarla en la hoja de cálculo previamente creada.
### **VSTO**
Error al renderizar macro 'code': valor no válido especificado para el parámetro lang
### **Aspose.Cells**
{{< highlight csharp >}}

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
