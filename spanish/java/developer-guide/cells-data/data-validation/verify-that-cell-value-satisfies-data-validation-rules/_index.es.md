---
title: Verifique que el valor Cell cumpla con las reglas de validación de datos
type: docs
weight: 90
url: /es/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas de la hoja de trabajo. Por ejemplo, se puede aplicar una validación decimal para restringir los números entre 10 y 20. Si se ingresa cualquier otro número fuera de este rango especificado, el Excel Microsoft muestra un mensaje de error y solicita al usuario que vuelva a ingresar un número del rango correcto. Si la copia del usuario pega un número, digamos 3, en la celda, Excel no ejecuta la verificación de validación ni muestra un mensaje de error.

{{% /alert %}}

## Verifique que el valor Cell cumpla con las reglas de validación de datos

A veces, es necesario verificar dinámicamente si un valor dado satisface las reglas de validación de datos aplicadas a la celda. Para ello, las API Aspose.Cells proporcionan la[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) método. Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve**Falso** , más**Verdadero**.

El siguiente archivo Excel de ejemplo Microsoft se usa con el código de ejemplo a continuación para probar el[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) método. Como puede ver en la instantánea que las celdas**C1** posee**validación de datos decimales** aplicado y sólo aceptará valores**entre 10 y 20** . Siempre que el valor de la celda esté entre 10 y 20,[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) el método devolverá**Verdadero** , de lo contrario, volverá**Falso**.

![todo:imagen_alternativa_texto](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 El siguiente código de ejemplo ilustra cómo el[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) método funciona. Primero, ingresa el valor 3 en C1. Debido a que esto no satisface la regla de validación de datos, el[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) el método devuelve**Falso** . Luego, ingresa el valor 15 en C1. Debido a que este valor satisface la regla de validación de datos, el[**celda.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) el método devuelve**Verdadero** . Del mismo modo, vuelve**Falso** por valor 30.

## Java código para verificar si un valor Cell cumple con las reglas de validación de datos

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Salida de la consola generada por el código de muestra

Esta es la salida de la consola generada cuando el código de muestra se ejecuta con el archivo de muestra de Excel que se muestra arriba.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
