---
title: Excel 形式間の変換
type: docs
weight: 20
url: /ja/net/convert-between-excel-formats/
---
## **Excel を PDF に変換する**

**PDF**ファイルは、組織、政府部門、および個人の間でドキュメントを交換するために広く使用されています。これは標準的なドキュメント形式であり、ソフトウェア開発者は Microsoft Excel ファイルを**PDF**ドキュメント。
**Aspose.Cells**は、Excel ファイルを PDF に変換することをサポートし、変換で高い視覚的忠実度を維持します。

Aspose.Cells for .NET は、他のソフトウェアとは独立してスプレッドシートから PDF への変換をサポートします。 Workbook クラスの Save メソッドを使用して、Excel ファイルを PDF に保存します。 Save メソッドは、ネイティブ Excel ファイルを PDF 形式に変換する SaveFormat.Pdf 列挙型メンバーを提供します。

**変換中**サードパーティのツールや外部の API を使用する代わりに、スプレッドシートから直接 PDF に**利点**:

1. 直接変換では、プロセス全体をメモリ内で実行できるため、一時ファイルは必要ありません。
1. XML ファイルが不要なため、大きなファイルを簡単に変換できます。
1. 変換速度ははるかに高速です。

**ファイルを PDF に変換するには:**

1. のオブジェクトをインスタンス化する**ワークブック**空のコンストラクターを呼び出してクラスを作成します。
1. してもいいです**開く/ロードする**既存のテンプレート ファイルを使用するか、ワークブックを最初から作成する場合はこの手順をスキップします。
1. Aspose.Cells' API を使用して、スプレッドシートで目的の作業 (データの入力、書式の適用、数式の設定、画像やその他の描画オブジェクトの挿入など) を実行します。
1. スプレッドシート コードが完成したら、**Workbook クラスの Save メソッド**スプレッドシートを保存します。ファイル形式は PDF である必要があるため、SaveFormat 列挙から Pdf (定義済みの値) を選択して、最終的な PDF ドキュメントを生成します。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Excel を MHTML に変換する**

**MHTML**通常の HTML を外部リソース (つまり、画像、アニメーション、オーディオなど、通常はリンクされるコンテンツ) と組み合わせて 1 つのファイルにします。これらは、ファイル拡張子が .mht の電子メールに使用されます。
Aspose.Cells は、MHTML ファイルの読み取りと書き込みをサポートします。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Excel を XPS に変換する**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存する必要があります。テキスト形式 (例: TXT、TabDelim、CSV など) の場合、既定では、Microsoft Excel と Aspose.Cells の両方で、アクティブなワークシートの内容のみが保存されます。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
