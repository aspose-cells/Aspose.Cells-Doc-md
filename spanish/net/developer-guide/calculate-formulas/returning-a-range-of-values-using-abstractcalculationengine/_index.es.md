---
title: Devolver un rango de valores utilizando AbstractCalculationEngine
description: Este artículo presenta un motor de cálculo abstracto que devuelve un rango de valores en Microsoft Excel utilizando la librería Aspose.Cells. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para obtener un rango de valores y devolver el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, un motor de cálculo abstracto que devuelve una serie de valores
type: docs
weight: 55
url: /es/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) que se utiliza para implementar funciones personalizadas que no son compatibles con Microsoft Excel como funciones integradas.

Este artículo explicará cómo devolver el rango de valores desde [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

El siguiente código demuestra el uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) y devuelve el rango de valores a través de su método.

Crear una clase con una función *CalculateCustomFunction*. Esta clase implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Ahora utiliza la función anterior en tu programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
