---
title: Adlandırılmış Aralık için Formül Ayarlama
type: docs
weight: 20
url: /tr/python-net/setting-formula-for-named-range/
---

## **Adlandırılmış Aralık için Formül Ayarlama**
Excel uygulamasına benzer şekilde, Aspose.Cells for Python via .NET API'leri, adlandırılmış bir aralık için formül belirleme özelliği olan [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to) özelliğini kullanır. Bu özelliğin birçok kullanışlı durumu olabilir, aşağıda birkaç örneği detaylandırılmıştır.
### **Basit Formül Ayarlama Adlandırılmış Aralık için**
Basit bir formül, aynı (veya farklı) çalışma sayfasındaki başka bir hücreye bir referans olabilir. Aşağıdaki örnek, yeni bir elektronik tablo oluşturur ve referansını başka bir hücreye ayarlar.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Karmaşık Formül Ayarlama Adlandırılmış Aralık için**
Karmaşık bir formül, bir dinamik aralık veya farklı çalışma sayfalarındaki birden çok hücreye yayılan bir formül olabilir. Aşağıdaki örnek, bir değerin konumuna bağlı olarak INDEX işlevini kullanarak dinamik bir aralık oluşturur.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Aşağıda, farklı çalışma sayfalarındaki 2 hücreden değerleri toplamak için adlandırılmış bir aralık kullanan başka bir örnek bulunmaktadır.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
