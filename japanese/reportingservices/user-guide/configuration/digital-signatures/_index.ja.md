---
title: デジタル署名
type: docs
weight: 50
url: /ja/reportingservices/digital-signatures/
---

Microsoft Excel 2007ファイルまたはODSファイルをエクスポートする際、Aspose.Cells for Reporting Servicesはデジタル署名をサポートしています。デジタル署名の構成情報は**Aspose.Cells.ReportingServices.xml**ファイルで設定できます。

DigitalSignatureの値が**off**の場合、Aspose.Cells for Reporting Servicesではデジタル署名をオフにします。

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

DigitalSignatureの値が**on**の場合、Aspose.Cells for Reporting Servicesではデジタル署名をオンにします。

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

DigitalSignatureセクションには4つのパラメーターがあります。これらは次のとおりです。 

- **name**: デジタル署名が必要なレポートを表します。パラメーターが空白の場合、レポートではデジタル署名にPFXファイルを使用します。
- **pfxFilename**: PFXファイルを参照します。ファイル名は完全修飾ファイル名で、パスとファイル拡張子が含まれている必要があります。空白であってはなりません。
- **pfxPwd**: パスワードを設定します。空白ではない必要があります。
- **purpose**: 署名の目的の説明です。空白にすることができます。

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
