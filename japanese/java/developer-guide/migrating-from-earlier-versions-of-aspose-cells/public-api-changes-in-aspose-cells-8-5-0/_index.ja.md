---
title: Aspose.Cells 8.5.0での公開APIの変更
type: docs
weight: 170
url: /ja/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsの挙動の変更について説明しています。これは、バージョン8.4.2から8.5.0への変更であり、モジュール/アプリケーション開発者にとって興味深いものかもしれません。[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-0/)に加え、新しいおよび更新された公開メソッドだけでなく、Aspose.Cellsの内部の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **ICustomFunction.CalculateCustomFunctionパラメータを変更しました**
カスタム関数の1つのパラメータがセル参照の場合、古いバージョンのAspose.Cells APIでは、セル参照を1つのセル値に変換するか、参照領域のすべてのセル値のオブジェクト配列に変換していました。しかし、多くの関数やユーザーにとって、参照領域のセル値配列は必要ない場合があります。彼らは式の位置に対応する1つのセル値だけが必要だったり、セル値の配列の代わりに参照自体が欲しい場合があります。一部の状況では、すべてのセル値を取得することが循環参照エラーのリスクを高めることさえありました。

そのような要件をサポートするために、Aspose.Cells for Java 8.5.0では、参照領域に対応する"paramsList"のパラメータ値を変更しました。これにより、APIは、対応するパラメータが参照またはその計算結果が参照である場合、"paramsList"にReferredAreaオブジェクトを配置します。参照自体が必要な場合は、ReferredAreaを直接使用できます。式の位置に対応する1つのセル値が必要な場合は、ReferredArea.getValue(rowOffset, int colOffset)メソッドを使用できます。全領域のセル値配列が必要な場合は、ReferredArea.getValuesメソッドを使用できます。

Aspose.Cells for Java 8.5.0 は「paramsList」内で ReferredArea を提供するため、古いバージョンでは ReferredAreaCollection（古いバージョンでは常にカスタム関数のパラメータに1対1のマップを提供できなかった）はもはや必要ありません。そのため、このリリースでは「contextObjects」からも削除されました。

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Aspose.Cells for Java 8.5.0 は、数式計算エンジンの柔軟性と拡張性を高めるために、CalculationOptions クラスを公開しました。新しく追加されたクラスには以下のプロパティがあります。 

1. CalculationOptions.CalcStackSize: 再帰的にセルを計算するためのスタックサイズを指定します。-1 は、計算が対応するワークブックの WorkbookSettings.CalcStackSize を使用することを指定します。
1. CalculationOptions.CustomFunction: カスタム数式を使用して数式計算エンジンを拡張します。
1. CalculationOptions.IgnoreError: エラーを隠すべきかどうかを示す真偽値。エラーの原因は、サポートされていない関数、外部リンクなどによる場合があります。
1. CalculationOptions.PrecisionStrategy: 計算の精度処理の戦略を指定する CalculationPrecisionStrategy タイプの値。
### **列挙型 CalculationPrecisionStrategy 追加**
Aspose.Cells for Java 8.5.0 は、選択に応じて期待する結果を得るために、数式計算エンジンに対して柔軟性を高めるために CalculationPrecisionStrategy 列挙型を公開しました。この列挙型は計算精度の処理を戦略付けます。IEEE 754 浮動小数点演算の精度の問題により、見かけ上簡単な数式でも期待通りの結果を得られない場合があるため、最新の API ビルドでは、選択に応じて期待する結果を得るために、以下のフィールドを公開しました。

1. CalculationPrecisionStrategy.DECIMAL: 可能な場合は操作数として 10 進数を使用し、性能の観点からもっとも非効率的です。
1. CalculationPrecisionStrategy.ROUND: 有効桁数に従って計算結果を四捨五入します。
1. CalculationPrecisionStrategy.NONE: 何も戦略を適用しないため、計算中にエンジンはオリジナルの倍精度浮動小数点値を操作数として使用し、結果を直接返します。このオプションは最も効率的であり、ほとんどのケースに適用されます。
### **CalculationOptions を使用するためのメソッドが追加されました**
v8.5.0 のリリースに伴い、Aspose.Cells API は以下にリストされる calculateFormula メソッドのオーバーロードバージョンを追加しました。

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **列挙型 Field PasteType.ROW_HEIGHTS 追加**
Aspose.Cells API は、範囲をコピーする際に行の高さをコピーする目的で PasteType.ROW_HEIGHTS 列挙型フィールドを提供しました。PasteOptions.PasteType プロパティを ((PasteType.ROW_HEIGHTS}} に設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **SheetRender.PageScale プロパティが追加されました**
Microsoft Excel で **n ページの幅 x m ページの高さに適合** オプションを使用してページ設定のスケーリングを設定すると、Microsoft Excel はページ設定のスケーリングファクターを計算します。Aspose.Cells for Java 8.5.0 によって公開された SheetRender.PageScale プロパティを使用することで同じことが実現できます。このプロパティは、パーセンテージ値に変換できる倍精度浮動小数点値を返します。たとえば、0.507968245 が返されると、スケーリングファクターが 51% であることを意味します。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **列挙型 CellValueFormatStrategy 追加**
Aspose.Cells for Java 8.5.0 は、セルの値を書式設定を適用して取得する必要がある場合の対処に新しい列挙型 CellValueFormatStrategy を追加しました。CellValueFormatStrategy 列挙型には以下のフィールドがあります。 

1. CellValueFormatStrategy.CELL_STYLE: セルのオリジナルの書式でのみ書式設定されます。
1. CellValueFormatStrategy.DISPLAY_STYLE: セルの表示スタイルで書式設定されます。
1. CellValueFormatStrategy.NONE: 書式設定されません。
### **Cell.getStringValue メソッドが追加されました**
CellValueFormatStrategy 列挙型を使用するために、v8.5.0 で Cell.getStringValue メソッドが公開されました。これは CellValueFormatStrategy タイプのパラメータを受け入れ、指定されたオプションに応じて値を返します。

以下のコードスニペットは、新しく公開された Cells.getStringValue メソッドの使用方法を示しています。

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
