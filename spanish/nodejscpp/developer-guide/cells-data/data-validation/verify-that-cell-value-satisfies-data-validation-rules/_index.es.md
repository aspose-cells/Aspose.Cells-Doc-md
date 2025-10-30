---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende cómo verificar si el valor de una celda satisface las reglas de validación de datos a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener valor de validación de celda en Node.js vía C++, obtener valor de validación de celda en Node.js vía C++, verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda en Node.js vía C++
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Excel muestra un mensaje de error y solicita ingresar un número en el rango correcto. Si copias y pegas un número, por ejemplo 3, en la celda, Excel no realiza una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
## **Introducción**
Aspose.Cells for Node.js via C++ proporciona el método [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) para validar los valores de las celdas de forma programática. Si el valor en una celda no cumple con la regla de validación de datos aplicada, devuelve **false**, de lo contrario, **true**.

El siguiente código de ejemplo ilustra cómo funciona el método [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--). Primero, introduce el valor 3 en C1. Como esto no cumple con la regla de validación de datos, el método devuelve **false**. Luego, introduce el valor 15 en C1. Como este valor cumple con la regla, el método devuelve **true**. De manera similar, devuelve **false** para el valor 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Salida**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
