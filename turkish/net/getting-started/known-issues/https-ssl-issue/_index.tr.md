---
title: HTTPS SSL Sorunu
type: docs
weight: 20
url: /tr/net/https-ssl-issue/
---
## **HTTPS/SSL Sorunu**
Bazı kullanıcılar, Aspose.Cells ile oluşturulan Excel dosyalarını indirmekte sorun yaşadıklarını bildirdi. Kaydet iletişim kutusu açıldığında, dosya adı excel dosyası yerine aspx sayfasının adını içeriyor ve Dosya Türü boş.
### **Açıklama**
HTTP sıkıştırma sorununu çözmek için HTTP yanıt başlıklarını değiştirdik. Bu, istemci tarayıcısına HTTPS/SSL aracılığıyla dosya gönderirken soruna neden olabilir.
### **Çözüm**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
