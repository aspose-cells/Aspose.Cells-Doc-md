---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende a verificar que el valor de la celda cumple con las reglas de validación de datos a través de la API Aspose.Cells for .NET.
keywords: Obtener valor de validación de la celda, obtener valor de validación de la celda, verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Microsoft Excel muestra un mensaje de error y les solicita que ingresen un número en el rango correcto. Si copias y pegas un número, digamos 3, en la celda, Excel no ejecuta una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
## **Introducción**
Aspose.Cells proporciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) para validar los valores de las celdas programáticamente. Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve **Falso**, de lo contrario **Verdadero**.

El siguiente código de ejemplo ilustra cómo funciona el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue). Primero, ingresa el valor 3 en C1. Debido a que esto no cumple con la regla de validación de datos, el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) devuelve **Falso**. Luego, ingresa el valor 15 en C1. Debido a que este valor cumple con la regla de validación de datos, el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) devuelve **Verdadero**. De manera similar, devuelve **Falso** para el valor 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Salida**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
