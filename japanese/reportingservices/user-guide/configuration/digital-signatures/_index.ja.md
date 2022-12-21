---
title: デジタル署名
type: docs
weight: 50
url: /ja/reportingservices/digital-signatures/
---
Aspose.Cells for Reporting Services は、Microsoft Excel 2007 ファイルまたは ODS ファイルのエクスポート時にデジタル署名をサポートします。で設定できるデジタル署名の構成情報がいくつかあります。**Aspose.Cells.ReportingServices.xml**ファイル。

 DigitalSignature の値が**オフ**、Aspose.Cells for Reporting Services はデジタル署名をオフにします。

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 DigitalSignature の値が**の上**Aspose.Cells for Reporting Services はデジタル署名をオンにします。

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature セクションには 4 つのパラメーターがあります。これらは：

- **名前**デジタル署名が必要なレポートを表します。パラメータを空白のままにすると、レポートはデジタル署名に PFX ファイルを使用します。
- **pfxファイル名**PFX ファイルを参照します。ファイル名は、パスとファイル拡張子を含む完全修飾ファイル名である必要があります。空白にすることはできません。
- **pfxPwd**: パスワードを設定します。空白にすることはできません。
- **目的**署名の目的の説明。空白にすることができます。

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
