---
title: GridJ'ler için özel hesaplama motoruyla çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/customcalculation/
description: Bu makalede, Aspose.Cells.GridJs kitaplığı için özel hesaplama motorunun nasıl kullanılacağı açıklanmaktadır.
---
## **Özel Hesaplama Motorunu Uygulayın**

Aspose.Cells.GridJs, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de izin verir.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Arayüzü uygular**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** olan bir**[Hesapla(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** yöntem. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde,**MYTESTFUNC** formülünü seçin ve ilk parametre değeri için 2 ile çarpın.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
