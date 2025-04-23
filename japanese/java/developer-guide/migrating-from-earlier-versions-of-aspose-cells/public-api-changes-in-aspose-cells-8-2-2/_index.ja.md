---
title: Aspose.Cells 8.2.2でのパブリックAPIの変更
type: docs
weight: 100
url: /ja/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.2.1から8.2.2へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。

{{% /alert %}} 
## **APIの追加**
### **BuiltInDocumentPropertyCollectionクラスに新しいプロパティVersionが追加されました**
スプレッドシートの特定のファイルでアプリケーションのバージョンを取得または設定できるように、BuiltInDocumentPropertyCollectionクラスに新しいプロパティVersionが追加されました。

{{% alert color="primary" %}} 

スプレッドシートを作成したアプリケーションのバージョンを取得する詳細な記事をご覧ください

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Chart.Worksheet プロパティを追加しました**
Aspose.Cells 8.2.2のリリース前、ChartオブジェクトからWorksheetのインスタンスを取得することはできませんでした。Aspose.Cells 8.2.2は、Chart.Worksheetプロパティを提供することでこのギャップを埋めました

{{% alert color="primary" %}} 

Chartのワークシートに関する詳細な記事をご覧ください

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
