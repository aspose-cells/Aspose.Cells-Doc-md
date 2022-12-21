---
title: パブリック API Aspose.Cells の変更点 8.4.2
type: docs
weight: 150
url: /ja/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.4.1 から 8.4.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **改善されたチャート作成メカニズム**
Aspose.Cells.Charts.Chart クラスは、チャート作成のタスクを容易にするために SetChartDataRange メソッドを公開しました。 SetChartDataRange メソッドは 2 つのパラメーターを受け入れます。最初のパラメーターは、データ系列をプロットするセル領域を指定する文字列型です。 2 番目のパラメーターは、プロットの向きを指定する Boolean 型です。行ごとまたは列ごとにセル値の範囲からチャート データ系列をプロットするかどうか。

次のコード スニペットは、グラフのプロット シリーズ データがセル A1 から D4 までの同じワークシートに存在することを前提として、数行のコードで縦棒グラフを作成する方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **メソッド VbaModuleCollection.Add が追加されました**
Aspose.Cells for .NET 8.4.2 では、Workbook のインスタンスに新しい VBA モジュールを追加する VbaModuleCollection.Add メソッドが公開されています。 VbaModuleCollection.Add メソッドは、Worksheet 型のパラメーターを受け取り、ワークシート固有のモジュールを追加します。

次のコード スニペットは、VbaModuleCollection.Add メソッドの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **オーバーロードされたメソッド Cells.CopyColumns が追加されました**
Aspose.Cells for .NET 8.4.2 は、コピー元の列をコピー先に繰り返す Cells.CopyColumns メソッドのオーバーロードされたバージョンを公開しました。新しく公開されたメソッドは、合計 5 つのパラメーターを受け入れます。最初の 4 つのパラメーターは、共通の Cells.CopyColumns メソッドと同じです。ただし、int 型の最後のパラメーターは、ソース列を繰り返す必要がある宛先列の数を指定します。

次のコード スニペットは、新しく公開された Cells.CopyColumns メソッドの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **列挙フィールド PasteType.Default & PasteType.DefaultExceptBorders を追加**
v8.4.2 のリリースにより、Aspose.Cells API は PasteType の 2 つの新しい列挙フィールドを追加しました。詳細は以下のとおりです。

- PasteType.Default: セルの範囲を貼り付ける Excel の「すべて」機能と同様に機能します。
- PasteType.DefaultExceptBorders: セルの範囲を貼り付けるための Excel の「境界線以外のすべて」機能と同様に機能します。

次のサンプル コードは、PasteType.Default フィールドの使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Aspose.Cells for .NET 8.4.2 のリリース以降、列挙型フィールド PasteType.All は、セルの範囲を貼り付ける Excel の「すべて」機能とは異なる動作をします。現在、PasteType.All は、Excel の「すべて」機能とは対照的に、列幅も宛先範囲にコピーします。 Excel の「すべて」の動作を模倣するには、PasteType.Default を使用してください。

{{% /alert %}}
