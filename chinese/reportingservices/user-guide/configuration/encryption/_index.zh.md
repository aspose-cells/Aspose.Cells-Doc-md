---
title: 加密
type: docs
weight: 40
url: /zh/reportingservices/encryption/
---

Aspose.Cells for Reporting Services支持三种加密形式：XOR、WEAK ENCRYPTION和Microsoft Strong Cryptographic Provider。请查看**Aspose.Cells.ReportingServices.xml**文件中的加密配置信息。

当加密的值为**off**时，Aspose.Cells for Reporting Services将关闭加密功能。

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

当加密的值为**on**时，Aspose.Cells for Reporting Services将启用加密。

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

加密部分有四个参数:

- **ReportName**：指向需要加密的报告。如果参数留空，则所有报告使用相同的加密方法。
- **Password**：设置密码。不能为空。
- **EncryptionType**：设置加密类型。不能为空。
- **KeyLength**：设置密钥长度。不能为空。

{{< highlight java >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
