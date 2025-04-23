---
title: Enviar la forma al frente o atrás dentro de la hoja de cálculo
type: docs
weight: 600
url: /es/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Cuando hay múltiples formas presentes en la misma ubicación, su visibilidad se decide por sus posiciones de orden z. Aspose.Cells proporciona el método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-) que cambia la posición de orden z de la forma. Si desea enviar la forma atrás, utilizará un número negativo como -1, -2, -3, etc. Y si desea enviar la forma al frente, utilizará un número positivo como 1, 2, 3, etc.

## **Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo**

El siguiente código de ejemplo explica el uso del método [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-). Consulte el [archivo de Excel de muestra](50528362.xlsx) utilizado dentro del código y el [archivo de Excel de salida](50528361.xlsx) generado por él. La captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarlo.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
