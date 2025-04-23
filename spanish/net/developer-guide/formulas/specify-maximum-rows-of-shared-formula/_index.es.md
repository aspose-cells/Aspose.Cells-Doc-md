---
title: Especificar el número máximo de filas de la fórmula compartida
type: docs
weight: 40
url: /es/net/specify-maximum-rows-of-shared-formula/
---

## **Escenarios de uso posibles**

El número máximo predeterminado de filas de la fórmula compartida es 64. Podría ser cualquier número, por ejemplo, podría ser 1000. El rendimiento de la fórmula compartida cambia con un número diferente de filas. Por lo tanto, Aspose.Cells proporciona la propiedad [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) que se puede usar para especificar el número máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula compartida es mayor que el número mostrado en la siguiente captura de pantalla.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Especificar el número máximo de filas de la fórmula compartida**

El siguiente código de ejemplo explica el uso de la propiedad [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). Establece el número máximo de filas de la fórmula compartida en 5 y agrega la fórmula compartida en la celda D1 para 100 filas y se guarda en el [archivo Excel de salida](61767856.xlsx). Si extraes el contenido del archivo Excel de salida y revisas el *sheet1.xml*, verás que la fórmula compartida se divide después de cada 5 filas como se muestra en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
