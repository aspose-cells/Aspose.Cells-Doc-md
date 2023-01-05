---
title: Agregar marca de agua de Word Art a la hoja de trabajo usando Aspose.Cells
type: docs
weight: 10
url: /es/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---
## **Aspose.Cells - Agregar marca de agua de Word Art a la hoja de trabajo**
Use WordArt para agregar efectos de texto especiales a las hojas de cálculo. Por ejemplo, estire un título en la parte superior del archivo, decore el texto y haga que el texto se ajuste a una forma preestablecida, o aplique texto a una hoja de Excel como una marca de agua de fondo. El WordArt se convierte en un objeto que puede mover o colocar en hojas de cálculo para agregar decoración.

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook();

//Get the first default sheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add Watermark

Shape wordart = sheet.getShapes().addTextEffect(MsoPresetTextEffect.TEXT_EFFECT_1,

"CONFIDENTIAL", "Arial Black", 50, false, true

, 18, 8, 1, 1, 130, 800);

//Get the shape's fill format

FillFormat wordArtFormat = wordart.getFill();

//Set the transparency

wordArtFormat.setTransparency(0.9);

//Make the line invisible

wordart.setHasLine(false);

//Save the file

workbook.save(dataDir + "AsposeWatermark_Out.xls");

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Agregar marca de agua de WordArt a la hoja de trabajo](/cells/es/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
