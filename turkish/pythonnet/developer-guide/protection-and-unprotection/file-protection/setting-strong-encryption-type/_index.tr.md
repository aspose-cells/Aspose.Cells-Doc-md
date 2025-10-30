---
title: Güçlü Şifreleme Türü Ayarlama
type: docs
weight: 60
url: /tr/python-net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) elektronik tabloları şifrelemeye ve parola koruması sağlamaya olanak tanır. Bunun için bir Kripto Servis Sağlayıcı tarafından sağlanan algoritmayı kullanır. Kripto Servis Sağlayıcısı (veya CSP), farklı özelliklere sahip bir dizi kriptografik algoritmadır. Varsayılan CSP 'Office 97/2000 Uyumlu'dur. Bu, bazı kamuya bilinen güvenlik sorunları olan bir CSP'dir. 'Zayıf şifreleme (XOR)' veya 'Office 97/2000 Uyumlu' şifreleme türleriyle korunan elektronik tablolar kolayca kırılabilir.

Bu sorunu aşmak için Microsoft Excel tarafından sağlanan güçlü şifreleme türlerinden birini kullanın. Şifreleme türünü en güçlü CSP'ye değiştirebilirsiniz. Güçlü şifreleme için en az 128 bitlik bir anahtar uzunluğu gereklidir, örneğin, 'Microsoft Güçlü Kriptografik Sağlayıcı'.

Ayrıca, güçlü şifreleme türü kullanarak Excel dosyalarını da şifreleyebilir ve parola koruma altına alabilirsiniz Aspose.Cells for Python via .NET API’si ile.

{{% /alert %}} 

## **Microsoft Excel'de Şifreleme Uygulama**
Microsoft Excel'de dosya şifrelemeyi uygulamak için (örneğin 2007):

1. **Araçlar** menüsünden **Seçenekler**'i seçin.
1. **Güvenlik** sekmesini seçin.
1. **Açmak için Parola** alanı için bir değer girin.
1. **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells ile Şifreleme Uygulama**
Aşağıdaki kod örnekleri bir dosyaya güçlü şifreleme uygular ve bir şifre ayarlar.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SettingStrongEncryptionType-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
