---
title: Devolver un rango de valores usando AbstractCalculationEngine
type: docs
weight: 55
url: /es/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Este artículo explicará cómo devolver el rango de valores de[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 El siguiente código demuestra el uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase y devuelve el rango de valores a través de su método.

Crear una clase con una función.*CalculateCustomFunction*. Esta clase implementa[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Ahora use la función anterior en su programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
