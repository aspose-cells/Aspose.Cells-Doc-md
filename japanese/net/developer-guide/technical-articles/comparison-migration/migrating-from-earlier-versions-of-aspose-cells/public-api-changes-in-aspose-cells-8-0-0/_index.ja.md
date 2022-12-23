---
title: パブリック API Aspose.Cells 8.0.0 の変更点
type: docs
weight: 10
url: /ja/net/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

このページには、Aspose.Cells 8.0.0 で導入されたパブリック API の変更がリストされています。これには、新しいパブリック メソッドと廃止されたパブリック メソッドだけでなく、既存のコードに影響を与える可能性のある Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **LoadOptions & WorkbookSettings に MemorySetting を追加**
Aspose.Cells for .NET の v8.0.0 から、パフォーマンスを考慮してメモリ使用オプションを提供しています。 LoadOptions & WorkbookSettings クラスで MemorySetting プロパティを使用できるようになりました。
##### **例**
最適化モードで Excel ファイル (サイズが大きい) を読み取る方法を示します。

**C#**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

最適化モードで大規模なデータセットをワークシートに書き込む方法を示します。

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

の詳細記事をご確認ください[大きなファイルを操作する際のメモリの最適化](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Row & Cell の実装が変更されました**
以前のバージョンでは、Row オブジェクトと Cell オブジェクトは、ワークシートの対応する行とセルを表すためにメモリに保持されていました。常に同じインスタンスが返されました**RowCollection[int インデックス]**また**Cells[整数行、整数列]**が取得されました。メモリのパフォーマンスを考慮して、これ以降、Row と Cell のプロパティとデータのみがメモリに保持されます。したがって、Row & Cell オブジェクトは、前述のプロパティのラッパーになります。
### **例**
これから Cell と Row オブジェクトを比較する方法を示します。

**C#**

{{< highlight "csharp" >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Row オブジェクトと Cell オブジェクトは呼び出しに従ってインスタンス化されるため、Cells コンポーネントによってメモリ内に保持および管理されることはありません。したがって、いくつかの挿入および削除操作の後、行と列のインデックスが更新されないか、さらに悪いことに、これらのオブジェクトが無効になることがあります。
### **例**
たとえば、次のコード スニペットは、8.0.0 以降を使用すると無効な結果を返します。

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



新しいバージョンでは、Cell オブジェクトが無効になるか、不要な値で A2 を参照します。このような状況を回避するには、セル コレクションから Row または Cell オブジェクトを再度取得して、正しい結果を取得します。

**C#**

{{< highlight "csharp" >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

内部リストに Row オブジェクトがないため、RowCollection は CollectionBase を継承しません。

{{% /alert %}}
## **Cell.StringValue の動作が変更されました**
以前のバージョンでは、特殊なパターン_は、セル値の書式設定中に無視されました。特殊文字 * は、書式設定された結果に常に 1 文字を生成しました。このバージョンから、特殊文字を処理するロジックを変更しました_と*書式設定された結果を Excel アプリケーションと同じにするため。たとえば、カスタム セル形式 "_(\$* #,##0.00_)" を使用して値 123 を表すと、結果は "$ 123.00" になります。新しいバージョンでは、Cell.StringValue に結果が "$123.00" として含まれます。これは、セルのコピー中に Excel アプリケーションが示す動作と同じです。テキストまたは CSV にエクスポートします。
## **CreatedTime を PdfSaveOptions に追加**
ユーザーは、PdfSaveOptions クラスを使用してスプレッドシートを PDF に保存する際に、PDF の作成時刻を取得または設定できるようになりました。
## **ワークシートに ShowFormulas を追加**
これ以降、ユーザーは Worksheet が提供するブール型プロパティ ShowFormulas を使用して、ビューを式から特定のワークシートの値に変更できます。
## **FileFormatType に Ooxml を追加**
新しい定数 Ooxml が FileFormatType クラスに追加され、XLSX、DOCX、PPTX などの暗号化された Office オープン XML ファイルを表します。
## **AutoFilter の廃止された FilterColumnCollection**
Aspose.Cells for Java により、FilterColumnCollection プロパティは廃止されました。代わりに AutoFilter.FilterColumns プロパティを使用することをお勧めします。
## **SeriesCollection.SecondCategoryData を SeriesCollection.SecondCategoryData に置き換えました**
SeriesCollection.SecondCatergoryData のプロパティ名のタイプミスを基本的に修正しました。元のプロパティ SeriesCollection.SecondCategoryData は廃止されているのに対し、今後は SeriesCollection.SecondCategoryData プロパティを使用できます。
