---
title: Dijital İmzalar
type: docs
weight: 50
url: /tr/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services, Microsoft Excel 2007 dosyalarını veya ODS dosyalarını dışa aktarırken dijital imzaları destekler. Dijital imzalar için yapılandırma bilgilerimiz var, bunlar **Aspose.Cells.ReportingServices.xml** dosyasında ayarlanabilir.

Dijital İmza değeri **kapalı** olduğunda, Aspose.Cells for Reporting Services dijital imzaları kapatır.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Dijital İmza değeri **açık** olduğunda, Aspose.Cells for Reporting Services dijital imzaları açar.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Dijital İmza bölümünde dört parametre bulunmaktadır. Bunlar: 

- **name**: dijital imza gerektiren bir raporu temsil eder. Parametre boş bırakıldığında, raporlar dijital imzalar için bir PFX dosyası kullanır.
- **pfxDosyaAdı**: bir PFX dosyasına referans verir. Dosya adı, tam yol ve dosya uzantısı dahil olmak üzere tamamen belirtilmiş bir dosya adı olmalıdır. Boş olmamalıdır.
- **pfxParola**: parolayı ayarlar. Boş olmamalıdır.
- **amaç**: imzanın ne için olduğunu açıklar. Boş olabilir.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
