---
title: パブリック API Aspose.Cells の変更点 8.2.2
type: docs
weight: 90
url: /ja/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.2.1 から 8.2.2 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **プロパティ BuiltInDocumentPropertyCollection.Version が追加されました**
開発者が特定のスプレッドシートを作成したアプリケーションのバージョンを取得できるようにするために、新しいプロパティ Version が BuiltInDocumentPropertyCollection クラスに追加されました。

{{% alert color="primary" %}} 

詳細記事をご確認ください[スプレッドシートを作成したアプリケーションのバージョンを取得する](/cells/ja/net/get-the-version-number-of-the-application-that-created-the-excel-document/)詳細については。

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Property Chart.Worksheet が追加されました**
Aspose.Cells 8.2.2 がリリースされる前は、Worksheet が保持する Chart オブジェクトから Worksheet のインスタンスを取得することはできませんでした。 Aspose.Cells 8.2.2 は Chart.Worksheet プロパティを提供することでこのギャップを埋めました。

{{% alert color="primary" %}} 

詳細記事をご確認ください[チャートのワークシートを取得](/cells/ja/net/get-worksheet-of-the-chart/)詳細については。

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
