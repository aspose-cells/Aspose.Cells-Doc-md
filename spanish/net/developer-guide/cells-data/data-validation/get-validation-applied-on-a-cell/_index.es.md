---
title: Obtener validación aplicada en una celda
type: docs
weight: 200
url: /es/net/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con C#.
keywords: aplicar validación de celda en excel con c#, aplicar validación en una celda en excel con c#, aplicar validación en excel con c#, validación de celda en excel con c#, c# aplicar validación de celda en excel, c# aplicar validación en una celda en excel, c# validación de celda en excel, c# validación de celda
---

{{% alert color="primary" %}}

Puede usar Aspose.Cells para obtener la validación aplicada a una celda. Aspose.Cells proporciona el método [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) para este fin. Si no hay validación aplicada en la celda, devuelve nulo.

De manera similar, puede usar el método [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

## Código C# para obtener la validación aplicada en una Celda

El siguiente código de ejemplo le muestra cómo obtener la validación aplicada en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## Artículos relacionados

- [Validación de datos](/cells/es/net/data-validation/)
{{< app/cells/assistant language="csharp" >}}
