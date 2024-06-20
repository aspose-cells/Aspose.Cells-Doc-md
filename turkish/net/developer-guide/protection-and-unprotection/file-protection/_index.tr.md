---
title: Excel Dosyalarını Şifrelemek ve Çözmek
type: docs
weight: 10
url: /tr/net/encrypt-and-decrypt-excel-files/
description: C# Kullanarak Excel dosyalarını nasıl şifreleyip çözeceğinizi anlatır. Excel dosyalarını kilitleme ve açma.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemeye ve parola koruması yapmaya olanak tanır. Bir şifreleme hizmet sağlayıcısı tarafından sağlanan algoritmalar, yani bir dizi farklı özelliklere sahip şifreleme algoritmaları kullanır. Varsayılan CSP 'Ofis 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' dur. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bit'ten fazlasını desteklemez. Bu zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'ler içerir. Size bir fikir vermek gerekirse, 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandığı şeydir.

Aspose.Cells, istediğiniz şifreleme türüyle Microsoft Excel dosyalarını şifrelemeye ve parola korumaya olanak tanır.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin. Bir iletişim kutusu görünecektir.
1. **Güvenlik** sekmesini seçin.
1. Bir parola girin ve **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile Excel dosyasının Şifrelenmesi**

Aşağıdaki örnek, Aspose.Cells API'sını kullanarak bir Excel dosyasını şifrelemek ve parolayla korumak için nasıl yapılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Değiştirilecek Parolayı Belirtme Seçeneği**

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells API'sını kullanarak **Değiştirilecek Parolayı** Microsoft Excel seçeneğini nasıl ayarlayacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Aspose.Cells ile Excel dosyasının şifresini çözme**
Koruma altındaki Excel dosyasını açmak ve Aspose.Cells API'sını kullanarak aşağıdaki kodları kullanarak şifresini çözmek çok kolaydır:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Gelişmiş Konular**
- [ODS dosyalarını şifreleme ve şifresini çözme](/cells/tr/net/encrypt-and-decrypt-ods-files/)
- [Güçlü Şifreleme Türü Belirleme](/cells/tr/net/setting-strong-encryption-type/)
- [Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme](/cells/tr/net/specify-author-while-write-protecting-workbook/)
- [Şifreli Dosyaların Parolasını Doğrulama](/cells/tr/net/verify-password-of-encrypted-excel-and-ods-files/)

