---
title: パブリック API Aspose.Cells の変更点 8.4.2
type: docs
weight: 160
url: /ja/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.4.1 から 8.4.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **改善されたチャート作成メカニズム**
com.aspose.cells.charts.Chart クラスは setChartDataRange メソッドを公開して、チャート作成のタスクを容易にしました。 setChartDataRange メソッドは 2 つのパラメーターを受け入れます。最初のパラメーターは、データ系列をプロットするセル領域を指定する文字列型です。 2 番目のパラメーターは、プロットの向きを指定する Boolean 型です。行ごとまたは列ごとにセル値の範囲からチャート データ系列をプロットするかどうか。

次のコード スニペットは、グラフのプロット シリーズ データがセル A1 から D4 までの同じワークシートに存在することを前提として、数行のコードで縦棒グラフを作成する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **メソッド VbaModuleCollection.add が追加されました**
Aspose.Cells for Java 8.4.2 では、Workbook のインスタンスに新しい VBA モジュールを追加する VbaModuleCollection.add メソッドが公開されています。 VbaModuleCollection.add メソッドは、Worksheet 型のパラメーターを受け取り、ワークシート固有のモジュールを追加します。

次のコード スニペットは、VbaModuleCollection.add メソッドの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **オーバーロードされたメソッド Cells.copyColumns が追加されました**
Aspose.Cells for Java 8.4.2 では、コピー元の列をコピー先に繰り返すために、オーバーロードされたバージョンの Cells.copyColumns メソッドが公開されています。新しく公開されたメソッドは、合計 5 つのパラメーターを受け入れます。最初の 4 つのパラメーターは、一般的な Cells.copyColumns メソッドと同じです。ただし、int 型の最後のパラメーターは、ソース列を繰り返す必要がある宛先列の数を指定します。

次のコード スニペットは、新しく公開された Cells.copyColumns メソッドの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **列挙型フィールド PasteType.DEFAULT および PasteType.ALL_EXCEPT_BORDERS を追加**
v8.4.2 のリリースにより、Aspose.Cells API は PasteType の 2 つの新しい列挙フィールドを追加しました。詳細は以下のとおりです。

- PasteType.DEFAULT: セルの範囲を貼り付けるための Excel の「すべて」機能と同様に機能します。
- PasteType.ALL_を除外する_BORDERS: セルの範囲を貼り付けるための Excel の「境界線以外のすべて」機能と同様に機能します。

次のサンプル コードは、PasteType.DEFAULT フィールドの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Aspose.Cells for Java 8.4.2 のリリース以降、列挙型フィールド PasteType.ALL は、セルの範囲を貼り付ける Excel の「すべて」機能とは異なる動作をします。現在、PasteType.ALL は、Excel の「すべて」機能とは対照的に、列幅も宛先範囲にコピーします。 Excel の「すべて」の動作を模倣するには、PasteType.DEFAULT を使用してください。

{{% /alert %}}
