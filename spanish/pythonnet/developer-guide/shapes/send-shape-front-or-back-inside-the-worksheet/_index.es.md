---
title: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 3400
url: /es/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Cuando hay múltiples formas en la misma ubicación, cómo serán visibles se decide por sus posiciones de orden de z. Aspose.Cells para Python via .NET proporciona el método [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) que cambia la posición del orden z de la forma. Si quieres enviar una forma al fondo, usarás un número negativo como -1, -2, -3, etc., y si deseas enviar la forma al frente, usarás un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El siguiente código de ejemplo explica el uso del método [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back). Consulta el [archivo de Excel de ejemplo](50528330.xlsx) utilizado en el código y el [archivo de Excel de salida](50528331.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo al ejecutarlo.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
