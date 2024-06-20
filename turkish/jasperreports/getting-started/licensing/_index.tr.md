---
title: Lisanslama
type: docs
weight: 40
url: /tr/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports, [İndirme sayfasından](https://downloads.aspose.com/cells/jasperreports) ücretsiz, süresiz değerlendirme sürümü olarak mevcuttur. Ürünün değerlendirme ve lisanslı sürümleri aynı indirme dosyasıdır.

Değerlendirme sürümünden memnun kaldığınızda, [bir lisans satın alabilirsiniz](https://purchase.aspose.com/). Lisans şartlarını anladığınızdan ve kabul ettiğinizden emin olun.

Lisans, sipariş ödendiğinde sipariş sayfasından indirilebilir. Lisans, net metin, dijital olarak imzalanmış bir XML dosyasıdır. Lisans, müşteri adı, satın alınan ürün ve lisans türü gibi bilgileri içerir. Lisans dosyasının içeriğini değiştirmeyin: aksi takdirde lisans geçersiz hale gelir.

Bir lisansı uygulamanın iki yolu vardır:

- [setLicense'ı çağırın](/cells/tr/jasperreports/licensing/#call-setlicense)
- [applicationContext.xml'de bir dışa aktarıcı parametresi ayarlayın](/cells/tr/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Lisansı yükledikten sonra,

- [İşe yaradığını doğrulayın](/cells/tr/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **setLicense'ı çağırın**

{{% alert color="primary" %}}

Bu yöntem JasperReports ile kullanım için uygundur.

{{% /alert %}}

Lisansı bilgisayarınıza indirin ve uygun klasöre kopyalayın (örneğin uygulamanızın klasörü veya **JasperReports\lib** gibi).
Projeye aşağıdaki kodu ekleyin:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **applicationContext.xml'de lisansDosyası Dışa Aktarıcı Parametresini ayarlayın**

{{% alert color="primary" %}}

Bu yöntem JasperServer ile kullanım için uygundur.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Lisanstan emin olun**

Herhangi bir raporu XLS formatına dışa aktarın ve raporda bir değerlendirme mesajı bulunup bulunmadığını kontrol edin. Eğer bir değerlendirme mesajı yoksa, o zaman lisans düzgün bir şekilde çalışıyor demektir.

**Aspose.Cells for JasperReports, değerlendirme modunda bir değerlendirme çalışma sayfası takar** 

![todo:image_alt_text](licensing_1.png)

**Geçerli bir lisans olduğunda bir değerlendirme çalışma sayfası olmaz** 

![todo:image_alt_text](licensing_2.png)
