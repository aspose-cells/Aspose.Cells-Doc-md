---
title: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 3400
url: /es/net/send-shape-front-or-back-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Cuando hay múltiples formas presentes en la misma ubicación, la forma en que se mostrarán está decidida por sus posiciones de orden z. Aspose.Cells proporciona el método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) que cambia la posición de orden z de la forma. Si quieres enviar la forma al fondo, usarás un número negativo como -1, -2, -3, etc. y si quieres enviar la forma al frente, usarás un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El siguiente código de ejemplo explica el uso del método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback). Consulta el [archivo de Excel de ejemplo](50528330.xlsx) utilizado en el código y el [archivo de Excel de salida](50528331.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo al ejecutarlo.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
