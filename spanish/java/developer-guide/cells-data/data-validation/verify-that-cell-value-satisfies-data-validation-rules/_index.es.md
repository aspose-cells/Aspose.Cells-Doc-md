---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 90
url: /es/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas de la hoja de cálculo. Por ejemplo, se puede aplicar una validación decimal para restringir los números entre 10 y 20. Si se ingresa cualquier otro número fuera de este rango especificado, Microsoft Excel muestra un mensaje de error y solicita al usuario que vuelva a ingresar un número del rango correcto. Si el usuario copia y pega un número, por ejemplo, 3, en la celda, Excel no ejecuta la comprobación de validación ni muestra un mensaje de error.

{{% /alert %}}

## Verificar que el valor de la celda cumple con las reglas de validación de datos

A veces es necesario verificar de forma dinámica si un valor dado cumple con las reglas de validación de datos aplicadas a la celda. Con este propósito, las API de Aspose.Cells proporcionan el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve **Falso**, de lo contrario **Verdadero**.

El siguiente archivo de ejemplo de Microsoft Excel se utiliza con el código de ejemplo a continuación para probar el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Como se puede ver en la captura de pantalla, las celdas **C1** tienen **validación de datos decimales** aplicada y solo aceptarán valores **entre 10 y 20**. Cada vez que el valor de la celda esté entre 10 y 20, el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) devolverá **Verdadero**, de lo contrario, devolverá **Falso**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

El siguiente código de ejemplo ilustra cómo funciona el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Primero, ingresa el valor 3 en C1. Debido a que esto no cumple con la regla de validación de datos, el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) devuelve **Falso**. Luego, ingresa el valor 15 en C1. Dado que este valor cumple con la regla de validación de datos, el método [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) devuelve **Verdadero**. De manera similar, devuelve **Falso** para el valor 30.

## Código Java para verificar si el valor de una celda cumple con las reglas de validación de datos

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Salida de consola generada por el código de ejemplo

Aquí está la salida de la consola generada cuando se ejecuta el código de ejemplo con el archivo de Excel de ejemplo mostrado anteriormente.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
