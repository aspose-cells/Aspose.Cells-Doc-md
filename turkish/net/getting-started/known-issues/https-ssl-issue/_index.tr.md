---
title: HTTPS SSL Sorunu
type: docs
weight: 20
url: /tr/net/https-ssl-issue/
---

## **HTTPS/SSL Sorunu**
Bazı kullanıcılar, Aspose.Cells ile oluşturulan Excel dosyalarını indirirken sorun yaşadıklarını bildirdiler. Kaydet iletişim kutusu açıldığında, dosya adı excel dosyasının adını içermez, Dosya Türü boştur.
### **Açıklama**
HTTP sıkıştırma sorununu çözmek için HTTP yanıt başlıklarını değiştirdik. Bu, dosyaları HTTPS/SSL aracılığıyla istemci tarayıcıya gönderirken sorun oluşturabilir.
### **Çözüm**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
