---  
title: Establecer márgenes del comentario o forma dentro de la hoja de cálculo con Golang vía C++  
linktitle: Establecer márgenes de comentario o forma dentro de la hoja de cálculo  
type: docs  
weight: 1500  
url: /es/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aprender a establecer márgenes de comentarios o formas dentro de una hoja de cálculo usando Aspose.Cells con Golang vía C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells le permite configurar los márgenes de cualquier forma o comentario usando la propiedad [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/). Esta propiedad devuelve el objeto de la clase [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) que tiene diferentes propiedades, por ejemplo, [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), etc., que se pueden usar para establecer los márgenes superior, izquierdo, inferior y derecho.  

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**  

Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](61767851.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Por favor, vea el [archivo de Excel de salida](61767852.xlsx) generado por el código y una captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Código de muestra**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
