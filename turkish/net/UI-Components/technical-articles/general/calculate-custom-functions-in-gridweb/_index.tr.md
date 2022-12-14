---
title: GridWeb'de Özel İşlevleri Hesaplayın
type: docs
weight: 90
url: /tr/net/calculate-custom-functions-in-gridweb/
---
## **Olası Kullanım Senaryoları**
Aspose.Cells.GridWeb, GridWeb.CustomCalculationEngine özelliğiyle özel işlevlerin hesaplanmasını destekler. Bu özellik, GridAbstractCalculationEngine arabiriminin örneğini alır. Lütfen GridAbstractCalculationEngine arayüzünü uygulayın ve özel fonksiyonlarınızı kendi mantığınızla hesaplayın.
## **GridWeb'de Özel İşlevleri Hesaplayın**
Aşağıdaki örnek kod, B3 hücresine MYTESTFUNC() adlı özel bir işlev ekler. Daha sonra GridAbstractCalculationEngine arayüzünü implemente ederek bu fonksiyonun değerini hesaplıyoruz. MYTESTFUNC() parametresini 2 ile çarpacak ve sonucu verecek şekilde hesaplıyoruz. Yani parametresi 9 ise, 2*9 = 18 döndürür.
### **Basit kod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
