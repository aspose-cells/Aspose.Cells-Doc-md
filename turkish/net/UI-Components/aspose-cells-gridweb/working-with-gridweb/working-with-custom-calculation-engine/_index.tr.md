---
title: Özel hesaplama motoruyla çalışma
type: docs
weight: 70
url: /tr/net/working-with-custom-calculation-engine/
---
## **Özel Hesaplama Motorunu Uygulayın**

Aspose.Cells.Gridweb, Microsoft Excel formüllerinin neredeyse tamamını hesaplayabilen güçlü bir hesaplama motoruna sahiptir. Buna rağmen, size daha fazla güç ve esneklik sağlayan varsayılan hesaplama motorunu genişletmenize de izin verir.

Bu özelliğin uygulanmasında aşağıdaki özellik ve sınıflar kullanılır.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Aşağıdaki kod, Özel Hesaplama Motorunu uygular. Arayüzü uygular**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** olan bir**[Hesapla(GridCalculationData data)](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** yöntem. Bu yöntem, tüm formüllerinize karşı çağrılır. Bu yöntemin içinde,**MYTESTFUNC** formülünü seçin ve ilk parametre değeri için 2 ile çarpın.

### **Programlama Örneği**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

