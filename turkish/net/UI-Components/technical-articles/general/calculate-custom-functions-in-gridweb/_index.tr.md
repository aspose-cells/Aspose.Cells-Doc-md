---
title: Bir dataview nesnesinden liste öğelerini yüklemek için LoadValueList yöntemini kullanın 
type: docs
weight: 90
url: /tr/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: GridWeb de Özel Fonksiyonları Hesaplama
---


## **Olası Kullanım Senaryoları**
Aspose.Cells.GridWeb, GridWeb.CustomCalculationEngine özelliğiyle özel fonksiyonların hesaplanmasını destekler. Bu özellik GridAbstractCalculationEngine arabirim örneğini alır. Lütfen GridAbstractCalculationEngine arabirimini uygulayın ve özel fonksiyonlarınızı kendi mantığınızla hesaplayın.
## **GridWeb'de Özel Fonksiyonları Hesaplayın**
Aşağıdaki örnek kod, B3 hücresine MYTESTFUNC() adında özel bir fonksiyon ekler. Daha sonra, GridAbstractCalculationEngine arabirimini uygulayarak bu fonksiyonun değerini hesaplarız. MYTESTFUNC()  fonksiyonunu, parametresini 2 ile çarparak ve sonucu döndürerek hesaplarız. Yani, eğer parametresi 9 ise, 2 * 9 = 18 döndürecektir.
### **Örnek Kod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
