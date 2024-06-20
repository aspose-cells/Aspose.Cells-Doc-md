---
title: Şifreleme Yapılandırma
type: docs
weight: 40
url: /tr/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services şifrelemeyi destekler ve şifreli Microsoft Excel dosyalarını oluşturabilirsiniz. 

{{% /alert %}} 
### **Şifreleme Türleri**
Aspose.Cells for Reporting Services, Excel dosyalarını dışa aktarırken şifrelemeyi destekler. Üç farklı şifreleme türünü destekler:

- XOR
- ZAYIF ŞİFRELEME
- Microsoft Güçlü Kriptografik Sağlayıcı
### **Yapılandırma Bilgisi**
**Aspose.Cells.ReportingServices.xml** dosyasında şifreleme için yapılandırma bilgileri bulunmaktadır. Şifreleme değeri "kapalı" olarak ayarlandığında, Aspose.Cells.ReportingServices şifrelemeyi devre dışı bırakır.

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Şifreleme "açık" olarak ayarlandığında, Aspose.Cells.ReportingServices şifrelemeyi etkinleştirir.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Şifreleme bölümünde dört parametre bulunmaktadır: ReportName, Password, EncryptionType ve KeyLength.

- ReportName – Şifreleme ayarlarına ihtiyaç duyan raporu ayarlar. Bir rapor parametresi boş olduğunda aynı şifreleme yolunu kullanır.
- Password – Şifreyi ayarlar. Boş bırakılamaz.
- EncryptionType – Şifreleme türünü ayarlar. Boş bırakılamaz.
- KeyLength – Anahtar uzunluğunu ayarlar. Boş bırakılamaz. 

**XML**

{{< highlight csharp >}}

 <Encryption value="on">

<Report name="Test" >

<Password value="12345"/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

<Report name="" >

<Password value="123456"/>

<EncryptionType value="XOR"/>

<KeyLength value="128"/>

</Report>

</Encryption>



{{< /highlight >}}
