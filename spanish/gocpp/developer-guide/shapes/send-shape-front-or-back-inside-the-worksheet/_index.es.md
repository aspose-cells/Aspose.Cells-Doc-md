---
title: Enviar forma al frente o fondo dentro de la hoja de cálculo con Golang vía C++
linktitle: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 3400
url: /es/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aprende cómo cambiar la posición del orden Z de las formas en una hoja de cálculo utilizando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando hay varias formas presentes en la misma ubicación, su visibilidad se determina por sus posiciones en el orden Z. Aspose.Cells proporciona el método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/), que cambia la posición del orden Z de la forma. Si deseas enviar una forma al fondo, usarás un número negativo como -1, -2, -3, etc. Si deseas traer una forma al frente, usarás un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El siguiente código de ejemplo demuestra el uso del método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/). Por favor, vea el [archivo de Excel de muestra](50528330.xlsx) utilizado en el código y el [archivo de Excel de salida](50528331.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarse.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
