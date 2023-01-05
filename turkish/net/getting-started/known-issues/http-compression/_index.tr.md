---
title: HTTP Sıkıştırma
type: docs
weight: 10
url: /tr/net/http-compression/
---
## **HTTP Sıkıştırma sorunu**
Bazı kullanıcılar, IIS'de HTTP Sıkıştırmayı yapılandırırlarsa, oluşturulan dosyaları istemci tarayıcılara gönderirken hatalar bulduklarını bildirir.
### **Açıklama**
 Kullanırız**"Content-disposition", "satır içi; dosyaadı=test.xls"** tarayıcıyı dosyayı açmaya zorlamak için başlık ve**"İçerik düzenlemesi", "ek; dosyaadı=test.xls"** tarayıcıyı açmaya zorlamak için başlık**Farklı kaydet** iletişim kutusunu açın ve dosyayı açmak için Microsoft Excel'i kullanın. Ancak, var olan bazı istisnalar vardır.
### **İstisnalar**
Bunun bir Aspose hatası OLMADIĞINI doğrulamak için aşağıdaki kodu kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Çözümler**
Bu sorunu çözmek için aşağıdaki geçici çözümlerden birini kullanabilirsiniz:

- Belirtilen ASP.NET dosyalarını (Aspose.Cells'i çağıran kodu içeren) sıkıştırılmamış başka bir klasöre taşıyın.
- Dinamik içerik için HTTP Sıkıştırmasını devre dışı bırakın.
- Oluşturulan dosyayı sunucunuza kaydedin ve kullanıcılarınıza bir bağlantı sağlayın.

 HTTP Sıkıştırmasını kullanmak istiyorsanız, lütfen her zaman kullanın*OpenInExcel* yerine seçenek*Tarayıcıda aç* seçeneği, IIS sıkıştırmasını etkinleştirdiğinizi bildiğinizde.
