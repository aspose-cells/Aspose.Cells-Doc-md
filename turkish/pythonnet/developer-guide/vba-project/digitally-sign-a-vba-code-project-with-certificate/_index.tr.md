---
title: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ile VBA kod projenizi dijital olarak imzalayabilirsiniz [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature) metodunu kullanarak. Lütfen, Excel dosyanızın dijital olarak imzalanıp imzalanmadığını kontrol etmek için bu adımları izleyin.

- **Geliştirici** sekmesinden **Görsel Temel**'e tıklayarak **Görsel Temel Uygulamaları (IDE)**'ni açın.
- **Görsel Temel Uygulamaları (IDE)**'nin **Araçlar** > **Dijital İmzalar...**'ına tıklayın.

ve **Dijital İmza Formu**'nu göstererek belgenin sertifika ile dijital olarak imzalanıp imzalanmadığını gösterecektir.

{{% /alert %}} 

## **Python'da VBA Kod Projesini Sertifika ile Dijital Olarak İmzala**

Aşağıdaki örnek kod, [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature) yöntemini nasıl kullanacağınızı göstermektedir. Örnek kodun girdi ve çıktı dosyaları aşağıda verilmiştir. Bu kodu test etmek için herhangi bir excel dosyası ve sertifika kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
