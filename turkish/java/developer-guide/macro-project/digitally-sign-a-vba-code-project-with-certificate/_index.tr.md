---
title: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cells ile [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) yöntemini kullanarak VBA kod projenizi dijital olarak imzalayabilirsiniz. Excel dosyanızın sertifika ile dijital olarak imzalanıp imzalanmadığını kontrol etmek için lütfen aşağıdaki adımları izleyin.

- **Geliştirici** sekmesinden **Görsel Temel**'e tıklayarak **Görsel Temel Uygulamaları (IDE)**'ni açın.
- **Görsel Temel Uygulamaları IDE**'nin **Araçlar** > **Dijital İmzalar...**'ına tıklayın

ve **Dijital İmza Formu**'nu göstererek belgenin sertifika ile dijital olarak imzalanıp imzalanmadığını gösterecektir.

{{% /alert %}} 

## **C# ile bir VBA Kod Projesini Sertifika ile Dijital Olarak İmzalama**

Aşağıdaki örnek kod, [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-) yöntemini nasıl kullanacağınızı göstermektedir. İşte örnek kodun giriş ve çıkış dosyaları. Bu kodu test etmek için herhangi bir excel dosyası ve herhangi bir sertifikatı kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
{{< app/cells/assistant language="java" >}}
