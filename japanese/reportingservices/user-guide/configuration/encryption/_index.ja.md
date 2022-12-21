---
title: 暗号化
type: docs
weight: 40
url: /ja/reportingservices/encryption/
---
Aspose.Cells for Reporting Services は、XOR、WEAK ENCRYPTION、および Microsoft Strong Cryptographic Provider の 3 種類の暗号化をサポートします。の暗号化構成情報を参照してください。**Aspose.Cells.ReportingServices.xml**ファイル。

 Encryption の値が**オフ**、Aspose.Cells for Reporting Services は、暗号化機能をオフにします。

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Encryption の値が**の上**, Aspose.Cells for Reporting Services は、暗号化をオンにします。

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

暗号化セクションには 4 つのパラメーターがあります。

- **レポート名**暗号化が必要なレポートを指します。パラメータを空白のままにすると、すべてのレポートで同じ暗号化方式が使用されます。
- **パスワード**パスワードを設定します。空白にすることはできません。
- **暗号化の種類**暗号化タイプを設定します。空白にすることはできません。
- **キーの長さ**キーの長さを設定します。空白にすることはできません。

{{< highlight "java" >}}

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
