---
title: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cells ile [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) yöntemini kullanarak VBA kod projenizi dijital olarak imzalayabilirsiniz. Excel dosyanızın sertifika ile dijital olarak imzalanıp imzalanmadığını kontrol etmek için lütfen aşağıdaki adımları izleyin.

- **Geliştirici** sekmesinden **Görsel Temel**'e tıklayarak **Görsel Temel Uygulamaları (IDE)**'ni açın.
- **Görsel Temel Uygulamaları (IDE)**'nin **Araçlar** > **Dijital İmzalar...**'ına tıklayın.

ve **Dijital İmza Formu**'nu göstererek belgenin sertifika ile dijital olarak imzalanıp imzalanmadığını gösterecektir.

{{% /alert %}} 

## **C# ile bir VBA Kod Projesini Sertifika ile Dijital Olarak İmzalama**

Aşağıdaki örnek kod, [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign) yöntemini nasıl kullanacağınızı göstermektedir. Örnek kodun girdi ve çıktı dosyaları aşağıda verilmiştir. Bu kodu test etmek için herhangi bir excel dosyası ve sertifika kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
