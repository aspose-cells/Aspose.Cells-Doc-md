---
title: パブリック API Aspose.Cells 8.3.0 の変更点
type: docs
weight: 110
url: /ja/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.2.2 から 8.3.0 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **プロパティ WorkbookSettings.AutoRecover が追加されました**
プロパティ AutoRecover の getter/setter が WorkbookSettings クラスに追加され、開発者がアプリケーション内のスプレッドシートの Auto-Recovery オプションを取得/設定できるようになりました。

{{% alert color="primary" %}} 

記事をご確認ください[スプレッドシートの自動回復の設定](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook)詳細については。

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **プロパティ WorkbookSettings.CrashSave が追加されました**
プロパティ CrashSave の getter/setter が WorkbookSettings クラスに追加されました。ブール型のプロパティは、アプリケーションがクラッシュ後にワークブック ファイルを最後に保存したかどうかを示します。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **プロパティ WorkbookSettings.DataExtractLoad が追加されました**
プロパティ DataExtractLoad の getter/setter が WorkbookSettings クラスに追加され、開発者が最後のリカバリに関する情報を取得/設定できるようになりました。プロパティ DataExtractLoad が true を返した場合は、ワークブック ファイルでデータの回復が実行されたことを示します。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **プロパティ WorkbookSettings.RepairLoad が追加されました**
プロパティ RepairLoad のゲッター/セッターが WorkbookSettings クラスに追加されました。ブール型のプロパティは、スプレッドシートが Excel アプリケーションの最後の読み込みセッションで修復されたかどうかを示します。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **プロパティ TxtLoadOptions.KeepExactFormat が追加されました**
プロパティ KeepExactFormat が TxtLoadOptions クラスに追加されました。これは、文字列/テキストが数値または DateTime に変換されるときにセル値の正確な書式設定を保持する必要があるかどうかを示します。このプロパティは、CSV ファイルから DateTime または数値をロードするための MS Excel アプリケーションの動作と一致するように追加されました。 MS Excel の動作をシミュレートするには、KeepExactFormat プロパティを false に設定します。デフォルト値は true であるため、セル値は CSV ファイルの文字列としてフォーマットされます。

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **プロパティ Shape.Id が追加されました**
v8.3.0 では、特定のスプレッドシート内の各形状オブジェクトを一意に識別するために、プロパティ Shape.Id のゲッター/セッターが追加されました。この新しいプロパティは、以下に示すように、スプレッドシート内の Chart オブジェクトを一意に識別するのにも役立ちます。

**Java**

{{< highlight "csharp" >}}

ワークブック book = new Workbook("sample.xlsx");

ChartCollection チャート = book.getWorksheets().get(0).getCharts();

 for(int インデックス = 0; インデックス<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **メソッド PlotArea.setPositionAuto が追加されました**
メソッド setPositionAuto が PlotArea クラスに追加され、グラフのプロット エリアを自動モードに設定するのに役立ちます。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
