---
title: Gira el texto con forma dentro de la hoja de cálculo con Golang vía C++
linktitle: Rotar texto con forma
type: docs
weight: 1300
url: /es/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Aprenda a controlar la rotación del texto con formas en hojas de cálculo de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puede agregar texto dentro de cualquier forma utilizando Microsoft Excel. Si agrega una forma usando la muy antigua Microsoft Excel 2003, entonces el texto no rotará con la forma. Sin embargo, si agrega una forma usando versiones más recientes de Microsoft Excel, como 2007, 2010, 2013 o 2016, el texto rotará con la forma. Puede controlar si el texto debe rotar con la forma o no usando la propiedad [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/). El valor predeterminado de esta propiedad es **true**, lo que significa que el texto rotará con la forma. Si lo configura como **false**, el texto no rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716896.xlsx) que contiene una forma de triángulo, y su texto rota con la forma. Si abre el archivo de Excel de muestra en Microsoft Excel y rota la forma del triángulo, el texto también rotará con ella. Luego el código establece la propiedad [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) en **false** y lo guarda como el [archivo de Excel de salida](64716897.xlsx). Si ahora abre el archivo de Excel de salida en Microsoft Excel y rota la forma del triángulo, el texto no rotará con ella. Por favor, vea la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra como referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
