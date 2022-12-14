---
title: Obtenga la validación aplicada en un Cell
type: docs
weight: 80
url: /es/java/get-validation-applied-on-a-cell/
description: Este artículo muestra cómo aplicar la validación en un Cell con Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Puede usar Aspose.Cells API para aplicar la validación a cualquier celda. Aspose.Cells proporciona el[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) método para este propósito. Si no hay validación en la celda, devuelve nulo. Del mismo modo, puede utilizar el[**Worksheet.getValidations().getValidationInCell(fila int, columna int)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) para adquirir la validación aplicada a una celda proporcionando sus índices de fila y columna.

{{% /alert %}}

 La siguiente instantánea muestra el archivo de Excel de ejemplo Microsoft utilizado en el código de ejemplo a continuación. Cell**C1** posee**validación decimal** aplicado y sólo puede tomar valores**entre 10 y 20**.

**Una celda con validación**

![todo:imagen_alternativa_texto](get-validation-applied-on-a-cell_1.png)

El código de muestra a continuación obtiene la validación aplicada a C1 y lee sus diversas propiedades.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Aquí está la salida de la consola del código de muestra ejecutado con el archivo de muestra que se muestra en la instantánea anterior.

{{< highlight "java" >}}

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
