---
title: パブリック API Aspose.Cells の変更点 8.2.2
type: docs
weight: 100
url: /ja/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.2.1 から 8.2.2 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **BuiltInDocumentPropertyCollection クラスに追加されたプロパティ バージョン**
開発者が特定のスプレッドシートのアプリケーションのバージョンを取得または設定できるようにするために、新しいプロパティ Version が BuiltInDocumentPropertyCollection クラスに追加されました。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[スプレッドシートを作成したアプリケーションのバージョンを取得する](/cells/ja/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Property Chart.Worksheet が追加されました**
Aspose.Cells 8.2.2 がリリースされる前は、ワークシートに含まれる Chart オブジェクトからワークシートのインスタンスを取得することはできませんでした。 Aspose.Cells 8.2.2 は Chart.Worksheet プロパティを提供することでこのギャップを埋めました。

{{% alert color="primary" %}} 

詳細記事をご確認ください[チャートのワークシートを取得](/cells/ja/java/get-worksheet-of-the-chart/)詳細については。

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
