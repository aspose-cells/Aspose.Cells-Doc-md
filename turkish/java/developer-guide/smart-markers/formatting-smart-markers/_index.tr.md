---
title: Akıllı İşaretleri Biçimlendirme
type: docs
weight: 20
url: /tr/java/formatting-smart-markers/
---

## **Stil Özniteliğini Kopyala**
Bazı durumlarda, akıllı işaretleri kullanırken, içinde akıllı işaret etiketlerini taşıyan hücrenin stilini kopyalamak isteyebilirsiniz. Bu amaçla, akıllı işaretlerin etiketlerinin CopyStyle özniteliğini kullanabilirsiniz.
### **Hücrelerden Akıllı İmlerle Stilleri Kopyalama**
Bu örnek, A2 ve B2 hücrelerinde iki işaretçi bulunan basit bir şablon Microsoft Excel dosyasını kullanır. B2 hücresine yapıştırılan işaretçi CopyStyle özelliğini kullanırken, A2 hücresindeki işaretçi kullanmaz. Basit biçimlendirme uygulayın (örneğin, yazı tipi rengini **kırmızı** olarak ayarlayın ve hücre doldurma rengini **sarı** olarak ayarlayın).

Bu örnek, hücrelerde birkaç işaretçisini içeren [şablon dosyasını](template1.xlsx) kullanır. Kodu yürütürken, Aspose.Cells, B sütunundaki tüm kayıtlara biçimlendirmeyi kopyalar, ancak A sütununda biçimlendirmeyi korumaz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-UsingCopyStyleAttribute-1.java" >}}


## **Özel Etiketler Ekleniyor**
### **Giriş**
Akıllı İmler'in gruplandırma veri özelliği kullanılırken bazen özelleştirilmiş kendi etiketlerinizi özet satıra eklemeniz gerekebilir. Ayrıca Sütun'un adını bu etiketle birleştirmek istersiniz, örn. "Siparişlerin Alt Toplamı". Aspose.Cells, özel etiketlerinizi Smart İmler içine yerleştirebilmeniz için Label ve LabelPosition özelliklerini sağlar, böylece gruplandırma verilerine özel etiketlerinizi ekleyebilirsiniz.
### **Akıllı İmler içinde Alt Toplam satırlarıyla birleştirmek için özel Etiketler eklemek**
Bu örnek, hücrelerde birkaç işaretçisini içeren [şablon dosyasını](template.xlsx) kullanır. Kodu yürütürken, Aspose.Cells, gruplandırılmış veriler için özet satırlara bazı özel etiketler ekler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-SmartMarkers-AddCustomLabels-1.java" >}}
