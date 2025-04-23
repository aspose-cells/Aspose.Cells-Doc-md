---
title: Agregar texto artístico Word a una hoja de cálculo usando Aspose.Cells
type: docs
weight: 10
url: /es/java/add-word-art-watermark-to-worksheet-using-aspose-cells/
---

## **Aspose.Cells - Agregar texto artístico Word a una hoja de cálculo**
Utilice WordArt para agregar efectos especiales de texto a hojas de cálculo. Por ejemplo, estirar un título a través de la parte superior del archivo, decorar texto y hacer que el texto se ajuste a una forma preestablecida, o aplicar texto a una hoja de cálculo de Excel como marca de agua de fondo. El WordArt se convierte en un objeto que se puede mover o posicionar en hojas de cálculo para agregar decoración.

**Java**

{{< highlight java >}}

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
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Agregar marca de agua de texto artístico a hoja de cálculo](/cells/es/java/add-wordart-watermark-to-worksheet).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
