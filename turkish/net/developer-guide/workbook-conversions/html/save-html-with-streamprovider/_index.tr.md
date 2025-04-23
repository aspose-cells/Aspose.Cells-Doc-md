---
title: StreamProvider ile HTML yü Kaydet
type: docs
weight: 80
url: /tr/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

Resimler ve şekiller içeren excel dosyalarını html dosyalarına dönüştürdüğümüzde, genellikle aşağıdaki iki sorunla karşılaşırız:
1. Excel dosyasını html olarak kaydederken görüntü ve şekilleri nereye kaydedeceğiz.
1. Varsayılan yolu beklenen yol ile değiştirin.

Bu makale, [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arayüzünü [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) özelliğini ayarlamak için nasıl uygulayacağınızı açıklar. Bu arayüzü uygulayarak, HTML oluşturma sırasında oluşturulan kaynakları belirli konumlara veya bellek akışlarına kaydedebilirsiniz.

{{% /alert %}} 

Bu, [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) özelliğini kullanmanın ana kodudur.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Aşağıda, yukarıdaki kod içerisinde kullanılan [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) arayüzünü uygulayan *ExportStreamProvider* sınıfının kodu bulunmaktadır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}
