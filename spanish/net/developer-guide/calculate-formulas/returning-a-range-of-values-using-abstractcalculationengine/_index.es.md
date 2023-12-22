---
title: Devolver un rango de valores usando AbstractCalculationEngine
description: Este artículo presenta un motor de cálculo abstracto que devuelve un rango de valores en Microsoft Excel utilizando la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para obtener un rango de valores y devolver el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /es/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Este artículo explicará cómo devolver el rango de valores de[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 El siguiente código demuestra el uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase y devuelve el rango de valores a través de su método.

Crea una clase con una función *CalculateCustomFunction*. Esta clase implementa[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Ahora use la función anterior en su programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
