---
title: Exportar rango de Cells en una hoja de trabajo a imagen
type: docs
weight: 60
url: /es/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Posibles escenarios de uso**

Puede crear una imagen de una hoja de trabajo usando Aspose.Cells. Sin embargo, a veces necesita exportar solo un rango de celdas en una hoja de trabajo a una imagen. Este artículo explica cómo lograr esto.

## **Exportar rango de Cells en una hoja de trabajo a imagen**

 Para tomar una imagen de un rango, configure el área de impresión en el rango deseado y luego configure todos los márgenes en 0. Configure también[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) a**verdadero** . El siguiente código toma una imagen del rango D8:G16. A continuación se muestra una captura de pantalla de la[ejemplo de archivo de Excel](47153160.xlsx) utilizado en el código. Puedes probar el código con cualquier archivo de Excel.

## **Captura de pantalla del archivo Excel de muestra y su imagen exportada**

**![todo:image_alt_text](exportar-rango-de-celdas-en-una-hoja-de-trabajo-a-image_1.png)**

Ejecutar el código crea una imagen del rango D8: G16 únicamente.

**![todo:image_alt_text](Imagen-Salida.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
