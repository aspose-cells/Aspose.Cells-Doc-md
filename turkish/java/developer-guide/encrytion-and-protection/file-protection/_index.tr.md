---
title: Excel dosyalarını şifreleyin ve şifresini çözün
type: docs
weight: 40
url: /tr/java/encrypt-and-decrypt-excel-files/
description: Java kullanarak excel dosyalarını şifreleme ve şifrelerini çözme. Excel dosyalarını kilitleyin ve kilidini açın.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ), elektronik tablolarınızı şifrelemenizi / parola ile korumanızı sağlar. Crypto Service Provider tarafından sağlanan algoritmaları kullanır. Bir Kripto Hizmet Sağlayıcısı veya CSP, farklı özelliklere sahip bir dizi kriptografik algoritmadır. Varsayılan CSP "Office 97/2000 Uyumlu" veya "Hafta Şifreleme (XOR)" şeklindedir. Uygun bir şifreleme anahtarı uzunluğu seçmek de önemlidir. Kripto Hizmet Sağlayıcılarından bazıları 40 veya 56 bitten fazlasını desteklemez. Bu, zayıf bir şifreleme türü olarak kabul edilir. Ancak, güçlü şifreleme türü için minimum 128 bit anahtar uzunluğu gereklidir. Microsoft Windows, güçlü şifreleme türleri de sunan Kripto Hizmet Sağlayıcıları içerir, örneğin 'Microsoft Güçlü Şifreleme Sağlayıcı'. Bir fikir vermek gerekirse, 128 bit şifreleme, bankaların İnternet Bankacılığı Sistemleri ile bağlantıyı şifrelemek için kullandıkları şeydir. Aspose.Cells, excel dosyalarınızı istediğiniz şifreleme türü ile şifrelemenizi / şifre korumanızı sağlar.

{{% /alert %}}

## **MS Excel'i kullanma**

MS Excel'de (örn. MS Excel 2003), dosya şifreleme ayarlarını uygulamak için şunları deneyebilirsiniz:

-  itibaren**Aletler** menü, seç**Seçenekler** ve ardından**Güvenlik** sekme.
-  Giriş**açmak için şifre** ve tıklayın**Gelişmiş** buton.
- Şifreleme türünü seçin ve parolayı onaylayın.

![yapılacaklar:resim_alternatif_Metin](encrypting-excel-files_1.png)

**Şekil: Seçenekler iletişim kutusu**

![yapılacaklar:resim_alternatif_Metin](encrypting-excel-files_2.png)

**Şekil: Şifreleme Türü iletişim kutusu**

## **Excel dosyasını şifreleme**
Aşağıdaki örnek, Aspose.Cells API kullanarak bir excel dosyasını nasıl şifreleyebileceğinizi / parolayla koruyabileceğinizi gösterir.

### **Basit kod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Aspose.Cells ile Excel dosyasının şifresini çözme**
Parola korumalı excel dosyasını açmak ve aşağıdaki kodlar gibi Aspose.Cells API kullanarak şifresini çözmek çok önemlidir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



