---
title: Establecer Fórmula Compartida en Aspose.Cells
type: docs
weight: 110
url: /es/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Supongamos que tienes una hoja de cálculo llena de datos.

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

{{% /alert %}} 

Aspose.Cells te permite especificar una fórmula usando la propiedad Cell.Formula.

Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O haz lo que hiciste para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de la celda en consecuencia (A3*0.09, A4*0.09, A5*0.09 y así sucesivamente). Esto requiere que se actualicen las referencias de celda para cada fila. También requiere que Aspose.Cells analice cada fórmula individualmente, lo que puede ser consumidor de tiempo para hojas de cálculo grandes y fórmulas complejas. También agrega líneas de código adicionales, aunque los bucles pueden reducirlas en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método Cell.SetSharedFormula es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Descargar Ejemplo en Ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
