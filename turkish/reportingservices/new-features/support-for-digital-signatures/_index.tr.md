---
title: Dijital İmza Desteği
type: docs
weight: 70
url: /tr/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

 Dijital imza, çalışma kitabının geçerli olduğunu ve kimsenin değiştirmediğini garanti eder. Dijital imza eklemek, bir zarfı mühürlemeye benzer. Bir zarf mühürlü olarak gelirse, içeriğinin kimsenin kurcalanmadığına dair bir dereceye kadar güvenceye sahip olursunuz.

 Microsoft Selfcert.exe veya başka bir aracı kullanarak kişisel bir dijital imza oluşturabilir veya bir dijital imza satın alabilirsiniz. Bir elektronik tabloyu imzalamak için, dijital bir imza oluşturduktan sonra çalışma kitaplarınıza bir imza ekleyin.

 Aspose.Cells for Reporting Services dijital imzaları destekler.

{{% /alert %}} 
### **Dijital İmzalarla Çalışma**
#### **Dijital İmzalar için Desteklenen Excel Formatları**
Aspose.Cells for Reporting Services, Excel 2007 ve ODS dosya biçimlerine dışa aktarırken dijital imzaları destekler.
#### **Dijital İmzaları Yapılandırma**
 bu**Aspose.Cells.ReportingServices.xml** dosyası, bir dijital imzanın yapılandırma bilgilerini ve metnini tutar.<DigitalSignature> etiket:

- DigitalSignature kapalı olarak ayarlandığında, Aspose.Cells for Reporting Services, dijital imza işlevini kapatır.
 Örneğin:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- DigitalSignature değeri açık olduğunda, Aspose.Cells.ReportingServices, dijital imza işlevselliğini açar.
 Örneğin:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature bölümünde dört adet parametre bulunmaktadır. Bunlar :

- ad – Dijital imza gerektiren bir rapora işaret eder. Rapor, parametre boş olduğunda dijital imza için bir PFX dosyası kullanır.
- pfxFilename – PFX dosyasını işaret eder. Dosya adı tam bir dosya adı olmalıdır. Boş bir değere ayarlanamaz.
- pfxPwd – Parolayı ayarlar. Boş bırakılamaz.
- amaç – İmzanın amacını açıklar. Boş olabilir.
 Örneğin:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
