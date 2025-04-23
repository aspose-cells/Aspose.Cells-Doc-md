---
title: Çalışma Kitabı Yapısını Koruma Altına Alma ve Korumasız Yapma
type: docs
weight: 40
url: /tr/net/protect-and-unprotect-workbook-structure/
description: CSharp kodlarıyla Excel dosyalarının çalışma kitabı yapısını koruma altına alma ve korumasız yapma
---


{{% alert color="primary" %}}
Diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, çalışma sayfalarını ekleme, taşıma, silme veya gizleme işlemlerini yapmalarını engellemek ve çalışma sayfalarını yeniden adlandırmak için Excel çalışma kitabınızın yapısını bir şifre ile koruyabilirsiniz.
{{% /alert %}}


## **MS Excel'de Çalışma Kitabı Yapısını Koruma ve Kaldırma**

**![çalışma kitabı yapısını koruma ve kaldırma](protect-and-unprotect-workbook-structure.png)**

1. Tıklayın **İncele > Çalışma Kitabını Koru**.
1. **Şifre kutusuna** bir şifre girin.
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.


## **Aspose.Cell for .Net kullanarak Çalışma Kitabı Yapısını Koruma**
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Example-Protect-Workbook-Structure.cs" >}}

## **Aspose.Cell for .Net kullanarak Çalışma Kitabı Yapısını Kaldırma**
Aspose.Cells API ile çalışma kitabı yapısını korumak kolaydır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-Unprotect-Workbook-Structure.cs" >}}

{{% alert color="primary" %}}
Not: Doğru bir şifre gerekli.
{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
