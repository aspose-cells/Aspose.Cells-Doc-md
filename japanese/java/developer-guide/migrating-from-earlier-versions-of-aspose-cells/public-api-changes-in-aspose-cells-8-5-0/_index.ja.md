---
title: パブリック API Aspose.Cells 8.5.0 の変更点
type: docs
weight: 170
url: /ja/java/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.4.2 から 8.5.0 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-0/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **ICustomFunction.CalculateCustomFunction パラメータを変更しました**
カスタム関数の 1 つのパラメーターがセル参照である場合、古いバージョン Aspose.Cells では、セル参照を 1 つのセル値または参照領域内のすべてのセル値のオブジェクト配列に変換するために API が使用されていました。ただし、多くの関数とユーザーにとって、参照された領域内のすべてのセルのセル値配列は必要ありません。数式の位置に対応する 1 つのセルが必要なだけか、セル値または値配列の代わりに参照自体が必要なだけです。 .状況によっては、すべてのセル値をフェッチすると、循環参照エラーのリスクが高まることさえありました。

このような要件をサポートするために、Aspose.Cells for Java 8.5.0 では、参照される領域のパラメーター値が「paramsList」に変更されました。 v8.5.0 以降、API は、対応するパラメーターが参照であるか、その計算結果が参照である場合、ReferredArea オブジェクトを「paramsList」に入れるだけです。参照自体が必要な場合は、ReferredArea を直接使用できます。数式の位置に対応する参照から 1 つのセル値を取得する必要がある場合は、ReferredArea.getValue(rowOffset, int colOffset) メソッドを使用できます。領域全体のセル値配列が必要な場合は、ReferredArea.getValues メソッドを使用できます。

Aspose.Cells for Java 8.5.0 は「paramsList」で ReferredArea を提供するため、「contextObjects」の ReferredAreaCollection はもう必要ありません (古いバージョンでは、カスタム関数のパラメーターに常に 1 対 1 のマップを与えることができませんでした)。そのため、このリリースでは「contextObjects」からも削除されました。

この変更により、参照パラメーターの値が必要な場合、ICustomFunction の実装のコードを少し変更する必要があります。

**古い実装**

{{< highlight "csharp" >}}

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

**新しい実装**

{{< highlight "csharp" >}}

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
### **クラス計算オプションが追加されました**
Aspose.Cells for Java 8.5.0 では、CalculationOptions クラスが公開され、数式計算エンジンの柔軟性と拡張性が向上しました。新しく追加されたクラスには、次のプロパティがあります。

1. CalculationOptions.CalcStackSize: セルを再帰的に計算するためのスタック サイズを指定します。 -1 は、計算が対応するワークブックの WorkbookSettings.CalcStackSize を使用することを指定します。
1. CalculationOptions.CustomFunction: 数式計算エンジンをカスタム数式で拡張します。
1. CalculationOptions.IgnoreError: ブール型の値は、数式の計算中にエラーを非表示にするかどうかを示します。エラーは、サポートされていない関数、外部リンクなどが原因である可能性があります。
1. CalculationOptions.PrecisionStrategy: 計算の処理精度の戦略を指定する CalculationPrecisionStrategy 型の値。
### **Enumeration CalculationPrecisionStrategy が追加されました**
Aspose.Cells for Java 8.5.0 では列挙型の CalculationPrecisionStrategy が公開され、数式計算エンジンの柔軟性が向上し、目的の結果が得られます。この列挙は、計算精度の処理を戦略化します。 IEEE 754 Floating-Point Arithmetic の精度の問題により、一見単純な数式の一部が計算されず、期待される結果が得られない場合があるため、最新の API ビルドでは、選択に従って目的の結果が得られるように次のフィールドが公開されています。

1. CalculationPrecisionStrategy.DECIMAL: 可能な場合はオペランドとして 10 進数を使用しますが、パフォーマンスを考慮すると最も非効率的です。
1. CalculationPrecisionStrategy.ROUND: 有効桁数に従って計算結果を丸めます。
1. CalculationPrecisionStrategy.NONE: 戦略は適用されないため、計算中にエンジンは元の double 値をオペランドとして使用し、結果を直接返します。このオプションは最も効率的で、ほとんどの場合に適用できます。
### **CalculationOptions を使用するために追加されたメソッド**
v8.5.0 のリリースに伴い、Aspose.Cells API は、以下に示すように calculateFormula メソッドのオーバーロード バージョンを追加しました。

- Workbook.calculateFormula(計算オプション)
- Worksheet.calculateFormula(CalculationOptions オプション、bool 再帰)
- Cell.calculate(計算オプション)
### **列挙型フィールド PasteType.ROW_HEIGHTS が追加されました**
Aspose.Cells API は PasteType.ROW を提供しました_範囲をコピーしながら行の高さをコピーするための HEIGHTS 列挙型フィールド。 PasteOptions.PasteType プロパティを ((PasteType.ROW_HEIGHTS}} ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

**Java**

{{< highlight "csharp" >}}

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
### **プロパティ SheetRender.PageScale が追加されました**
を使用してページ設定スケーリングを設定すると、**幅 n ページ、高さ m に合わせる**オプション、Microsoft Excel はページ設定倍率を計算します。同じことは、Aspose.Cells for Java 8.5.0 によって公開された SheetRender.PageScale プロパティを使用して実現できます。このプロパティは、パーセント値に変換できる double 値を返します。たとえば、0.507968245 を返す場合、倍率が 51% であることを意味します。

**Java**

{{< highlight "csharp" >}}

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
### **列挙体 CellValueFormatStrategy が追加されました**
Aspose.Cells for Java 8.5.0 では、フォーマットを適用して、または適用せずにセル値を抽出する必要がある状況を処理するために、新しい列挙体 CellValueFormatStrategy が追加されました。列挙体 CellValueFormatStrategy には次のフィールドがあります。

1. CellValueFormatStrategy.CELL_STYLE: セルの元の形式でのみフォーマットされます。
1. CellValueFormatStrategy.DISPLAY_STYLE: セルの表示スタイルでフォーマットされます。
1. CellValueFormatStrategy.NONE: フォーマットされていません。
### **メソッド Cell.getStringValue を追加**
CellValueFormatStrategy 列挙を使用するために、v8.5.0 はタイプ CellValueFormatStrategy のパラメーターを受け入れ、指定されたオプションに依存する値を返す Cell.getStringValue メソッドを公開しました。

次のコード スニペットは、新しく公開された Cells.getStringValue メソッドの使用方法を示しています。

**Java**

{{< highlight "csharp" >}}

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
