---
title: パブリック API Aspose.Cells の変更点 8.3.1
type: docs
weight: 120
url: /ja/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.0 から 8.3.1 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **プロパティ DataLabels.ShowCellRange が追加されました**
実行時にグラフのデータ ラベルをフォーマットする Excel の機能を模倣するために、プロパティ ShowCellRange のゲッター/セッターが DataLabels クラスに追加されました。 Excel は、次の手順でこの機能を提供することに注意してください。

1. シリーズのデータ ラベルを選択し、右クリックしてポップアップ メニューを開きます。
1. クリック**データ ラベルの書式設定...**そしてそれは表示されます**ラベル オプション**.
1. チェックボックスをオンまたはオフにする**ラベルの内容 - Cells からの値**.

以下のサンプル コードは、グラフ シリーズのデータ ラベルにアクセスし、DataLabels.setShowCellRange() メソッドを true に設定して、Excel の機能を模倣します。**ラベルの内容 - Cells からの値**.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

記事をご確認ください[Cell 範囲をデータ ラベルとして表示](/cells/ja/java/showing-cell-range-as-the-data-labels/)詳細については。

{{% /alert %}} 

### **メソッド Cell.getTable & ListObject.putCellValue を追加**
メソッド Cell.getTable & ListObject.putCellValue が Aspose.Cells for Java 8.3.1 で追加され、ユーザーがセルから ListObject にアクセスし、行と列のオフセットを使用してその中に値を追加できるようになりました。次のサンプル コードは、ソース スプレッドシートを読み込み、テーブル内に値を追加します。

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

記事をご確認ください[Cell からテーブルにアクセスし、行と列のオフセットを使用してテーブル内に値を追加する](/cells/ja/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/)詳細については。

{{% /alert %}} 

### **メソッド OdsSaveOptions.isStrictSchema11 および OdsSaveOptions.setStrictSchema11 が追加されました**
開発者が ODF v1.2 仕様に準拠した形式でスプレッドシートを保存できるようにするために、メソッド isStrictSchema11 および setStrictSchema11 が OdsSaveOptions クラスに追加されました。 setStrictSchema11 プロパティのデフォルト値は false です。これは、Aspose.Cells API のバージョン 8.3.1 以降、デフォルトで ODS ファイルが ODF フォーマット バージョン 1.2 として保存されることを意味します。

以下のコード スニペットは、ODS ファイルを ODF 1.2 形式で保存します。

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

記事をご確認ください[ODS ファイルを ODF 1.1 および 1.2 仕様で保存](/cells/ja/java/save-ods-file-in-odf-1-1-and-1-2-specifications/)詳細については。

{{% /alert %}} 

### **メソッド SparklineCollection.add が追加されました**
Aspose.Cells API は SparklineCollection.add(String dataRange, int row, int column) メソッドを公開して、スパークライン グループのデータ範囲と場所を指定しました。 Excel は、次の手順で同じ機能を提供することに注意してください。

1. スパークラインを含むセルを選択します。
1. 選択する**スパークラインからデータを編集する**セクション内**デザイン**タブ
1. 選ぶ**グループの場所とデータの編集**.
1. 特定**データ範囲** & **位置**.

次のサンプル コードは、ソース スプレッドシートを読み込み、最初のスパークライン グループにアクセスし、スパークライン グループに新しいデータ範囲と場所を追加します。

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

記事をご確認ください[スパークライン グループのデータ範囲と場所を指定してスパークラインをコピーする](/cells/ja/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/)詳細については。

{{% /alert %}}
