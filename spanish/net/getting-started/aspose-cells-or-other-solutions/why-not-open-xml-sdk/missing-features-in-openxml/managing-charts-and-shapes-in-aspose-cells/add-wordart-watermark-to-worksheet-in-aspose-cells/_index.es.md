---
title: Agregar marca de agua WordArt a una hoja de cálculo en Aspose.Cells
type: docs
weight: 20
url: /es/net/add-wordart-watermark-to-worksheet-in-aspose-cells/
---

{{% alert color="primary" %}}

Utilice WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estire un título en la parte superior del archivo, decore texto y ajuste texto a una forma predefinida, o aplique texto a una hoja de Excel como marca de agua de fondo. El WordArt se convierte en un objeto que puede mover o posicionar en las hojas de cálculo para agregar decoración.

{{% /alert %}}

El siguiente ejemplo muestra cómo agregar una forma WordArt para establecer una marca de agua de fondo para una hoja de cálculo.

Después de ejecutar el código, el archivo de salida contiene una marca de agua WordArt de color rojo pálido.

**El archivo de salida** 

![todo:image_alt_text](picture1.png)

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Add WordArt Watermark to Worksheet.xlsx";

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.Worksheets[0];

//Add Watermark

Aspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the fill format of the word art

MsoFillFormat wordArtFormat = wordart.FillFormat;

//Set the color

wordArtFormat.ForeColor = System.Drawing.Color.Red;

//Set the transparency

wordArtFormat.Transparency = 0.9;

//Make the line invisible

MsoLineFormat lineFormat = wordart.LineFormat;

lineFormat.IsVisible = false;

//Save the file

workbook.Save(FileName);

{{< /highlight >}}

## **Descargar Código de Ejemplo**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark)

## **Descargar Ejemplo en Ejecución**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
