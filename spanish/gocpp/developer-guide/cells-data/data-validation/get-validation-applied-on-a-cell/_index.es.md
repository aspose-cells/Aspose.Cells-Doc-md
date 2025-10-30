---
title: Obtener la validación aplicada en una celda con Golang a través de C++
linktitle: Obtener validación aplicada en una celda
type: docs
weight: 200
url: /es/go-cpp/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con Golang a través de C++.
keywords: aplicar validación de celda en Excel con C++, aplicar validación en una celda en Excel con C++, aplicar validación en Excel con C++, validación de celda en Excel con C++, C++ aplicar validación en celda en Excel, C++ aplicar validación en una celda en Excel, validación de celda en Excel con C++, validación de celda con C++
---

{{% alert color="primary" %}}

Puede usar Aspose.Cells para obtener la validación aplicada a una celda. Aspose.Cells proporciona el método [**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/) para este fin. Si no hay validación aplicada en la celda, devuelve nulo.

De manera similar, puede usar el método [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

## Código en C++ para obtener la validación aplicada en una celda

El siguiente ejemplo de código muestra cómo obtener la validación aplicada en una celda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## Artículos relacionados

- [Validación de datos](/cells/es/cpp/data-validation/)
