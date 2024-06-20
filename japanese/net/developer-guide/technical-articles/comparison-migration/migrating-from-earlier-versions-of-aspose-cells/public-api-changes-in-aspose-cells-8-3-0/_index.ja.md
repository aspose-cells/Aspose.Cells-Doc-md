---
title: Aspose.Cells 8.3.0のパブリックAPIの変更
type: docs
weight: 100
url: /ja/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIのバージョン8.2.2から8.3.0への変更について、モジュール/アプリケーション開発者に興味を持っていただけるかもしれない変更について説明しています

{{% /alert %}} 
## **APIの追加**
### **WorkbookSettings.AutoRecoverプロパティを追加しました**
ワークブックのスプレッドシートで自動回復のオプションを設定するために、WorkbookSettingsクラスに新しいAutoRecoverプロパティが追加されました。

{{% alert color="primary" %}} 

詳細については、[スプレッドシートの自動回復の設定](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook)の記事をご確認ください。

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **WorkbookSettings.CrashSaveプロパティを追加しました**
WorkbookSettingsクラスにBoolean型のCrashSaveプロパティが追加され、アプリケーションがクラッシュした後にワークブックファイルを最後に保存したかどうかを示します。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **WorkbookSettings.DataExtractLoadプロパティを追加しました**
WorkbookSettingsクラスにDataExtractLoadプロパティが追加され、開発者がスプレッドシート上で前回のデータ復旧に関する情報を取得できるようになりました。DataExtractLoadプロパティがtrueを返すと、データ復旧がスプレッドシートで実行されたことを示します。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **WorkbookSettings.RepairLoadプロパティを追加しました**
RepairLoadプロパティは、Excelアプリケーションでの最後の読み込み時にスプレッドシートが修復されたかどうかを示します。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **TxtLoadOptions.KeepExactFormatプロパティを追加しました**
TxtLoadOptionsクラスに、数値や日付時刻のCSVファイルからの変換時に、セルの値の正確な書式を維持するかどうかを示すプロパティKeepExactFormatが追加されました。このプロパティは、デフォルト値がtrueであるため、セルの値はCSVファイルのように文字列としてフォーマットされます

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Shape.Idプロパティを追加しました**
ShapeクラスにIdプロパティが追加され、指定されたスプレッドシート内の各シェイプオブジェクトを一意に識別するのに役立ちます。この新しいプロパティは、スプレッドシート内のチャートオブジェクトを識別するのにも役立ちます。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **PlotAreaクラスにSetPositionAutoメソッドが追加され、チャートのプロットエリアを自動モードに設定するのをサポートします。**
PlotAreaクラスにSetPositionAutoメソッドが追加され、チャートのプロットエリアを自動モードに設定するのをサポートします。

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
