---
title: 数字签名支持
type: docs
weight: 70
url: /zh/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

数字签名可确保工作簿是有效的，且无人篡改。附加数字签名类似于封口信封。当密封信封到达时，您可以有一定程度的保证其内容未被人篡改。 

您可以使用Microsoft Selfcert.exe或其他工具创建个人数字签名，也可以购买数字签名。在创建数字签名后，将签名附加到您的工作簿。 

Aspose.Cells for Reporting Services支持数字签名。 

{{% /alert %}} 
### **数字签名操作**
#### **数字签名支持的Excel格式**
Aspose.Cells for Reporting Services在导出到Excel 2007和ODS文件格式时支持数字签名。
#### **配置数字签名**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- 当DigitalSignature设置为off时，Aspose.Cells for Reporting Services关闭数字签名功能。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- 当DigitalSignature值为on时，Aspose.Cells.ReportingServices开启数字签名功能。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

数字签名部分有四个参数。这些参数是： 

- name – 指向需要数字签名的报表。当参数为空白时，报表使用PFX文件进行数字签名。
- pfxFilename – 指向PFX文件。文件名必须是完整的文件名，不能设置为空白值。
- pfxPwd – 设置密码，不能留空。
- purpose – 解释签名的目的，可以为空。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
