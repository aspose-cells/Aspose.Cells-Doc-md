---
title: Aspose.Cells 8.0.0 のパブリックAPI変更
type: docs
weight: 20
url: /ja/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Aspose.Cells 8.0.0 で導入されたパブリックAPIの変更が記載されています。新しく追加されたメソッドや旧形式になったメソッドだけでなく，Aspose.Cells の内部動作に影響を与える変更についても記述されています。

{{% /alert %}} 
## **LoadOptions と WorkbookSettings に MemorySetting プロパティが追加されました。**
Aspose.Cells for Javaのv8.0.1からは，パフォーマンスを考慮したメモリ使用オプションが提供されています。MemorySetting プロパティはLoadOptions と WorkbookSettings クラスで利用可能です。
### **例**
大きなサイズのExcelファイルの最適なモードでの読み取り方法を示します。

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

大きなデータセットを最適なモードでワークシートに書き込む方法を示します。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

大きなデータセットを扱う際のメモリの最適化に関する詳細な記事は[大容量データを扱う際のメモリ最適化](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)を参照してください。

{{% /alert %}}
## **Row と Cell の実装が変更されました。**
以前のバージョンでは，Row と Cell オブジェクトはWorksheet内の対応する行とセルを表すためにメモリに保持されました。**RowCollection[int index]** や **Cells[int row, int column]** を取得すると，同じインスタンスが返されました。メモリのパフォーマンスを考慮して，今後はRow と Cell のプロパティとデータのみがメモリに保持されるようになります。したがって，Row および Cell オブジェクトは前述のプロパティのラッパーになります。
### **例**
今後のCellおよびRowオブジェクトを比較する方法を示します。

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Row および Cell オブジェクトは呼び出しに応じてインスタンス化されるため，Cellsコンポーネントによってメモリに保持・管理されることはありません。そのため，挿入や削除の操作の後、Row & Column インデックスが更新されない場合がありますし，これらのオブジェクトが無効になる可能性もあります。
### **例**
例えば、次のコードスニペットは、8.0.0以降を使用すると無効な結果を返します。

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

新しいバージョンでは、Cellオブジェクトが無効になるか、望ましくない値でA2を参照するようになります。このような状況を回避するためには、再びセルのコレクションから行またはセルオブジェクトを取得して正しい結果を取得します。

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollectionは、内部リストにRowオブジェクトがないため、もはやCollectionBaseを継承しません。

{{% /alert %}}
## **Cell.StringValueの動作が変更されました**
以前のバージョンでは、特別なパターン _ はセルの値のフォーマット時に無視されていましたが、特別文字 * は常にフォーマットされた結果に1文字を生成しました。このバージョンからは、特別文字 _ と * を処理する論理を変更し、フォーマットされた結果をExcelアプリケーションと同じにします。例えば、カスタムセルフォーマット "_(\$* #,##0.00_)" は値123を"$ 123.00"として表示していましたが、新しいバージョンでは、Cell.StringValueに"$123.00"として表示されます。これは、セルをテキストにコピーするかCSVにエクスポートする際にExcelアプリケーションが示す動作と同じです。
## **PdfSaveOptionsにCreatedTimeを追加しました**
ユーザーは、PdfSaveOptionsクラスを使用してスプレッドシートをPDF形式で保存する際にPDF作成時刻を取得または設定できるようになりました。
## **WorksheetにShowFormulasを追加しました**
今後、ユーザーは、Worksheetが提供するBooleanプロパティShowFormulasを使用して、指定されたワークシートの表示を式や値の間で切り替えることができます。
## **FileFormatTypeにOoxmlを追加しました**
FileFormatTypeクラスに、XLSX、DOCX、PPTXなどのOffice Open XMLファイルを表すための新しい定数Ooxmlが追加されました。
## **AutoFilterのFilterColumnCollectionを廃止しました**
Aspose.Cells for JavaでgetFilterColumnCollectionメソッドが廃止されました。AuotFilter.getFilterColumnsメソッドを代わりに使用することが推奨されています。
## **SeriesCollection.SecondCatergoryDataをSeriesCollection.SecondCategoryDataに置き換えました**
SeriesCollection.getSecondCatergoryDataのメソッド名のタイプミスを修正しました。以降、SeriesCollection.getSecondCategoryDataメソッドを使用することができます。一方、元のメソッドSeriesCollection.getSecondCatergoryDataが廃止されました。
