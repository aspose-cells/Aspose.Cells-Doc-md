---
title: パブリック API Aspose.Cells 8.3.0 の変更点
type: docs
weight: 100
url: /ja/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.2.2 から 8.3.0 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **プロパティ WorkbookSettings.AutoRecover が追加されました**
新しいプロパティ AutoRecover が WorkbookSettings クラスに追加され、開発者がアプリケーションでスプレッドシートの自動回復のオプションを設定できるようになりました。

{{% alert color="primary" %}} 

記事をご確認ください[スプレッドシートの自動回復の設定](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook)詳細については。

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **プロパティ WorkbookSettings.CrashSave が追加されました**
ブール型のプロパティ CrashSave が WorkbookSettings クラスに追加されました。これは、アプリケーションがクラッシュ後にワークブック ファイルを最後に保存したかどうかを示します。

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **プロパティ WorkbookSettings.DataExtractLoad が追加されました**
開発者が最後の回復に関する情報を取得できるようにするために、プロパティ DataExtractLoad が WorkbookSettings クラスに追加されました。プロパティ DataExtractLoad が true を返した場合は、スプレッドシートでデータ リカバリが実行されたことを示します。

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **プロパティ WorkbookSettings.RepairLoad が追加されました**
プロパティ RepairLoad は、スプレッドシートが Excel アプリケーションでの最後の読み込みで修復されたかどうかを示します。

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **プロパティ TxtLoadOptions.KeepExactFormat が追加されました**
プロパティ KeepExactFormat が TxtLoadOptions クラスに追加されました。これは、文字列/テキストが数値または DateTime に変換されるときにセル値の正確な書式設定を保持する必要があるかどうかを示します。このプロパティは、CSV ファイルから DateTime または数値をロードするための MS Excel アプリケーションの動作と一致するように追加されました。 MS Excel の動作をシミュレートするには、KeepExactFormat プロパティを false に設定します。デフォルト値は true であるため、セル値は CSV ファイルの文字列としてフォーマットされます。

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **プロパティ Shape.Id が追加されました**
プロパティ Id が Shape クラスに追加され、特定のスプレッドシート内の各シェイプ オブジェクトを一意に識別できるようになりました。この新しいプロパティは、以下に示すように、スプレッドシート内の Chart オブジェクトの識別にも役立ちます。

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **メソッド PlotArea.SetPositionAuto が追加されました**
メソッド SetPositionAuto が PlotArea クラスに追加され、グラフのプロット エリアを自動モードに設定するのに役立ちます。

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
