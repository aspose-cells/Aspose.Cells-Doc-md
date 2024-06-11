---
title: 数字签名支持
type: docs
weight: 70
url: /zh/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

数字签名提供了对工作簿有效性的保证，且没有人篡改过。添加数字签名类似于封装一个信封。如果一个信封被封好，你就有一定程度的保证没有人篡改其内容。 

您可以使用 Microsoft Selfcert.exe 或其他工具创建个人数字签名，或者购买数字签名。创建数字签名后，将其附加到工作簿即可对电子表格进行签名。 

Aspose.Cells for Reporting Services 支持数字签名。 

{{% /alert %}} 
### **数字签名操作**
#### **数字签名支持的 Excel 格式**
Aspose.Cells for Reporting Services 在导出到 Excel 2007 和 ODS 文件格式时支持数字签名。
#### **配置数字签名**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- 当 DigitalSignature 设置为 off 时，Aspose.Cells for Reporting Services 关闭数字签名功能。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- 当 DigitalSignature 的值为 on 时，Aspose.Cells.ReportingServices 打开数字签名功能。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

数字签名部分有四个参数，它们分别是： 

- name – 指向需要数字签名的报表。当参数为空时，报表使用 PFX 文件进行数字签名。
- pfxFilename – 指向 PFX 文件。文件名必须是完整的文件名，不能设置为空值。
- pfxPwd – 设置密码，不能留空。
- purpose – 解释签名的目的，可以为空。
  例如: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
