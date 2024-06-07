---
title: 数字签名
type: docs
weight: 50
url: /zh/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services支持在导出Microsoft Excel 2007文件或ODS文件时进行数字签名。我们为数字签名提供了一些配置信息，可在**Aspose.Cells.ReportingServices.xml**文件中进行设置。

当数字签名的值为**off**时，Aspose.Cells for Reporting Services将关闭数字签名。

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

当数字签名的值为**on**时，Aspose.Cells for Reporting Services将启用数字签名。

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

数字签名部分有四个参数，分别是: 

- **name**：表示需要数字签名的报告。当参数留空时，报告将使用PFX文件进行数字签名。
- **pfxFilename**：指向PFX文件。文件名应该是完整的带路径和文件扩展名的文件名。不能为空。
- **pfxPwd**：设置密码。不能为空。
- **purpose**：对签名用途的描述。可以留空。

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
