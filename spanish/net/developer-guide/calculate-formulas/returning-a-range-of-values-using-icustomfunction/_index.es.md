---
title: Retorno de un rango de valores usando ICustomFunction
description: Este artículo describe cómo usar la biblioteca Aspose.Cells para devolver un rango de valores con ICustomFunction en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para obtener un rango de valores y devolver el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, ICustomFunction, devuelve una serie de valores
type: docs
weight: 50
url: /es/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

El [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) está obsoleto desde el lanzamiento de Aspose.Cells for Java 20.8. Por favor, utiliza la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). El uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) se describe en el siguiente artículo.

[Retorno de un rango de valores usando AbstractCalculationEngine](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells proporciona la interfaz [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) que se utiliza para implementar funciones personalizadas definidas por el usuario que no son compatibles con las funciones integradas de Microsoft Excel.

Mayormente, cuando se implementa el método de la interfaz [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), es necesario devolver un valor de celda única. Pero a veces, es necesario devolver un rango de valores. Este artículo explicará cómo devolver el rango de valores desde [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

El siguiente código implementa [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) y devuelve el rango de valores a través de su método.

Crear una clase con una función *CalculateCustomFunction*. Esta clase implementa [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Ahora utiliza la función anterior en tu programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
