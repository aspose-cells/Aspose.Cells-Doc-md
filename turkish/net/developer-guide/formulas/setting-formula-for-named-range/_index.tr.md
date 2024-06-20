---
title: Adlandırılmış Aralık için Formül Ayarlama
type: docs
weight: 20
url: /tr/net/setting-formula-for-named-range/
---

## **Adlandırılmış Aralık için Formül Ayarlama**
Excel uygulaması gibi, Aspose.Cells API'leri, [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto) özelliğini kullanırken adlandırılmış bir aralık için formül belirtme yeteneği sağlar. Bu özelliğin çeşitli kullanılabilir senaryoları olabilir, bunlardan bazıları aşağıda detaylandırılmıştır.
### **Basit Formül Ayarlama Adlandırılmış Aralık için**
Basit bir formül, aynı (veya farklı) çalışma sayfasındaki başka bir hücreye bir referans olabilir. Aşağıdaki örnek, yeni bir elektronik tablo oluşturur ve referansını başka bir hücreye ayarlar.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Karmaşık Formül Ayarlama Adlandırılmış Aralık için**
Karmaşık bir formül, bir dinamik aralık veya farklı çalışma sayfalarındaki birden çok hücreye yayılan bir formül olabilir. Aşağıdaki örnek, bir değerin konumuna bağlı olarak INDEX işlevini kullanarak dinamik bir aralık oluşturur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Aşağıda, farklı çalışma sayfalarındaki 2 hücreden değerleri toplamak için adlandırılmış bir aralık kullanan başka bir örnek bulunmaktadır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
