---
title: Güçlü Şifreleme Türü Ayarlama
type: docs
weight: 10
url: /tr/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010), elektronik tabloları şifrelemeye ve parola korumaya imkan tanır. Bu, bir Kripto Hizmet Sağlayıcısı tarafından sağlanan algoritmaları kullanır. Bir Kripto Hizmet Sağlayıcısı (veya KHS), farklı özelliklere sahip bir dizi kriptografik algoritmalardır. Varsayılan KHS, "Ofis 97/2000 Uyumlu'dur". Bu, bazı halka açık güvenlik sorunları olan bir KHS'dir. "Zayıf şifreleme (XOR)" veya "Ofis 97/2000 Uyumlu" şifreleme türleriyle korunan elektronik tablolar kolayca kırılabilir.

Bu sorunu aşmak için, Microsoft Excel tarafından sağlanan güçlü şifreleme türlerinden birini kullanın. Şifreleme türünü en güçlü kullanılabilir KHS'ye değiştirebilirsiniz. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcı'.

Aspose.Cells API'sı kullanarak güçlü şifreleme türü ile Excel dosyalarını da şifreleyebilir ve parola koruyabilirsiniz.

{{% /alert %}}

## **Microsoft Excel'de Şifreleme Uygulama**

Microsoft Excel'de dosya şifrelemeyi uygulamak için (örneğin 2007):

1. **Araçlar** menüsünden **Seçenekler**'i seçin.
1. **Güvenlik** sekmesini seçin.
1. **Açmak için Parola** alanı için bir değer girin.
1. **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

   **Microsoft Excel'de şifreleme ayarlama**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Aspose.Cells ile Şifreleme Uygulama**

Aşağıdaki kod örneği, bir dosyaya güçlü şifreleme uygular ve bir parola belirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
