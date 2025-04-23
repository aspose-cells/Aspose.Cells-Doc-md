---
title: Exportar rango de celdas en una hoja de cálculo a imagen
type: docs
weight: 60
url: /es/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Escenarios de uso posibles**

Puede hacer una imagen de una hoja de cálculo utilizando Aspose.Cells. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de cálculo a una imagen. Este artículo explica cómo lograrlo.

## **Exportar un rango de celdas en una hoja de cálculo a una imagen**

Para tomar una imagen de un rango, establezca el área de impresión en el rango deseado y luego establezca todos los márgenes en 0. También establezca [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) a **true**. El siguiente código toma una imagen del rango D8:G16. A continuación se muestra una captura de pantalla del [archivo de Excel de muestra](47153160.xlsx) utilizado en el código. Puede probar el código con cualquier archivo de Excel.

## **Captura de pantalla del archivo de Excel de muestra y su imagen exportada**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Al ejecutar el código se crea una imagen del rango D8:G16 solamente.

**![todo:image_alt_text](Output-Image.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
