---
title: Aspose.Cells 8.2.2でのパブリックAPIの変更
type: docs
weight: 90
url: /ja/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.2.1から8.2.2へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。

{{% /alert %}} 
## **APIの追加**
### **BuiltInDocumentPropertyCollection.Versionプロパティを追加しました**
アプリケーションが作成したスプレッドシートのバージョンを取得するために、BuiltInDocumentPropertyCollectionクラスに新しいVersionプロパティが追加されました。

{{% alert color="primary" %}} 

詳細については、[スプレッドシートを作成したアプリケーションのバージョンを取得](/cells/ja/net/get-the-version-number-of-the-application-that-created-the-excel-document/)の記事をご確認ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Chart.Worksheet プロパティを追加しました**
Aspose.Cells 8.2.2のリリース前に、Chartオブジェクトが保持するワークシートからインスタンスを取得することはできませんでした。Aspose.Cells 8.2.2では、Chart.Worksheetプロパティが提供され、このギャップを埋めました。

{{% alert color="primary" %}} 

詳細については、[チャートのワークシートを取得](/cells/ja/net/get-worksheet-of-the-chart/)の記事をご確認ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
