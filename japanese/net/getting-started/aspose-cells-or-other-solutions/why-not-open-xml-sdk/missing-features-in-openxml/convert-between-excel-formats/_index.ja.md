---
title: Excel形式間の変換
type: docs
weight: 20
url: /ja/net/convert-between-excel-formats/
---

## **ExcelをPDFに変換する**

**PDF** ファイルは、組織、政府セクター、個人間で文書を交換するために広く使用されています。これは標準的なドキュメント形式であり、ソフトウェア開発者は Microsoft Excel ファイルを **PDF** ドキュメントに変換する方法を求められることがあります。
**Aspose.Cells** は、ExcelファイルをPDFに変換し、変換時の視覚的な忠実度を高く維持します。

Aspose.Cells for .NETは他のソフトウェアに依存せずに、表計算からPDFへの変換をサポートします。WorkbookクラスのSaveメソッドを使用して、ExcelファイルをPDF形式に変換します。Saveメソッドは、ネイティブのExcelファイルをPDF形式に変換するSaveFormat.Pdf列挙型メンバを提供します。

スプレッドシートから直接PDFに変換することは、サードパーティのツールや外部APIを使用しないで行うため、いくつかの**利点**があります。

1. 直接変換は一時ファイルを必要としないため、全プロセスをメモリで完了できます。
1. XMLファイルは不要なため、大きなファイルも簡単に変換できます。
1. 変換速度ははるかに速くなります。

**ファイルをPDFに変換するには:**

1. 空のコンストラクタを呼び出してWorkbookクラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたりロードしたりするか、ワークブックをゼロから作成する場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシートで必要な作業（データの入力、書式の適用、数式の設定、画像の挿入など）を行います。
1. スプレッドシートコードが完成したら、WorkbookクラスのSaveメソッドを呼び出して、スプレッドシートを保存します。ファイル形式はPDFであるため、SaveFormat列挙型からPdf（事前定義された値）を選択して最終的なPDFドキュメントを生成します。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **ExcelをMHTMLに変換**

**MHTML** は通常のHTMLと外部リソース（通常はリンクされた画像、アニメーション、音声などのコンテンツ）を1つのファイルに組み合わせたものです。.mhtのファイル拡張子を持つ電子メールで使用されます。
Aspose.CellsはMHTMLファイルの読み書きをサポートしています。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **ExcelをXPSに変換**

時々、複数のワークシートを持つワークブックをテキスト形式に変換または保存したいことがあります。テキスト形式（たとえばTXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelとAspose.Cellsの両方がアクティブなワークシートの内容のみを保存します。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
