---
title: Especificar filas máximas de fórmula compartida
type: docs
weight: 40
url: /es/java/specify-maximum-rows-of-shared-formula/
---
## **Posibles escenarios de uso**

Las filas máximas predeterminadas de la fórmula compartida son 64. Podría ser cualquier número, por ejemplo, podría ser 1000. El rendimiento de la fórmula compartida cambia con un número diferente de filas. Por lo tanto, Aspose.Cells proporciona la[**Libro de trabajo.Configuración.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)propiedad que se puede utilizar para especificar el máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula compartida es mayor, como se muestra en la siguiente captura de pantalla.

![todo:imagen_alternativa_texto](specify-maximum-rows-of-shared-formula_1.png)

## **Especificar filas máximas de fórmula compartida**

El siguiente código de ejemplo explica el uso de la[**Libro de trabajo.Configuración.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)propiedad. Establece el máximo de filas de la fórmula compartida en 5 y agrega la fórmula compartida en la celda D1 para 100 filas y guarda en[archivo de salida de Excel](61767869.xlsx). Si extrae el contenido del archivo de salida de Excel y comprueba el*hoja1.xml*, verá que la fórmula compartida se divide después de cada 5 filas, como se resalta en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
