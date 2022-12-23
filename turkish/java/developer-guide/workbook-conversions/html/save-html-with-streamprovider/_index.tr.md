---
title: StreamProvider ile Html'yi Kaydet
type: docs
weight: 120
url: /tr/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

Resim ve şekiller içeren excel alanlarını html dosyalarına dönüştürürken, genellikle aşağıdaki iki sorunla karşılaşırız:
1. Excel dosyasını html akışına kaydederken resimleri ve şekilleri nereye kaydetmeliyiz.
1. Varsayılan yolu, özel yol ile değiştirin.

 Bu makalede, nasıl uygulanacağı açıklanmaktadır[**IStream Sağlayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) ayarlamak için arayüz[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) Emlak. Bu arabirimi uygulayarak, HTML üretimi sırasında oluşturulan kaynakları belirli konumlarınıza veya bellek akışlarınıza kaydedebileceksiniz.

{{% /alert %}}

## Basit kod

 Bu, kullanımını gösteren ana koddur.[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)Emlak

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 İşte kodu*ExportStreamProvider* uygulayan sınıf[**IStream Sağlayıcı**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)Yukarıdaki kodun içinde kullanılan arayüz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

