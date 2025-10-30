---
title: Especificar el número máximo de filas de la fórmula compartida
type: docs
weight: 40
url: /es/python-net/specify-maximum-rows-of-shared-formula/
---

## **Escenarios de uso posibles**

El número máximo predeterminado de filas para la fórmula compartida es 64. Puede ser cualquier número, por ejemplo, 1000. El rendimiento de la fórmula compartida varía con el número de filas. Por lo tanto, Aspose.Cells para Python via .NET proporciona la propiedad [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) que puede usarse para especificar el número máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas excede ese número, como se muestra en la siguiente captura.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Especificar el número máximo de filas de la fórmula compartida**

El siguiente código de ejemplo explica el uso de la propiedad [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). Establece el número máximo de filas de la fórmula compartida en 5 y agrega la fórmula compartida en la celda D1 para 100 filas y se guarda en el [archivo Excel de salida](61767856.xlsx). Si extraes el contenido del archivo Excel de salida y revisas el *sheet1.xml*, verás que la fórmula compartida se divide después de cada 5 filas como se muestra en la captura de pantalla anterior.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}
