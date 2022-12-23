---
title: 出力PDFと画像の文字列の交差方法を指定
type: docs
weight: 120
url: /ja/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **考えられる使用シナリオ**

セルにテキストまたは文字列が含まれているが、セルの幅よりも大きい場合、次の列の次のセルが null または空の場合、文字列はオーバーフローします。 Excel ファイルを PDF/Image に保存する場合、[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)列挙。次の値があります。

- **TextCrossType.Default**: 次のセルに依存する MS Excel のようなテキストを表示します。次のセルが null の場合、文字列が交差するか、切り捨てられます。

- **TextCrossType.CrossKeep**: MS Excel exporting PDF/Image のような文字列を表示します

- **TextCrossType.CrossOverride**: 他のセルと交差してすべてのテキストを表示し、交差したセルのテキストを上書きします

- **TextCrossType.StrictInCell**: セルの幅内に文字列のみを表示します。

## **TextCrossType を使用して、出力 PDF/Image で文字列を交差させる方法を指定します**

次のサンプル コードは、サンプルの Excel ファイルを読み込み、別のファイルを指定して PDF/Image 形式で保存します。[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype).サンプルの Excel ファイルと出力ファイルは、次のリンクからダウンロードできます。

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### サンプルコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
