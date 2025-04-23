---
title: Akıllı İşaretleri Biçimlendirme
type: docs
weight: 20
url: /tr/net/formatting-smart-markers/
---

## **Stil Özniteliğini Kopyala**
Bazı durumlarda, akıllı işaretleri kullanırken, içinde akıllı işaret etiketlerini taşıyan hücrenin stilini kopyalamak isteyebilirsiniz. Bu amaçla, akıllı işaretlerin etiketlerinin CopyStyle özniteliğini kullanabilirsiniz.
### **Hücrelerden Akıllı İmlerle Stilleri Kopyalama**
Bu örnek, A2 ve B2 hücrelerinde iki işaretçi bulunan basit bir şablon Microsoft Excel dosyasını kullanır. B2 hücresine yapıştırılan işaretçi CopyStyle özelliğini kullanırken, A2 hücresindeki işaretçi kullanmaz. Basit biçimlendirme uygulayın (örneğin, yazı tipi rengini **kırmızı** olarak ayarlayın ve hücre doldurma rengini **sarı** olarak ayarlayın).

Kod çalıştırıldığında, Aspose.Cells B sütunundaki tüm kayıtlara biçimlendirmeyi kopyalar ancak A sütunundaki biçimlendirmeyi korumaz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Özel Etiketler Ekleniyor**
### **Giriş**
Akıllı İmler'in gruplandırma veri özelliği kullanılırken bazen özelleştirilmiş kendi etiketlerinizi özet satıra eklemeniz gerekebilir. Ayrıca Sütun'un adını bu etiketle birleştirmek istersiniz, örn. "Siparişlerin Alt Toplamı". Aspose.Cells, özel etiketlerinizi Smart İmler içine yerleştirebilmeniz için Label ve LabelPosition özelliklerini sağlar, böylece gruplandırma verilerine özel etiketlerinizi ekleyebilirsiniz.
### **Akıllı İmler içinde Alt Toplam satırlarıyla birleştirmek için özel Etiketler eklemek**
Bu örnek, birkaç imleçli bir [veri dosyası](96927971.xlsx) ve [şablon dosyası](96927972.xlsx) kullanır. Kod çalıştırıldığında, Aspose.Cells gruplanmış veriler için özet satırlara bazı özel etiketler ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
