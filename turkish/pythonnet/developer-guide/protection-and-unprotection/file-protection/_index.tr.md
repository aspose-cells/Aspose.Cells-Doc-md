---
title: Excel Dosyalarını Şifrelemek ve Çözmek
type: docs
weight: 10
url: /tr/python-net/encrypt-and-decrypt-excel-files/
description: Python kullanarak excel dosyalarını şifrelemeyi ve şifresini çözmeyi nasıl yapılır. Excel dosyalarını kilitleme ve açma.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemeye ve parola koruması yapmaya olanak tanır. Bir şifreleme hizmet sağlayıcısı tarafından sağlanan algoritmalar, yani bir dizi farklı özelliklere sahip şifreleme algoritmaları kullanır. Varsayılan CSP 'Ofis 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' dur. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bit'ten fazlasını desteklemez. Bu zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'ler içerir. Size bir fikir vermek gerekirse, 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandığı şeydir.

Aspose.Cells for Python via .NET, Microsoft Excel dosyalarını istediğiniz şifreleme türüyle şifreleyip parola koruma özelliği eklemenize izin verir.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin. Bir iletişim kutusu görünecektir.
1. **Güvenlik** sekmesini seçin.
1. Bir parola girin ve **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile Excel dosyasının Şifrelenmesi**

Aşağıdaki örnek, Aspose.Cells for Python via .NET API kullanarak bir Excel dosyasını nasıl şifreleyip parola koruma altına alacağınızı gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Değiştirilecek Parolayı Belirtme Seçeneği**

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells for Python via .NET API kullanarak **Değiştirmek için Parola** Microsoft Excel seçeneğinin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}


## **Aspose.Cells ile Excel dosyasının şifresini çözme**
Şifre korumalı Excel dosyasını açmak ve şifreyi çözmek Aspose.Cells for Python via .NET API kullanılarak aşağıdaki kodlar ile çok kolaydır:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-Decrypt-Excel-File.py" >}}


## **Gelişmiş Konular**
- [ODS dosyalarını şifreleme ve şifresini çözme](/cells/tr/python-net/encrypt-and-decrypt-ods-files/)
- [Güçlü Şifreleme Türü Belirleme](/cells/tr/python-net/setting-strong-encryption-type/)
- [Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme](/cells/tr/python-net/specify-author-while-write-protecting-workbook/)
- [Şifreli Dosyaların Parolasını Doğrulama](/cells/tr/python-net/verify-password-of-encrypted-excel-and-ods-files/)

