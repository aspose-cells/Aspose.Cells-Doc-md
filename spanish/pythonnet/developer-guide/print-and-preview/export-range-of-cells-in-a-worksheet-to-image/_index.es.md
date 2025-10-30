---
title: Exportar rango de celdas en una hoja de cálculo a imagen
type: docs
weight: 60
url: /es/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Escenarios de uso posibles**

Puedes crear una imagen de una hoja de cálculo usando Aspose.Cells para Python via .NET. Sin embargo, a veces necesitas exportar solo un rango de celdas de una hoja a una imagen. Este artículo explica cómo lograr esto.

## **Exportar un rango de celdas en una hoja de cálculo a una imagen**

Para tomar una imagen de un rango, establezca el área de impresión en el rango deseado y luego establezca todos los márgenes en 0. También establezca [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) a **true**. El siguiente código toma una imagen del rango D8:G16. A continuación se muestra una captura de pantalla del [archivo de Excel de muestra](47153160.xlsx) utilizado en el código. Puede probar el código con cualquier archivo de Excel.

## **Captura de pantalla del archivo de Excel de muestra y su imagen exportada**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Al ejecutar el código se crea una imagen del rango D8:G16 solamente.

**![todo:image_alt_text](Output-Image.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
