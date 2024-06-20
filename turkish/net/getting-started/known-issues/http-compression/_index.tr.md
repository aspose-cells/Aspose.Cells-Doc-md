---
title: HTTP Sıkıştırma
type: docs
weight: 10
url: /tr/net/http-compression/
---

## **HTTP Sıkıştırma problemi**
Bazı kullanıcılar, IIS'de HTTP Sıkıştırmasını yapılandırırlarsa, üretilen dosyaları istemci tarayıcılara gönderirken hatalarla karşılaştıklarını bildirmektedir.
### **Açıklama**
Tarayıcının dosyayı açmasını zorlamak için **"Content-disposition", "inline; filename=test.xls"** başlığını kullanırız ve dosyanın **Farklı Kaydet** ile açılmasını zorlamak ve Microsoft Excel'in dosyayı açmasını sağlamak için **"Content-disposition", "attachment; filename=test.xls"** başlığını kullanırız. Ancak bazı istisnaların olduğunu bilmek önemlidir.
### **Özel Durumlar**
Aşağıdaki kodu kullanarak, bunun Aspose'un bir hatası olmadığını doğrulayabilirsiniz.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Çözümler**
Bu sorunu çözmek için aşağıdaki çözümlerden birini kullanabilirsiniz:

- Aspose.Cells çağrısı içeren belirtilen ASP.NET dosyalarını sıkıştırılmamış olan başka bir klasöre taşıyın.
- Dinamik içerik için HTTP Sıkıştırmasını devre dışı bırakın.
- Oluşturulan dosyayı sunucunuzda kaydedin ve kullanıcılarınıza bir bağlantı sağlayın.

Eğer HTTP Sıkıştırmasını kullanmak istiyorsanız, lütfen IIS sıkıştırmayı etkinleştirdiğinizi bildiğinizde her zaman *OpenInBrowser* seçeneği yerine *OpenInExcel* seçeneğini kullanın.
