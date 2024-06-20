---
title: 暗号化
type: docs
weight: 40
url: /ja/reportingservices/encryption/
---

Aspose.Cells for Reporting ServicesはXOR、WEAK ENCRYPTION、およびMicrosoft Strong Cryptographic Providerの3種類の暗号化をサポートしています。**Aspose.Cells.ReportingServices.xml**ファイルでの暗号化の構成情報を参照してください。

Encryptionの値が**off**の場合、Aspose.Cells for Reporting Servicesでは暗号化機能をオフにします。

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Encryptionの値が**on**の場合、Aspose.Cells for Reporting Servicesでは暗号化をオンにします。

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

暗号化セクションには4つのパラメーターがあります。

- **ReportName**: 暗号化が必要なレポートを指します。パラメーターが空白の場合、すべてのレポートが同じ暗号化方法を使用します。
- **Password**: パスワードを設定します。空白にはできません。
- **EncryptionType**: 暗号化の種類を設定します。空白にできません。
- **KeyLength**: キーの長さを設定します。空白にできません。

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
