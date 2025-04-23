---
title: Aspose.Cells 8.0.0 のパブリックAPI変更
type: docs
weight: 10
url: /ja/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Aspose.Cells 8.0.0 で導入されたパブリックAPIの変更が記載されています。新しく追加されたメソッドや旧形式になったメソッドだけでなく，Aspose.Cells の内部動作に影響を与える変更についても記述されています。

{{% /alert %}} 
## **LoadOptions と WorkbookSettings に MemorySetting プロパティが追加されました。**
Aspose.Cells for .NETのv8.0.0から、パフォーマンスを考慮したメモリ使用オプションを提供しました。MemorySettingプロパティはLoadOptionsおよびWorkbookSettingsクラスで利用可能です。
##### **例**
大きなサイズのExcelファイルの最適なモードでの読み取り方法を示します。

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

大きなデータセットを最適なモードでワークシートに書き込む方法を示します。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

大容量のデータセットを扱う際のメモリの最適化についての詳細な記事は[こちら](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)をご確認ください

{{% /alert %}}
## **Row と Cell の実装が変更されました。**
以前のバージョンでは，Row と Cell オブジェクトはWorksheet内の対応する行とセルを表すためにメモリに保持されました。**RowCollection[int index]** や **Cells[int row, int column]** を取得すると，同じインスタンスが返されました。メモリのパフォーマンスを考慮して，今後はRow と Cell のプロパティとデータのみがメモリに保持されるようになります。したがって，Row および Cell オブジェクトは前述のプロパティのラッパーになります。
### **例**
今後のCellおよびRowオブジェクトを比較する方法を示します。

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Row および Cell オブジェクトは呼び出しに応じてインスタンス化されるため，Cellsコンポーネントによってメモリに保持・管理されることはありません。そのため，挿入や削除の操作の後、Row & Column インデックスが更新されない場合がありますし，これらのオブジェクトが無効になる可能性もあります。
### **例**
例えば、次のコードスニペットは、8.0.0以降を使用すると無効な結果を返します。

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



新しいバージョンでは、Cellオブジェクトが無効になるか、望ましくない値でA2を参照するようになります。このような状況を回避するためには、再びセルのコレクションから行またはセルオブジェクトを取得して正しい結果を取得します。

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollectionは、内部リストにRowオブジェクトがないため、もはやCollectionBaseを継承しません。

{{% /alert %}}
## **Cell.StringValueの動作が変更されました**
以前のバージョンでは、特殊パターン_はセルの値をフォーマットする際に無視され、特殊文字*は常にフォーマットされた結果に1文字を含めていました。しかし、新しいバージョンでは、特殊文字_および*を処理するロジックを変更し、フォーマットされた結果がExcelアプリケーションと同じになるようにしました。たとえば、カスタムセルフォーマット"_(\$* #,##0.00_)"を使用して値123を表すと、以前は"$ 123.00"となりましたが、新しいバージョンではCell.StringValueに"$123.00"となります。
## **PdfSaveOptionsにCreatedTimeを追加しました**
ユーザーは、PdfSaveOptionsクラスを使用してスプレッドシートをPDF形式で保存する際にPDF作成時刻を取得または設定できるようになりました。
## **WorksheetにShowFormulasを追加しました**
以降、ユーザーはワークシートが提供するBooleanプロパティShowFormulasを使用して、与えられたワークシートの数式から値に表示を切り替えることができます。
## **FileFormatTypeにOoxmlを追加しました**
FileFormatTypeクラスに、XLSX、DOCX、PPTXなどのOffice Open XMLファイルを表すための新しい定数Ooxmlが追加されました。
## **AutoFilterのFilterColumnCollectionを廃止しました**
Aspose.Cells for Javaで、FilterColumnCollectionプロパティが廃止されました。AuotFilter.FilterColumnsプロパティを使用することが推奨されています。
## **SeriesCollection.SecondCatergoryDataをSeriesCollection.SecondCategoryDataに置き換えました**
SeriesCollection.SecondCatergoryDataのプロパティ名のタイプミスを修正しました。以降、SeriesCollection.SecondCategoryDataプロパティを使用することができます。元のプロパティSeriesCollection.SecondCatergoryDataは廃止されています。
{{< app/cells/assistant language="csharp" >}}
