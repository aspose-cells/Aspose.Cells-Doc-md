---
title: Obtener valor de cadena de celda con y sin formato con Golang vía C++
linktitle: Obtener valor de cadena de celda
type: docs
weight: 240
url: /es/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Aprende cómo obtener el valor de cadena de una celda con y sin formato a través de la API Aspose.Cells for C++.
keywords: Obtener el valor de cadena de la celda con o sin formato, recuperar el valor de cadena de la celda con o sin formato, obtener el valor de cadena de la celda con o sin formato
---

{{% alert color="primary" %}}

Aspose.Cells proporciona un método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) que puede usarse para obtener el valor de cadena de la celda con o sin ningún formato. Supón que tienes una celda con valor 0.012345 y la formateaste para mostrar solo dos decimales. Entonces, mostrará como 0.01 en Excel. Puedes recuperar los valores de cadena tanto como 0.01 como 0.012345 usando el método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Este método toma el enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) con los siguientes valores:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- Estrategia de Formato de Valor de Celda::Cadena de Visualización
- Estrategia de Formato de Valor de Celda::Ninguno

{{% /alert %}}

El siguiente código de ejemplo explica el uso del método [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
