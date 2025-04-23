---
title: Establecer márgenes de comentario o forma dentro de la hoja de cálculo
type: docs
weight: 90
url: /es/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite establecer los márgenes de cualquier forma o comentario utilizando la propiedad [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment). Esta propiedad devuelve el objeto de la clase [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) que tiene diferentes propiedades como [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt), [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt), [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt), [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt), etc. que pueden ser utilizadas para establecer los márgenes superior, izquierdo, inferior y derecho.

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**

Por favor consulta el siguiente código de muestra. Carga el [archivo de Excel de muestra](61767867.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Observa el [archivo de Excel de salida](61767866.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
