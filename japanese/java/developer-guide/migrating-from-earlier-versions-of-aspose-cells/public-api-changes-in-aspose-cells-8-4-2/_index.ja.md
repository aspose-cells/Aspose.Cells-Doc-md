---
title: Aspose.Cells 8.4.2での公開APIの変更
type: docs
weight: 160
url: /ja/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsの挙動の変更について説明しています。これは、バージョン8.4.1から8.4.2への変更であり、モジュール/アプリケーション開発者にとって興味深いものかもしれません。[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-4-2/)に加え、新しいおよび更新された公開メソッドだけでなく、Aspose.Cellsの内部の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **改良されたチャート作成メカニズム**
com.aspose.cells.charts.Chartクラスは、setChartDataRangeメソッドを公開し、チャートの作成タスクを容易にしました。setChartDataRangeメソッドは、2つのパラメータを受け入れます。1つ目のパラメータは、データ系列をプロットするためのセル範囲を指定するstring型で、2つ目のパラメータは、プロットの方向（つまり、行または列ごとにチャートのデータ系列をプロットするか）を指定するBoolean型です。

以下のコードスニペットは、少数のコードを使用して列のチャートを作成する方法を示しています。チャートのプロット系列データが同じワークシート上のセルA1からD4にあると仮定しています。

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **VbaModuleCollection.addメソッドを追加しました**
Aspose.Cells for Java 8.4.2では、VbaModuleCollection.addメソッドを公開し、ワークブックのインスタンスに新しいVBAモジュールを追加するために使用できるようにしました。VbaModuleCollection.addメソッドは、ワークシートの型のパラメータを受け入れ、ワークシート固有のモジュールを追加するために使用します。

以下のコードスニペットは、VbaModuleCollection.addメソッドの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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

### **Cells.copyColumnsのオーバーロードメソッドを追加しました**
Aspose.Cells for Java 8.4.2では、Cells.copyColumnsメソッドのオーバーロードバージョンを公開し、元の列を宛先に繰り返しコピーできるようにしました。新たに公開されたメソッドは、合計5つのパラメータを受け入れます。最初の4つのパラメータは、通常のCells.copyColumnsメソッドと同じです。ただし、最後のint型のパラメータは、元の列を繰り返す宛先の列の数を指定します。

以下のコードスニペットは、新たに公開されたCells.copyColumnsメソッドの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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

### **列挙型フィールドPasteType.DEFAULTおよびPasteType.ALL_EXCEPT_BORDERSを追加しました**
v8.4.2のリリースに伴い、Aspose.Cells APIにはPasteType用の2つの新しい列挙型フィールドが追加されました。

- PasteType.DEFAULT: セルの範囲を貼り付ける際に、Excelの「全て」機能と類似の操作を行います。
- PasteType.ALL_EXCEPT_BORDERS: セルの範囲を貼り付ける際に、Excelの「罫線を含まない全て」機能と類似の操作を行います。

以下のサンプルコードは、PasteType.DEFAULTフィールドの使用方法を示しています。

**Java**

{{< highlight csharp >}}

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

Aspose.Cells for Java 8.4.2のリリース以降、列挙型フィールドPasteType.ALLは、セルの範囲を貼り付ける際の動作が、Excelの「全て」機能とは異なるように変更されました。現在、PasteType.ALLは、列の幅も目的の範囲にコピーする点がExcelの「全て」機能とは異なります。Excelの「全て」の動作を模倣するためには、PasteType.DEFAULTを使用してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
