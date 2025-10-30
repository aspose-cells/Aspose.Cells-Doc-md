---
title: Devolver un rango de valores usando AbstractCalculationEngine con Golang mediante C++
linktitle: Devolver un rango de valores utilizando AbstractCalculationEngine
description: Este artículo presenta un motor de cálculo abstracto que devuelve un rango de valores en Microsoft Excel usando la biblioteca Aspose.Cells con Golang mediante C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para obtener un rango de valores y devolver el resultado. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, un motor de cálculo abstracto que devuelve una serie de valores
type: docs
weight: 55
url: /es/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) que se utiliza para implementar funciones personalizadas que no son compatibles con Microsoft Excel como funciones integradas.

Este artículo explicará cómo devolver el rango de valores desde [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{% /alert %}}

El siguiente código demuestra el uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) y devuelve el rango de valores a través de su método.

 Crear una clase con una función `CalculateCustomFunction`. Esta clase implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
 Ahora usa la función anterior en tu programa.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
