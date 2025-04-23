---
title: Aspose.Cells 8.4.2での公開APIの変更
type: docs
weight: 150
url: /ja/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells API のバージョン 8.4.1 から 8.4.2 への変更について、モジュール／アプリケーション開発者に興味を持たれるかもしれない点を記載しています。これには新しいメソッドや更新された公開メソッドのほか、[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-4-2/)に関する情報だけでなく、Aspose.Cells の内部の動作に変更がある場合の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **改良されたチャート作成メカニズム**
Aspose.Cells.Charts.Chart クラスに SetChartDataRange メソッドが公開され、このメソッドを使用することでチャート作成のタスクを簡素化できるようになりました。SetChartDataRange メソッドは 2 つのパラメータを受け入れます。1 つ目のパラメータは文字列型で、データ系列をプロットするセル領域を指定します。2 つ目のパラメータは Boolean 型で、プロットの向きを指定します。つまり、セルの値の範囲からデータ系列を行方向または列方向にプロットするかを指定します。

以下のコードスニペットは、少数のコードを使用して列のチャートを作成する方法を示しています。チャートのプロット系列データが同じワークシート上のセルA1からD4にあると仮定しています。

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **VbaModuleCollection.Add メソッドが追加されました**
Aspose.Cells for .NET 8.4.2 では、VbaModuleCollection.Add メソッドが追加され、Workbook インスタンスに新しい VBA モジュールを追加することができるようになりました。VbaModuleCollection.Add メソッドは、ワークシート固有のモジュールを追加するための Worksheet 型のパラメータを受け入れます。

以下のコードスニペットは、VbaModuleCollection.Add メソッドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

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


### **Overloaded Method Cells.CopyColumns Added**
Aspose.Cells for .NET 8.4.2 では、Cells.CopyColumns メソッドのオーバーロードバージョンが公開され、ソースの列を宛先に繰り返してコピーすることができるようになりました。新たに公開されたメソッドは合計 5 つのパラメータを受け入れます。最初の 4 つのパラメータは通常の Cells.CopyColumns メソッドと同じですが、最後の int 型のパラメータは、ソースの列を繰り返す宛先の列の数を指定します。

以下のコードスニペットは、新たに公開された Cells.CopyColumns メソッドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

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


### **列挙体のフィールド PasteType.Default および PasteType.DefaultExceptBorders が追加されました**
v8.4.2のリリースに伴い、Aspose.Cells APIにはPasteType用の2つの新しい列挙型フィールドが追加されました。

- PasteType.Default: セルの範囲を貼り付ける際に Excel の「すべて」機能と同様に機能します。
- PasteType.DefaultExceptBorders: セルの範囲を貼り付ける際に Excel の「すべての罫線を除く」機能と同様に機能します。

次のサンプルコードは、PasteType.Default フィールドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

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

リリース Aspose.Cells for .NET 8.4.2 以降、列挙型の PasteType.All は、Excel の「すべて」機能とは異なる動作となりました。現在、PasteType.All は列の幅も宛先範囲にコピーするようになりました。Excel の「すべて」機能と同じ動作を再現するには、 PasteType.Default を使用してください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
