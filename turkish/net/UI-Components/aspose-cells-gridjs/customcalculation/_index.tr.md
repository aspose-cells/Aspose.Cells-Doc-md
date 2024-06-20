---
title: GridJs için özel hesaplama motoru ile çalışmak
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs,custom,calculation,customcalculation
description: Bu makale, Aspose.Cells.GridJs kütüphanesi için özel hesaplama motorunu nasıl kullanacağınızı açıklar.
---

## **Özel Hesaplama Motorunu Uygulama**

Aspose.Cells.GridJs, neredeyse tüm Microsoft Excel formüllerini hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, varsayılan hesaplama motorunu genişletmenizi sağlar, bu da size daha fazla güç ve esneklik sağlar.

Bu özellik uygulamada kullanılan özellik ve sınıflar.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Bir [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) arayüzünü uygular ve [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate) yöntemine sahiptir. Bu yöntem, formüllerinizin tümüne karşı çağrılır. Bu yöntemin içinde, **MYTESTFUNC** formülünü yakalar ve ilk parametre değerini 2 ile çarpar.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

