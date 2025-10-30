---
title: Verificar que el valor de la celda cumple con las reglas de validación de datos
type: docs
weight: 210
url: /es/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aprende cómo verificar que el valor de la celda satisface las reglas de validación de datos a través de la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Obtener Valor de Validación de Celda en Python, Obtener Valor de Validación de Celda en Python, Verificar si un valor satisface las reglas de validación de datos aplicadas a la celda en Python.
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios agregar reglas de validación de datos a las celdas. Por ejemplo, una validación decimal especifica que solo se pueden ingresar números entre 10 y 20. Si un usuario ingresa un número diferente, Microsoft Excel muestra un mensaje de error y les solicita que ingresen un número en el rango correcto. Si copias y pegas un número, digamos 3, en la celda, Excel no ejecuta una verificación de validación ni muestra un mensaje de error.

A veces, es necesario verificar si un valor cumple con las reglas de validación de datos aplicadas a la celda programáticamente. En el caso anterior, por ejemplo, la entrada debería fallar.

{{% /alert %}} 
## **Introducción**
Aspose.Cells for Python via .NET proporciona el método [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) para validar los valores de las celdas de forma programática. Si el valor de una celda no cumple con la regla de validación de datos aplicada a esa celda, devuelve **Falso**, en caso contrario devuelve **Verdadero**.

El siguiente código de ejemplo ilustra cómo funciona el método [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#). Primero, introduce el valor 3 en C1. Debido a que esto no cumple con la regla de validación de datos, el método [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) devuelve **Falso**. Luego, introduce el valor 15 en C1. Debido a que este valor cumple con la regla de validación de datos, el método [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) devuelve **Verdadero**. Del mismo modo, devuelve **Falso** para el valor 30.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Salida**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
