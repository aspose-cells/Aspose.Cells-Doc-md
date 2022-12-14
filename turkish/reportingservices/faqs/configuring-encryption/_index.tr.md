---
title: Şifrelemeyi Yapılandırma
type: docs
weight: 40
url: /tr/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Raporlama Hizmetleri için Aspose.Cells, şifrelemeyi destekler ve şifrelenmiş Microsoft Excel dosyalarını işleyebilirsiniz.

{{% /alert %}} 
### **Şifreleme Türleri**
Raporlama Hizmetleri için Aspose.Cells, Excel dosyalarını dışa aktarırken şifrelemeyi destekler. Üç şifreleme türünü destekler:

- XOR
- ZAYIF ŞİFRELEME
- Microsoft Güçlü Kriptografik Sağlayıcı
### **Yapılandırma Bilgileri**
 Şifreleme için yapılandırma bilgileri var.**Aspose.Cells.ReportingServices.xml** dosya. Encryption değeri "kapalı" olarak ayarlandığında, Aspose.Cells.ReportingServices şifrelemeyi kapatır.

**xml**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Şifreleme "açık" olarak ayarlandığında, Aspose.Cells.ReportingServices şifrelemeyi açar.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Şifreleme bölümünde dört parametre vardır: RaporAdı, Parola, EncryptionType ve KeyLength.

- RaporAdı – Şifreleme ayarları gerektiren raporu ayarlar. Parametre boş olduğunda bir rapor aynı şifreleme yolunu kullanır.
- Parola – Parolayı ayarlar. Boş bırakılamaz.
- EncryptionType – Şifreleme türünü ayarlar. Boş bırakılamaz.
-  KeyLength – Anahtar uzunluğunu ayarlar. Boş bırakılamaz.

**xml**

{{< highlight "csharp" >}}

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
