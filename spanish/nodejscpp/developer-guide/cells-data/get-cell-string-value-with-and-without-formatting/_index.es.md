---
title: Obtener el valor de cadena de la celda con o sin formato
type: docs
weight: 240
url: /es/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Aprende cómo obtener el valor de cadena de la celda con y sin formateo a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener valor de cadena de la celda con y sin formateo en Node.js vía C++, Obtener valor de cadena de la celda con y sin formateo en Node.js vía C++, Obtener valor de cadena de la celda con y sin formateo en Node.js vía C++
---

{{% alert color="primary" %}}

Aspose.Cells proporciona un método [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) que puede usarse para obtener el valor en cadena de la celda con o sin ningún formateo. Supón que tienes una celda con valor 0.012345 y la has formateado para mostrar solo dos lugares decimales. Entonces se mostrará como 0.01 en Excel. Puedes recuperar valores en cadena tanto como 0.01 como 0.012345 usando el método [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Toma el enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) como parámetro con los siguientes valores

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

El siguiente código de ejemplo explica el uso del método [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

