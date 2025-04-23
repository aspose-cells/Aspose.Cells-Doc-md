---
title: Especificar el número máximo de filas de la fórmula compartida
type: docs
weight: 40
url: /es/java/specify-maximum-rows-of-shared-formula/
---

## **Escenarios de uso posibles**

El número máximo predeterminado de filas de la fórmula compartida son 64. Podría ser cualquier número, por ejemplo, podría ser 1000. El rendimiento de la fórmula compartida cambia con un número diferente de filas. Por lo tanto, Aspose.Cells proporciona la propiedad [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) que puede usarse para especificar el número máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula compartida es mayor que el número especificado, como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Especificar el número máximo de filas de la fórmula compartida**

El siguiente código de muestra explica el uso de la propiedad [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula). Establece el número máximo de filas de la fórmula compartida en 5, agrega la fórmula compartida en la celda D1 para 100 filas y guarda el archivo Excel de salida. Si extrae el contenido del archivo Excel de salida y revisa el *sheet1.xml*, verá que la fórmula compartida se divide después de cada 5 filas, como se destaca en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
