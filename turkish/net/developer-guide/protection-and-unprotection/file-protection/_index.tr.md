---
title: Excel dosyalarını şifreleyin ve şifresini çözün
type: docs
weight: 10
url: /tr/net/encrypt-and-decrypt-excel-files/
description: C# kullanarak excel dosyaları nasıl şifrelenir ve şifreleri çözülür. Excel dosyalarını kilitleyin ve kilidini açın.
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemenizi ve parolayla korumanızı sağlar. Bir şifreleme hizmeti sağlayıcısı tarafından sağlanan algoritmaları veya farklı özelliklere sahip bir dizi şifreleme algoritması olan CSP'yi kullanır. Varsayılan CSP, "Office 97/2000 Uyumlu" veya "Zayıf Şifreleme (XOR)" şeklindedir. Uygun şifreleme anahtarı uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bitten fazlasını desteklemez. Bu, zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bit anahtar uzunluğu gerekir. Microsoft Windows, güçlü şifreleme türleri de sunan CSP'ler içerir, örneğin 'Microsoft Güçlü Şifreleme Sağlayıcı'. Size bir fikir vermesi için, bankaların İnternet Bankacılığı sistemleriyle bağlantıyı şifrelemek için kullandıkları 128 bit şifrelemedir.

Aspose.Cells, Microsoft Excel dosyalarını istediğiniz şifreleme türüyle şifrelemenizi ve parola korumanızı sağlar.

{{% /alert %}}

## **Microsoft Excel'i kullanma**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1.  itibaren**Aletler** menü, seç**Seçenekler**Bir iletişim kutusu görünecektir.
1.  seçin**Güvenlik** sekme.
1.  Bir şifre girin ve tıklayın**Gelişmiş**
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Excel dosyası Aspose.Cells ile şifreleniyor**

Aşağıdaki örnek, Aspose.Cells API kullanılarak bir excel dosyasının nasıl şifreleneceğini ve parolayla korunacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Seçeneği değiştirmek için Parola Belirtme**

 Aşağıdaki örnek, nasıl ayarlanacağını gösterir.**Değiştirilecek şifre** Microsoft Aspose.Cells API'i kullanan mevcut bir dosya için Excel seçeneği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Aspose.Cells ile Excel dosyasının şifresini çözme**
Parola korumalı excel dosyasını açmak ve aşağıdaki kodlar gibi Aspose.Cells API kullanarak şifresini çözmek çok önemlidir:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **ileri konular**
- [ODS dosyalarını şifreleyin ve şifresini çözün](/cells/tr/net/encrypt-and-decrypt-ods-files/)
- [Güçlü Şifreleme Türü Ayarlama](/cells/tr/net/setting-strong-encryption-type/)
- [Çalışma Kitabını Yazma Koruması Yaparken Yazarı Belirtin](/cells/tr/net/specify-author-while-write-protecting-workbook/)
- [Şifrelenmiş Dosyaların Parolasını Doğrulayın](/cells/tr/net/verify-password-of-encrypted-excel-and-ods-files/)

