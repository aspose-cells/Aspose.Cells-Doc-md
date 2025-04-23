---
title: Obtener validación aplicada en una celda
type: docs
weight: 200
url: /es/nodejs-cpp/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con Node.js vía C++.
keywords: aplicar validación en celda en Excel con Node.js vía C++, aplicar validación en una celda en Excel con Node.js vía C++, aplicar validación en Excel con Node.js vía C++, validación de celda en Excel con Node.js vía C++, Node.js vía C++ aplicar validación en celda en Excel, Node.js vía C++ aplicar validación en una celda en Excel, Node.js vía C++ validación en celda en Excel
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para Node.js para obtener la validación aplicada a una celda. Aspose.Cells proporciona el método [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) para este propósito. Si no hay validación en la celda, devuelve null.

De manera similar, puede usar el método [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

## Código Node.js para obtener la validación aplicada en una Celda

El siguiente ejemplo de código muestra cómo obtener la validación aplicada en una celda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Artículos relacionados

- [Validación de datos](/cells/es/nodejs-cpp/data-validation/)
