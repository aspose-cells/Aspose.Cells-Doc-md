---
title: Aspose.Cells 8.3.1のパブリックAPIの変更
type: docs
weight: 120
url: /ja/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIのバージョン8.3.0から8.3.1への変更について、モジュール/アプリケーション開発者に興味を持っていただけるかもしれない変更について説明しています

{{% /alert %}} 
## **APIの追加**
### **DataLabels.ShowCellRangeプロパティを追加しました**
DataLabelsクラスに、実行時にChartのデータラベルをフォーマットするExcelの機能を模倣するためのShowCellRangeプロパティのgetter/setterが追加されました 

データラベルを表示するための記事をご覧ください
1. **データラベルの書式設定...**をクリックし、**ラベルオプション**が表示されます。
1. チェックボックス **ラベルに - セルの値が含まれている** をチェックまたはチェックを外します。

以下のサンプルコードは、グラフシリーズのデータラベルにアクセスし、DataLabels.setShowCellRange()メソッドをtrueに設定して**ラベルが持つ - セルからの値**のExcelの機能を模倣します。

**Java**

{{< highlight csharp >}}

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

詳細については、[セル範囲をデータラベルとして表示](/cells/ja/java/showing-cell-range-as-the-data-labels/)の記事を確認してください。

{{% /alert %}} 

### **Cell.getTableおよびListObject.putCellValueメソッドを追加しました**
Cell.getTableおよびListObject.putCellValueメソッドは、Aspose.Cells for Java 8.3.1で追加されました。これにより、ユーザーはセルからListObjectにアクセスし、行および列のオフセットを使用してその内部に値を追加できます。次のサンプルコードでは、ソーススプレッドシートをロードし、テーブル内に値を追加しています。

**Java**

{{< highlight csharp >}}

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

詳細については、[セルからテーブルにアクセスし、行および列のオフセットを使用して値を追加する](/cells/ja/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/)をご覧ください。

{{% /alert %}} 

### **OdsSaveOptions.isStrictSchema11およびOdsSaveOptions.setStrictSchema11メソッドを追加しました**
isStrictSchema11およびsetStrictSchema11メソッドは、OdsSaveOptionsクラスに追加されました。これにより、開発者はスプレッドシートをODF v1.2仕様に準拠した形式で保存できるようになります。setStrictSchema11プロパティのデフォルト値はfalseであり、Aspose.Cells APIの8.3.1以降では、ODSファイルはデフォルトでODF形式バージョン1.2として保存されます。

以下のコードスニペットは、ODSファイルをODF 1.2形式で保存します。

**Java**

{{< highlight csharp >}}

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

詳細については、[ODF 1.1および1.2仕様でODSファイルを保存する](/cells/ja/java/save-ods-file-in-odf-1-1-and-1-2-specifications/)をご覧ください。

{{% /alert %}} 

### **SparklineCollection.addメソッドを追加しました**
Aspose.Cells APIは、SparklineCollection.add(String dataRange, int row, int column)メソッドを公開し、データ範囲とスパークライングループの場所を指定できるようにしました。Excelでは同様の機能を以下の手順で提供しています。 

1. スパークラインを含むセルを選択します。
1. **デザイン**タブ内の**スパークライン**セクションから**データの編集**を選択します
1. **グループの場所とデータの編集**を選択します。
1. **データ範囲**および**場所**を指定します。

以下のサンプルコードでは、ソーススプレッドシートをロードし、最初のスパークライングループにアクセスし、新しいデータ範囲と場所を追加しています。 

**Java**

{{< highlight csharp >}}

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

詳細については、[スパークライングループのデータ範囲と場所を指定してコピーする](/cells/ja/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/)をご覧ください。

{{% /alert %}}
