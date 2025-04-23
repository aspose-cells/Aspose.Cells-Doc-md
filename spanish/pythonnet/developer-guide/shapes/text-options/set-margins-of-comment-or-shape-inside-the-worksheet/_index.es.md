---
title: Establecer márgenes de comentario o forma dentro de la hoja de cálculo
type: docs
weight: 1500
url: /es/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET te permite establecer los márgenes de cualquier forma o comentario usando la propiedad [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment). Esta propiedad devuelve el objeto de la clase [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment), que tiene diferentes propiedades como [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt), [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt), [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt), [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt), etc., que se pueden usar para ajustar los márgenes superior, izquierdo, inferior y derecho.

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**

Consulta el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](61767851.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Consulta el [archivo de Excel de salida](61767852.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
