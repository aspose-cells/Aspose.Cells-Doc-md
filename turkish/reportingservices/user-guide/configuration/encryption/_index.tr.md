---
title: Şifreleme
type: docs
weight: 40
url: /tr/reportingservices/encryption/
---

Aspose.Cells for Reporting Services, XOR, ZAYIF ŞİFRELEME ve Microsoft Güçlü Kriptografik Sağlayıcı olmak üzere üç çeşit şifrelemeyi destekler. Şifreleme yapılandırma bilgileri için **Aspose.Cells.ReportingServices.xml** dosyasına bakınız.

Şifreleme değeri **kapalı** olduğunda, Aspose.Cells for Reporting Services şifreleme özelliklerini kapatır.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Şifreleme değeri **açık** olduğunda, Aspose.Cells for Reporting Services şifrelemeyi açar.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Şifreleme bölümünde dört parametre bulunmaktadır:

- **RaporAdı**: şifreleme gerektiren bir raporu işaret eder. Parametre boş bırakıldığında, tüm raporlar aynı şifreleme yöntemini kullanır.
- **Parola**: parolayı ayarlar. Boş olamaz.
- **Şifreleme Türü**: şifreleme türünü ayarlar. Boş olamaz.
- **Anahtar Uzunluğu**: anahtar uzunluğunu ayarlar. Boş olamaz.

{{< highlight java >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
