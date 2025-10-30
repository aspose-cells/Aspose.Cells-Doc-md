---
title: Traer formas al frente o al fondo en una hoja de cálculo
type: docs
weight: 3400
url: /es/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Cuando hay múltiples formas presentes en la misma ubicación, la forma en que se mostrarán está decidida por sus posiciones de orden z. Aspose.Cells proporciona el método [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) que cambia la posición de orden z de la forma. Si quieres enviar la forma al fondo, usarás un número negativo como -1, -2, -3, etc. y si quieres enviar la forma al frente, usarás un número positivo como 1, 2, 3, etc.

## **Traer forma al frente o al fondo dentro de la hoja de cálculo**

El siguiente código de ejemplo explica el uso del método [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)). Por favor, vea el [archivo de ejemplo Excel](sampleToFrontOrBack.xlsx) utilizado dentro del código y el [archivo Excel de salida](50528331.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo Excel de ejemplo al ejecutarse.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
