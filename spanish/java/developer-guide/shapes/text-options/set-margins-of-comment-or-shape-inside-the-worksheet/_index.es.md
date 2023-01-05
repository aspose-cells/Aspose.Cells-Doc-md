---
title: Establecer márgenes de comentario o forma dentro de la hoja de trabajo
type: docs
weight: 90
url: /es/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---
## **Posibles escenarios de uso**

 Aspose.Cells le permite configurar los márgenes de cualquier forma o comentario usando el[**Forma.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment) propiedad. Esta propiedad devuelve el objeto de[**FormaTextoAlineación**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) clase que tiene diferentes propiedades, por ejemplo[**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt), [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt), [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt), [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt), etc. que se pueden usar para establecer los márgenes superior, izquierdo, inferior y derecho.

## **Establecer márgenes de comentario o forma dentro de la hoja de trabajo**

 Consulte el siguiente código de ejemplo. carga el[ejemplo de archivo de Excel](61767867.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Por favor vea el[archivo de salida de Excel](61767866.xlsx) generado por el código y captura de pantalla que muestra el efecto del código en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
