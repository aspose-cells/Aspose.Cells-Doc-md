---
title: Establecer márgenes de comentario o forma dentro de la hoja de cálculo
type: docs
weight: 1500
url: /es/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite establecer los márgenes de cualquier forma o comentario usando la propiedad [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment). Esta propiedad devuelve el objeto de la clase [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment) que tiene diferentes propiedades como [**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt), [**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt), [**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt), [**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt), etc. que se pueden usar para establecer los márgenes superior, izquierdo, inferior y derecho.

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**

Consulta el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](61767851.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Consulta el [archivo de Excel de salida](61767852.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
