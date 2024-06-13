---
title: 数字签名
type: docs
weight: 50
url: /zh/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services 支持在导出 Microsoft Excel 2007 文件或 ODS 文件时使用数字签名。我们有一些数字签名的配置信息可以在 **Aspose.Cells.ReportingServices.xml** 文件中设置。

当 DigitalSignature 的值为 **off** 时， Aspose.Cells for Reporting Services 关闭数字签名。

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

当 DigitalSignature 的值为 **on** 时， Aspose.Cells for Reporting Services 打开了数字签名。

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

数字签名段中有四个参数。它们是： 

- **名称**：表示需要数字签名的报告。当参数留空时，报告使用 PFX 文件进行数字签名。
- **pfx文件名**：指的是一个 PFX 文件。文件名应为完整的文件名（包括路径和文件扩展名）。不能留空。
- **pfx密码**：设置密码。不能为空。
- **目的**：签名用途的描述。可以留空。

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
