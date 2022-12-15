---
title: şifreleme
type: docs
weight: 40
url: /tr/reportingservices/encryption/
---
 Aspose.Cells for Reporting Services, üç tür şifrelemeyi destekler: XOR, WEAK ENCRYPTION ve Microsoft Strong Cryptographic Provider. bölümündeki şifreleme yapılandırma bilgilerine bakın.**Aspose.Cells.ReportingServices.xml** dosya.

 Şifreleme değeri şu olduğunda**kapalı**, Aspose.Cells for Reporting Services şifreleme özelliklerini kapatır.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Şifreleme değeri şu olduğunda**üzerinde**, Aspose.Cells for Reporting Services şifrelemeyi açar.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Şifreleme bölümünde dört parametre vardır:

- **Rapor Adı**: şifreleme gerektiren bir rapora işaret eder. Parametre boş bırakılırsa tüm raporlar aynı şifreleme yöntemini kullanır.
- **Şifre**parolayı ayarlar. Boş bırakılamaz.
- **Şifreleme tipi**: bir şifreleme türü ayarlar. Boş bırakılamaz.
- **Anahtar Uzunluğu**: anahtar uzunluğunu ayarlar. Boş bırakılamaz.

{{< highlight "java" >}}

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
