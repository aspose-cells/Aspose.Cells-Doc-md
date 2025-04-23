---
title: HTML yi kaydederken CSS yi devre dışı bırak
type: docs
weight: 320
url: /tr/net/disable-css-while-saving-to-html/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı tek sayfalı HTML olarak kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülü olur ve HEAD bölümünde bulunur. Bu dosyayı bir e-posta içeriği/gövdesi olarak eklediğinizde, çoğu e-posta istemcisi CSS öğelerini kaldırır ve düzgün görüntüleme sağlar. Aspose.Cells 24.12 sürümü, CSS'i isteğe bağlı olarak devre dışı bırakma seçeneği getirir, böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. E-posta gövdesi olarak HTML kullanmak istiyorsanız, lütfen [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) özelliğini kullanın ve bunu **true** olarak ayarlayın.



## **CSS'yi devre dışı bırakırken HTML'ye kaydetme**

Aşağıdaki örnek kod, [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) özelliğinin kullanımını gösterir. 



## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
