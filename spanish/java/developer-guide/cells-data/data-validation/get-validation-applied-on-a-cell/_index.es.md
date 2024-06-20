---
title: Obtener validación aplicada en una celda
type: docs
weight: 80
url: /es/java/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar validación en una celda con Java
keywords: aplicar validación de celda en Excel con Java, aplicar validación en una celda en Excel con Java, aplicar validación en Excel con Java, validación de celda en Excel con Java, Java aplica validación de celda en Excel, Java aplica validación en una celda en Excel, validación de celda en Java en Excel, validación de celda en Java
---

{{% alert color="primary" %}}

Puede utilizar la API Aspose.Cells para obtener la validación aplicada a cualquier celda. Aspose.Cells proporciona el método [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) para este propósito. Si no hay validación en la celda, devuelve nulo. De manera similar, puede utilizar el método [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) para adquirir la validación aplicada a una celda, proporcionando sus índices de fila y columna.

{{% /alert %}}

La siguiente captura de pantalla muestra el archivo de Microsoft Excel de ejemplo utilizado en el código de ejemplo a continuación. La celda **C1** tiene **validación decimal** aplicada y solo puede tomar valores **entre 10 y 20**.

**Una celda con validación**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

El código de ejemplo a continuación obtiene la validación aplicada a C1 y lee sus diversas propiedades.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Aquí está la salida de la consola del código de ejemplo ejecutado con el archivo de ejemplo mostrado en la captura de pantalla anterior.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Artículos relacionados

- [Validación de datos](/cells/es/java/data-validation/)
