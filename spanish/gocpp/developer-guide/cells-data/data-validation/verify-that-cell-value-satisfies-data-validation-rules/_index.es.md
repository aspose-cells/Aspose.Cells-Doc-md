---
title: Verifique que el valor de la celda satisfaga las reglas de validación de datos con Golang a través de C++
linktitle: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende cómo verificar si el valor de la celda cumple con las reglas de validación de datos a través de la API Aspose.Cells for C++.
keywords: Obtener valor de validación de la celda, obtener valor de validación de la celda, verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Excel muestra un mensaje de error y solicita ingresar un número en el rango correcto. Si copias y pegas un número, por ejemplo 3, en la celda, Excel no realiza una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 

## **Introducción**
Aspose.Cells proporciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) para validar valores de celdas de forma programática. Si el valor en una celda no satisface la regla de validación de datos aplicada a esa celda, devuelve **False**, de lo contrario **True**.

El siguiente código de ejemplo ilustra cómo funciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/). Primero, ingresa el valor 3 en C1. Debido a que esto no satisface la regla de validación de datos, el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) devuelve **False**. Luego, ingresa el valor 15 en C1. Debido a que este valor satisface la regla de validación de datos, el método devuelve **True**. De manera similar, devuelve **False** para el valor 30.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Salida**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
