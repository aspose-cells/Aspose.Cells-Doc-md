---
title: Enviar forma al frente o al reverso dentro de la hoja de trabajo
type: docs
weight: 600
url: /es/java/send-shape-front-or-back-inside-the-worksheet/
---
## **Posibles escenarios de uso**

Cuando hay varias formas presentes en la misma ubicación, la forma en que serán visibles se decide por sus posiciones en el orden z. Aspose.Cells proporciona[**Forma.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) método que cambia la posición del orden z de la forma. Si desea enviar la forma hacia atrás, usará un número negativo como -1, -2, -3, etc. y si desea enviar la forma al frente, usará un número positivo como 1, 2, 3, etc.

## **Enviar forma al frente o al reverso dentro de la hoja de trabajo**

El siguiente código de ejemplo explica el uso de[**Forma.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) método. Por favor vea el[ejemplo de archivo de Excel](50528362.xlsx)utilizado dentro del código y el[archivo de salida de Excel](50528361.xlsx)generada por ella. La captura de pantalla muestra el efecto del código en el archivo de ejemplo de Excel durante la ejecución.

![todo:imagen_alternativa_texto](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
