---
title: Aspose.Cells 8.5.0での公開APIの変更
type: docs
weight: 160
url: /ja/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells バージョン 8.4.2 から 8.5.0 への変更について、モジュール／アプリケーション開発者に興味を持たれるかもしれない点を記載しています。これには新しいおよび更新された公開メソッド、[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-5-0/)に関する情報だけでなく、Aspose.Cells の内部の動作に変更がある場合の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **ICustomFunction.CalculateCustomFunctionパラメータを変更しました**
カスタム関数の1つのパラメータがセル参照の場合、古いバージョンのAspose.Cells APIでは、セル参照を1つのセル値に変換するか、参照領域のすべてのセル値のオブジェクト配列に変換していました。しかし、多くの関数やユーザーにとって、参照領域のセル値配列は必要ない場合があります。彼らは式の位置に対応する1つのセル値だけが必要だったり、セル値の配列の代わりに参照自体が欲しい場合があります。一部の状況では、すべてのセル値を取得することが循環参照エラーのリスクを高めることさえありました。

このような要件をサポートするために、Aspose.Cells for .NET 8.5.0 では参照された範囲に対するパラメータ値を「paramsList」に変更しました。v8.5.0 以降、API では、対応するパラメータが参照またはその計算結果が参照である場合、ReferredArea オブジェクトを「paramsList」に入れるだけになります。参照そのものが必要な場合は、ReferredArea を直接使用できます。式の位置に対応する参照から単一のセルの値を取得する必要がある場合は、ReferredArea.GetValue(rowOffset, int colOffset) メソッドを使用できます。範囲全体のセル値の配列が必要な場合は、ReferredArea.GetValues メソッドを使用できます。

現在、Aspose.Cells for .NET 8.5.0 では「paramsList」で ReferredArea を提供されており、「contextObjects」での ReferredAreaCollection は不要になりました（以前のバージョンでは常にカスタム関数のパラメータに対して一対一のマップを提供できなかったため）。そのため、このリリースでは「contextObjects」から ReferredAreaCollection を削除しました。

この変更により、リファレンスパラメータの値/値を必要とするときに、ICustomFunction の実装コードに多少の変更が必要になります。

** 古い実装 **

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

** 新しい実装 **

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **クラス CalculationOptions 追加**
Aspose.Cells for .NET 8.5.0 では、CalculationOptions クラスが公開され、数式計算エンジンの柔軟性と拡張性を向上させるためのクラスが追加されました。新たに追加されたクラスには以下のプロパティがあります。

1. CalculationOptions.CalcStackSize: 再帰的にセルを計算するためのスタックサイズを指定します。-1 は、計算が対応するワークブックの WorkbookSettings.CalcStackSize を使用することを指定します。
1. CalculationOptions.CustomFunction: カスタム数式を使用して数式計算エンジンを拡張します。
1. CalculationOptions.IgnoreError: エラーを隠すべきかどうかを示す真偽値。エラーの原因は、サポートされていない関数、外部リンクなどによる場合があります。
1. CalculationOptions.PrecisionStrategy: 計算の精度処理の戦略を指定する CalculationPrecisionStrategy タイプの値。
### **列挙型 CalculationPrecisionStrategy 追加**
Aspose.Cells for .NET 8.5.0 では、希望の結果を得るために計算エンジンに柔軟性を追加するために、列挙型 CalculationPrecisionStrategy が公開されました。この列挙型は計算精度の処理戦略を規定します。IEEE 754浮動小数点演算の精度の問題のため、見た目には単純な数式でも、期待通りの結果が得られないことがあるため、最新のAPIビルドでは以下のフィールドが公開され、選択に応じて希望の結果を得ることができます。

1. CalculationPrecisionStrategy.Decimal: 可能な限り10進数をオペランドとして使用し、パフォーマンス上最も効率が悪いです。
1. CalculationPrecisionStrategy.Round: 計算結果を有効桁数に従って四捨五入します。
1. CalculationPrecisionStrategy.None: 戦略は適用されず、計算中にエンジンはオリジナルの倍精度値をオペランドとして使用し、結果を直接返します。このオプションは最も効率的で、ほとんどの場合に適用できます。
### **CalculationOptions を使用するためのメソッドが追加されました**
v8.5.0のリリース以降、Aspose.Cells API は、以下にリストされている CalculateFormula メソッドのオーバーロードバージョンを追加しました。

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **列挙型フィールド PasteType.RowHeights が追加されました**
Aspose.Cells API は、範囲をコピーする際に行の高さをコピーするための PasteType.RowHeights 列挙フィールドを提供しています。PasteOptions.PasteTypeプロパティを ((PasteType.RowHeights}}に設定すると、ソース範囲内のすべての行の高さが、宛先範囲にコピーされます。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **SheetRender.PageScale プロパティが追加されました**
Microsoft Excel で **Fit to n page(s) wide by m tall** オプションを使用してページ設定スケーリングを設定すると、ページ設定のスケーリングファクターが計算されます。Aspose.Cells for .NET 8.5.0 が公開した SheetRender.PageScale プロパティを使用して同じことを達成できます。このプロパティはパーセンテージ値に変換できる倍精度値を返します。たとえば、0.507968245 が返された場合、スケーリングファクターは51％であることを意味します。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **列挙型 CellValueFormatStrategy 追加**
Aspose.Cells for .NET 8.5.0 は、セルの値をフォーマットを適用した場合、または適用しなかった場合に処理するための新しい列挙型 CellValueFormatStrategy を追加しました。列挙型 CellValueFormatStrategy には、以下のフィールドがあります。

1. CellValueFormatStrategy.CellStyle: セルのオリジナルの書式をそのままにフォーマットします。
1. CellValueFormatStrategy.DisplayStyle: セルの表示スタイルでフォーマットします。
1. CellValueFormatStrategy.None: フォーマットされません。
### **Cell.GetStingValue メソッドが追加されました**
CellValueFormatStrategy 列挙型を使用するために、v8.5.0 で Cell.GetStingValue メソッドが公開されました。このメソッドは、CellValueFormatStrategy型のパラメータを受け取り、指定されたオプションに応じた値を返します。

以下のコードスニペットは、新しく公開された Cells.GetStingValue メソッドの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **ExportTableOptions.FormatStrategy プロパティが追加されました**
Aspose.Cells for .NET 8.5.0 は、データをフォーマット付きでDataTableにエクスポートする必要があるユーザー向けに、ExportTableOptions.FormatStrategy プロパティが公開されました。このプロパティは、CellValueFormatStrategy 列挙型を使用し、指定されたオプションに従ってデータをエクスポートします。

以下のコードは、ExportTableOptions.FormatStrategy プロパティの使用方法を説明しています。

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
