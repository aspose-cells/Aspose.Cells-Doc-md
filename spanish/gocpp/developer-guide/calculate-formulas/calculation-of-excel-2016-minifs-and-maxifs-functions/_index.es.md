---
title: Cálculo de las funciones MINIFS y MAXIFS de Excel 2016 con Golang mediante C++
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para calcular las funciones MINIFS y MAXIFS en Microsoft Excel 2016 usando C++.
keywords: Aspose.Cells, Excel, 2016, función MINIFS, función MAXIFS, cálculo
type: docs
weight: 300
url: /es/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Escenarios de uso posibles**
Microsoft Excel 2016 soporta las funciones MINIFS y MAXIFS. Estas funciones no son compatibles en Excel 2013 o versiones anteriores. Aspose.Cells también soporta el cálculo de estas funciones. La siguiente captura de pantalla ilustra el uso de estas funciones. Por favor, lee los comentarios en rojo dentro de la captura para entender cómo funcionan estas funciones.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Cálculo de las funciones MINIFS y MAXIFS de Excel 2016**
El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115149.xlsx) y llama al método [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) para realizar el cálculo de la fórmula mediante Aspose.Cells y luego guarda los resultados en el [PDF de salida](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
