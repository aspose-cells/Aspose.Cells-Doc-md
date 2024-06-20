---
title: Dijital İmza Desteği
type: docs
weight: 70
url: /tr/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Bir dijital imza, bir çalışma kitabının geçerli olduğunu ve kimse tarafından değiştirilmediğinden emin olunmasını sağlar. Bir dijital imza eklemek, bir zarfı mühürlemek gibidir. Mühürlü bir zarf geldiğinde, içeriğiyle oynamayan birinin varlığına dair bir dereceye kadar güvenceye sahip olursunuz. 

Kişisel bir dijital imza oluşturabilirsiniz, Microsoft Selfcert.exe veya başka bir araç kullanarak veya bir dijital imza satın alabilirsiniz. Bir elektronik tabloya bir imza eklemek için, bir dijital imza oluşturduktan sonra imzanızı çalışma kitaplarınıza ekleyin. 

Aspose.Cells for Reporting Services dijital imzaları destekler. 

{{% /alert %}} 
### **Dijital İmzalarla Çalışma**
#### **Dijital İmzalar için Desteklenen Excel Formatları**
Aspose.Cells for Reporting Services, Excel 2007 ve ODS dosya biçimlerine dışa aktarırken dijital imzaları destekler.
#### **Dijital İmzaları Yaplandırma**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- DigitalSignature değeri off olarak ayarlandığında, Aspose.Cells for Reporting Services dijital imza işlevselliğini kapatır.
  Örneğin: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- DigitalSignature değeri on olduğunda, Aspose.Cells.ReportingServices dijital imza işlevselliğini açar.
  Örneğin: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Dijital İmza bölümünde dört parametre bulunmaktadır. Bunlar: 

- name - Bir dijital imzaya ihtiyaç duyan bir rapora işaret eder. Eğer parametre boş bırakılırsa, rapor, dijital imza için bir PFX dosyası kullanır.
- pfxDosyaAdı - PFX dosyasına işaret eder. Dosya adı tam bir dosya adı olmalıdır. Boş bir değere ayarlanamaz.
- pfxŞifre - Şifreyi ayarlar. Boş bırakılamaz.
- amaç - İmzanın amacını açıklar. Boş olabilir.
  Örneğin: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
