---
title: StreamProvider ile HTML yü Kaydet
type: docs
weight: 120
url: /tr/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

Resimler ve şekiller içeren excel dosyalarının HTML dosyalarına dönüştürülmesi sırasında genellikle aşağıdaki iki sorunla karşılaşırız:
1. Excel dosyasını html olarak kaydederken görüntü ve şekilleri nereye kaydedeceğiz.
1. Varsayılan yolu beklenen yol ile değiştirin.

Bu makale, [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) özelliğini ayarlamak için [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arayüzünü uygulamanın nasıl başarılacağını açıklar. Bu arayüzü uygulayarak, HTML oluşturma sırasında oluşturulan kaynakları belirli konumlara veya bellek akışlarına kaydedebileceksiniz.

{{% /alert %}}

## Örnek Kod

Bu, [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) özelliğinin kullanımını gösteren ana kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Yukarıdaki kodun içinde kullanılan [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) arayüzünü uygulayan *ExportStreamProvider* sınıfının kodu aşağıda bulunmaktadır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

