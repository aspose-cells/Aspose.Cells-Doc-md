---
title: Cálculo de la fórmula de matriz en tablas de datos con Golang mediante C++
linktitle: Cálculo de la fórmula de arreglo de tablas de datos
description: Cómo usar la biblioteca Aspose.Cells para calcular fórmulas de matriz para una tabla de datos en Microsoft Excel con Golang mediante C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar el método proporcionado por Aspose.Cells para calcular la fórmula de matriz de la tabla de datos y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, tablas de datos, fórmulas de matriz, cálculos, C++
type: docs
weight: 70
url: /es/go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Puede crear una tabla de datos en Microsoft Excel utilizando Datos > Análisis ¿Y si? > Tabla de datos.... Ahora Aspose.Cells le permite calcular la fórmula de arreglo de una tabla de datos. Por favor, use [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) como normal para calcular cualquier tipo de fórmulas.

{{% /alert %}}

En el siguiente código de ejemplo, usamos el [archivo de Excel de origen](5115535.xlsx). Si cambia el valor de la celda B1 a 100, los valores de la tabla de datos que están llenos con color amarillo se convertirán en 120 como se muestra en las siguientes imágenes. El código de ejemplo genera el [PDF de salida](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

A continuación se muestra el código de ejemplo utilizado para generar el [PDF de salida](5115538.pdf) a partir del [archivo de Excel de origen](5115535.xlsx). Por favor, lea los comentarios para más información.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}
