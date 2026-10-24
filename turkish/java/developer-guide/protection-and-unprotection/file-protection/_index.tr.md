---
title: Excel Dosyalarını Şifrelemek ve Çözmek
type: docs
weight: 40
url: /tr/java/encrypt-and-decrypt-excel-files/
description: Java kullanarak excel dosyalarını şifreleme ve şifresini çözme nasıl yapılır. Excel dosyalarını kilitleme ve kilidini açma.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365 ), elektronik tablolarınızı şifreleme / parola koruma imkanı sunar. Bu, Cryptographic Service Provider tarafından sağlanan algoritmaları kullanır. Cryptographic Service Provider veya CSP, farklı özelliklere sahip bir dizi şifreleme algoritmasıdır. Varsayılan CSP "Office 97/2000 Uyumlu" veya "Hafta Şifreleme (XOR)"'dir. Ayrıca uygun bir şifreleme anahtarı uzunluğunu seçmek de önemlidir. Bazı Cryptographic Service Provider'lar 40 veya 56 biti aşmayan şifreleme tiplerini desteklemez. Bu, zayıf bir şifreleme türü olarak kabul edilir. Ancak, güçlü şifreleme türü için, minimum 128 bitlik bir anahtar uzunluğu gereklidir. Ayrıca Microsoft Windows, örneğin,'Microsoft Strong Cryptographic Provider' gibi güçlü şifreleme türlerini sunan Cryptographic Service Provider'lar içerir. Bir fikir vermek gerekirse, 128 bit şifreleme, bankaların İnternet Bankacılık Sistemleri ile bağlantıyı şifrelemek için kullandığı şeydir. Aspose.Cells, istediğiniz şifreleme türüyle excel dosyalarını şifrelemenize / parola korumanıza imkan tanır.

{{% /alert %}}

## **MS Excel Kullanarak**

MS Excel'de (örneğin MS Excel 2003), dosya şifreleme ayarlarını gerçekleştirmek için şunları deneyebilirsiniz:

- **Araçlar** menüsünden **Seçenekler**'i seçin ve ardından **Güvenlik** sekmesini seçin.
- **Açmak için Şifre**'yi girin ve **Gelişmiş** düğmesine tıklayın.
- Şifreleme türünü seçin ve şifreyi doğrulayın.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Şekil: Seçenekler iletişim kutusu**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Şekil: Şifreleme Türü iletişim kutusu**

## **Excel dosyası şifreleme**
Aşağıdaki örnek, Aspose.Cells API'sını kullanarak bir Excel dosyasını şifrelemenin / parolayla korumanın nasıl yapılabileceğini göstermektedir.

### **Örnek Kod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Aspose.Cells ile Excel dosyasının şifresini çözme**
Koruma altındaki Excel dosyasını açmak ve Aspose.Cells API'sını kullanarak aşağıdaki kodları kullanarak şifresini çözmek çok kolaydır:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



{{< app/cells/assistant language="java" >}}
