---
title: Özel hesaplama motoru ile çalışma
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, özel, hesaplama, CalculationEngine, GridAbstractCalculationEngine
description: Bu makale, GridWeb de hesaplama sürecini özelleştirmek için GridAbstractCalculationEngine in nasıl kullanılacağını tanıtıyor.
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells.Gridweb, neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, varsayılan hesaplama motorunu genişletmenize olanak tanır, bu da size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bir [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) arayüzünü uygular ve [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate) yöntemine sahiptir. Bu yöntem, formüllerinizin tümüne karşı çağrılır. Bu yöntemin içinde, **MYTESTFUNC** formülünü yakalar ve ilk parametre değerini 2 ile çarpar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

