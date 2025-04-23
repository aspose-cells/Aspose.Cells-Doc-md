---
title: Agregar marca de agua WordArt a un gráfico en Aspose.Cells
type: docs
weight: 10
url: /es/net/add-wordart-watermark-to-chart-in-aspose-cells/
---

{{% alert color="primary" %}} 

Puede usar WordArt para agregar efectos de texto especiales a las hojas de cálculo. Por ejemplo, estirar un título, decorar texto, ajustar texto a una forma predefinida o aplicar el texto afectado al área de trama de un gráfico como marca de agua. El WordArt se convierte en un objeto que puede mover o posicionar en sus hojas de cálculo para agregar decoración.

{{% /alert %}} 

El siguiente ejemplo muestra cómo agregar una forma WordArt como marca de agua a un área de trama de gráfico existente. El ejemplo utiliza un archivo de Excel de plantilla que ya contiene el gráfico.

**El archivo de entrada** 

![todo:image_alt_text](picture1.png)

**El archivo de salida**

![todo:image_alt_text](picture2.png)

**C#**

{{< highlight csharp >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";

//Open the existing excel file.

Workbook workbook = new Workbook(FileName);

//Get the chart in the first worksheet.

Aspose.Cells.Charts.Chart chart = workbook.Worksheets[0].Charts[0];

//Add a WordArt watermark (shape) to the chart's plot area.

Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,

"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

//Get the shape's fill format.

Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the transparency.

wordArtFormat.Transparency = 0.9;

//Get the line format and make it invisible.

Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the excel file.

workbook.Save(FileName);

{{< /highlight >}}

## **Descargar Código de Ejemplo**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)

## **Descargar Ejemplo en Ejecución**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
