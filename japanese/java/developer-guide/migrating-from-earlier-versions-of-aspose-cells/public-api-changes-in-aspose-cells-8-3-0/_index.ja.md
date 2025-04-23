---
title: Aspose.Cells 8.3.0のパブリックAPIの変更
type: docs
weight: 110
url: /ja/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIのバージョン8.2.2から8.3.0への変更について、モジュール/アプリケーション開発者に興味を持っていただけるかもしれない変更について説明しています

{{% /alert %}} 
## **APIの追加**
### **WorkbookSettings.AutoRecoverプロパティを追加しました**
WorkbookSettingsクラスに、スプレッドシートの自動リカバリオプションを取得/設定するためのプロパティAutoRecoverのgetter/setterが追加されました 

{{% alert color="primary" %}} 

スプレッドシートの自動リカバリを設定する記事をご覧ください

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **WorkbookSettings.CrashSaveプロパティを追加しました**
WorkbookSettingsクラスに、ブール型のCrashSaveプロパティ（ブール型のプロパティ）が追加されました。このプロパティは、アプリケーションがクラッシュした後にブックファイルを保存したかどうかを示します

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **WorkbookSettings.DataExtractLoadプロパティを追加しました**
WorkbookSettingsクラスに、ワークブックファイルでの最後のリカバリに関する情報を取得/設定するためのDataExtractLoadプロパティのgetter/setterが追加されました。DataExtractLoadプロパティがtrueを返す場合、それはワークブックファイルでデータリカバリが実行されたことを示します

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **WorkbookSettings.RepairLoadプロパティを追加しました**
WorkbookSettingsクラスに、ブール型のプロパティRepairLoadのgetter/setterが追加されました。このプロパティは、スプレッドシートがExcelアプリケーションとの最後のロードセッションで修復されたかどうかを示します

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **TxtLoadOptions.KeepExactFormatプロパティを追加しました**
TxtLoadOptionsクラスに、数値や日付時刻のCSVファイルからの変換時に、セルの値の正確な書式を維持するかどうかを示すプロパティKeepExactFormatが追加されました。このプロパティは、デフォルト値がtrueであるため、セルの値はCSVファイルのように文字列としてフォーマットされます

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Shape.Idプロパティを追加しました**
v8.3.0には、スプレッドシート内の各Shapeオブジェクトを一意に識別するためにShape.Idプロパティのgetter/setterが追加されました。この新しいプロパティは、スプレッドシート内のChartオブジェクトを一意に識別するのにも役立ちます

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **PlotArea.setPositionAutoメソッドを追加しました**
PlotAreaクラスに、チャートのプロットエリアを自動モードに設定するのを支援するsetPositionAutoメソッドが追加されました

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
