---
title: Güçlü Şifreleme Türü Ayarlama
type: docs
weight: 60
url: /tr/net/setting-strong-encryption-type/
---
{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010), elektronik tabloları şifrelemenizi ve parolayla korumanızı sağlar. Bir Kripto Hizmet Sağlayıcısı tarafından sağlanan algoritmaları kullanır. Bir Kripto Hizmet Sağlayıcısı (veya CSP), farklı özelliklere sahip bir dizi kriptografik algoritmadır. Varsayılan CSP "Office 97/2000 Uyumludur". Bu, genel olarak bilinen bazı güvenlik sorunları olan bir CSP'dir. "Zayıf şifreleme (XOR)" veya "Office 97/2000 Uyumlu" şifreleme türü ile korunan elektronik tablolar kolayca kırılabilir.

Bu sorunu aşmak için Microsoft Excel tarafından sağlanan güçlü şifreleme türlerinden birini kullanın. Şifreleme türünü mevcut en güçlü CSP olarak değiştirebilirsiniz. Güçlü şifreleme için minimum 128 bit anahtar uzunluğu gereklidir, örneğin 'Microsoft Güçlü Şifreleme Sağlayıcı'.

Ayrıca Aspose.Cells API'i kullanarak Excel dosyalarını güçlü şifreleme türüyle şifreleyebilir ve parola ile koruyabilirsiniz.

{{% /alert %}} 
## **Microsoft Excel ile Şifreleme Uygulamak**
Microsoft Excel'de (örneğin 2007) dosya şifrelemeyi uygulamak için:

1.  itibaren**Aletler** menü, seç**Seçenekler**.
1.  seçin**Güvenlik** sekme.
1.  için bir değer girin**açmak için şifre** alan.
1.  Tıklamak**Gelişmiş**.
1. Şifreleme türünü seçin ve parolayı onaylayın.
## **Aspose.Cells ile Şifreleme Uygulamak**
Aşağıdaki kod örnekleri, bir dosyaya güçlü şifreleme uygular ve bir parola belirler.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingStrongEncryptionType-1.cs" >}}
