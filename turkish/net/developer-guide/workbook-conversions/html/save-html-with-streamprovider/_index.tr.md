---
title: StreamProvider ile Html'yi Kaydet
type: docs
weight: 80
url: /tr/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

Görüntüler ve şekiller içeren excel alanlarını html dosyalarına dönüştürürken, genellikle aşağıdaki iki sorunla karşılaşırız:
1. Excel dosyasını html akışına kaydederken resimleri ve şekilleri nereye kaydetmeliyiz.
1. Varsayılan yolu, özel yol ile değiştirin.

 Bu makalede, nasıl uygulanacağı açıklanmaktadır[IStream Sağlayıcı](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) ayarlamak için arayüz[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) Emlak. Bu arayüzü uygulayarak, HTML oluşturma sırasında oluşturulan kaynakları belirli konumlarınıza veya bellek akışlarınıza kaydedebileceksiniz.

{{% /alert %}} 

 Bu, kullanımını gösteren ana koddur.[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)Emlak



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 İşte kodu*ExportStreamProvider* uygulayan sınıf[IStream Sağlayıcı](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)Yukarıdaki kodun içinde kullanılan arayüz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

