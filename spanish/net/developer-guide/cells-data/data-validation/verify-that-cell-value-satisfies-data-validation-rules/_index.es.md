---
title: Verifique que el valor Cell cumpla con las reglas de validación de datos
type: docs
weight: 210
url: /es/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprenda cómo verificar que el valor Cell cumpla con las reglas de validación de datos a través del Aspose.Cells for .NET API.
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente. Microsoft Excel muestra un mensaje de error y les solicita que ingresen un número en el rango correcto. Si copia y pega un número, digamos 3, en la celda, Excel no ejecuta una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor satisface las reglas de validación de datos aplicadas a la celda mediante programación. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
##  **Introducción**
 Aspose.Cells proporciona la[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)Método para validar valores de celda mediante programación. Si el valor de una celda no satisface la regla de validación de datos aplicada a esa celda, devuelve *Falso**; en caso contrario, *Verdadero**.

 El siguiente código de muestra ilustra cómo[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) El método funciona. Primero, ingresa el valor 3 en C1. Debido a que esto no satisface la regla de validación de datos, el[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) el método devuelve**FALSO**. Luego, ingresa el valor 15 en C1. Debido a que este valor satisface la regla de validación de datos, el método [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) devuelve **Verdadero**. Del mismo modo, devuelve **Falso** por valor 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Producción**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
