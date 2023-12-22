---
title: Devolver un rango de valores usando ICustomFunction
description: Este artículo describe cómo utilizar la biblioteca Aspose.Cells para devolver un rango de valores con ICustomFunction en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para obtener un rango de valores y devolver el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /es/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 El[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) está en desuso desde el lanzamiento de Aspose.Cells for Java 20.8. Por favor use el[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase. El uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) La clase se describe en el siguiente artículo.

[Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells proporciona[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)interfaz que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Principalmente cuando implementas el[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) método de interfaz, debe devolver un valor de celda única. Pero a veces es necesario devolver un rango de valores. Este artículo explicará cómo devolver el rango de valores de[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 El siguiente código implementa[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)y devuelve el rango de valores a través de su método.

Crea una clase con una función *CalculateCustomFunction*. Esta clase implementa[**Función personalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Ahora use la función anterior en su programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
