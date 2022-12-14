---
title: Dijital imzalar
type: docs
weight: 50
url: /tr/reportingservices/digital-signatures/
---
 Raporlama Hizmetleri için Aspose.Cells, Microsoft Excel 2007 dosyalarını veya ODS dosyalarını dışa aktarırken dijital imzaları destekler. Dijital imzalar için ayarlanabilecek bazı yapılandırma bilgilerimiz var.**Aspose.Cells.ReportingServices.xml** dosya.

 DigitalSignature'ın değeri şu olduğunda:**kapalı**, Raporlama Hizmetleri için Aspose.Cells, dijital imzaları kapatır.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 DigitalSignature'ın değeri şu olduğunda:**üzerinde**, Raporlama Hizmetleri için Aspose.Cells, dijital imzaları açar.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature bölümünde dört parametre vardır. Bunlar:

- **isim**dijital imza gerektiren bir raporu temsil eder. Parametre boş bırakıldığında, raporlar dijital imzalar için bir PFX dosyası kullanır.
- **pfxDosyaadı**: bir PFX dosyasına atıfta bulunur. Dosya adı, yol ve dosya uzantısı ile tamamlanmış tam nitelikli bir dosya adı olmalıdır. Boş olmamalıdır.
- **pfxPwd**: şifreyi ayarlar. Boş olmamalıdır.
- **amaç**: imzanın ne için olduğunun açıklaması. boş olabilir

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
