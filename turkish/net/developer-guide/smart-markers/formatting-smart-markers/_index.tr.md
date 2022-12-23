---
title: Akıllı İşaretçileri Biçimlendirme
type: docs
weight: 20
url: /tr/net/formatting-smart-markers/
---
## **Stil Niteliğini Kopyala**
Bazen, akıllı işaretleyicileri kullanırken, akıllı işaretleyici etiketlerini içeren hücrenin stilini kopyalamak istersiniz. Bu amaçla akıllı işaretleyici etiketlerinin CopyStyle özelliğini kullanabilirsiniz.
### **Akıllı İşaretleyicilerle Cells'den Stilleri Kopyalama**
 Bu örnek, A2 ve B2 hücrelerinde iki işaretçi bulunan basit bir şablon Microsoft Excel dosyası kullanır. B2 hücresine yapıştırılan işaretçi CopyStyle özniteliğini kullanırken A2 hücresindeki işaretçi kullanmaz. Basit biçimlendirme uygulayın (örneğin, yazı tipi rengini şu şekilde ayarlayın:**kırmızı** ve hücre dolgu rengini şu şekilde ayarlayın:**sarı**).

Aspose.Cells, kodu çalıştırırken biçimlendirmeyi B sütunundaki tüm kayıtlara kopyalar ancak biçimlendirmeyi A sütununda tutmaz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Özel Etiketler Ekleme**
### **Giriş**
Smart Markers'ın veri gruplandırma özelliği ile çalışırken bazen kendi özel etiketlerinizi özet satırına eklemeniz gerekir. Ayrıca, Sütun adını bu Etiketle birleştirmek istiyorsunuz, örneğin "Siparişlerin Alt Toplamı". Aspose.Cells size Etiket ve EtiketPozisyonu özelliklerini sağlar, böylece gruplama verilerinde Alt Toplam satırlarıyla birleştirirken özel etiketlerinizi Akıllı İşaretleyicilere yerleştirebilirsiniz.
### **Akıllı İşaretleyicilerdeki Ara Toplam satırlarıyla birleştirmek için özel Etiketler ekleme**
Bu örnek bir[veri dosyası](96927971.xlsx) ve bir[şablon dosyası](96927972.xlsx) hücrelerde birkaç belirteç ile. Aspose.Cells kodu yürütürken, gruplanmış veriler için özet satırlarına bazı özel etiketler ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
