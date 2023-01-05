---
title: Verifique que el valor Cell cumpla con las reglas de validación de datos
type: docs
weight: 210
url: /es/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente. Microsoft Excel muestra un mensaje de error y les pide que ingresen un número en el rango correcto. Si copia y pega un número, digamos 3, en la celda, Excel no ejecuta una verificación de validación ni muestra un mensaje de error.

veces, es necesario verificar si un valor cumple las reglas de validación de datos aplicadas a la celda mediante programación. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
## **Introducción**
 Aspose.Cells proporciona el[Cell.ObtenerValidaciónValor()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) método para validar valores de celda mediante programación. Si el valor en una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve**Falso** , más**Verdadero**.

 El siguiente código de ejemplo ilustra cómo el[Cell.ObtenerValidaciónValor()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) el método funciona. Primero, ingresa el valor 3 en C1. Debido a que esto no satisface la regla de validación de datos, el[Cell.ObtenerValidaciónValor()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) el método devuelve**Falso** . Luego, ingresa el valor 15 en C1. Debido a que este valor satisface la regla de validación de datos, el[Cell.ObtenerValidaciónValor()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) el método devuelve**Verdadero** . Del mismo modo, vuelve**Falso** por valor 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Producción**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
