---
title: lisanslama
type: docs
weight: 40
url: /tr/jasperreports/licensing/
---
{{% alert color="primary" %}}

 JasperReports için Aspose.Cells numaralı telefondan ücretsiz, sınırsız süreli bir değerlendirme olarak edinilebilir.[indirme sayfası](https://downloads.aspose.com/cells/jasperreports). Ürünün değerlendirme ve lisanslı sürümleri aynı indirmedir.

 Değerlendirme sürümünden memnun olduğunuzda şunları yapabilirsiniz:[lisans satın al](https://purchase.aspose.com/). Lisans koşullarını anladığınızdan ve kabul ettiğinizden emin olun.

Lisans, sipariş ödendiğinde sipariş sayfasından indirilebilir. Lisans, açık metinli, dijital olarak imzalanmış bir XML dosyasıdır. Lisans, müşteri adı, satın alınan ürün ve lisans türü gibi bilgileri içerir. Lisans dosyasının içeriğini değiştirmeyin: bunu yapmak, lisansı geçersiz kılar.

Lisans başvurusu yapmanın iki yolu vardır:

- [setLicense'i arayın](/cells/tr/jasperreports/licensing/#call-setlicense)
- [applicationContext.xml'de bir dışa aktarıcı parametresi ayarlayın](/cells/tr/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Lisansı yükledikten sonra,

- [Çalıştığını doğrulayın](/cells/tr/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **setLicense'i arayın**

{{% alert color="primary" %}}

Bu yöntem, JasperReports ile kullanım için geçerlidir.

{{% /alert %}}

Lisansı bilgisayarınıza indirin ve uygun klasöre kopyalayın (örneğin, uygulamanızın klasörü veya**JasperReports\lib**).
Aşağıdaki kodu projenize ekleyin:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **applicationContext.xml'de licenseFile Exporter Parametresini ayarlayın**

{{% alert color="primary" %}}

Bu yöntem, JasperServer ile kullanım için geçerlidir.

{{% /alert %}}

1.  Lisansı bilgisayarınıza indirin ve kopyalayın.**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** klasör, nerede**\<Yükleme Dizini>** JasperServer kurulum dizini anlamına gelir.
1.  bulun**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** dosyasını açın ve aşağıdaki satırları ekleyin:

**xml**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Lisans Çalışmalarını Doğrulayın**

Herhangi bir raporu XLS formatına aktarın ve raporun bir değerlendirme mesajı içerip içermediğini kontrol edin. Değerlendirme mesajı yoksa, lisans düzgün çalışıyor demektir.

**JasperReports için Aspose.Cells, değerlendirme modunda bir değerlendirme çalışma sayfası ekler** 

![yapılacaklar:resim_alternatif_Metin](licensing_1.png)

**Geçerli bir lisans olduğunda değerlendirme çalışma sayfası yoktur** 

![yapılacaklar:resim_alternatif_Metin](licensing_2.png)
