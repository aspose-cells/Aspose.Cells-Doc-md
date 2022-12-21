---
title: 署名済みの Excel ファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **考えられる使用シナリオ**

Aspose.Cells は[**Workbook.addDigitalSignature(デジタル署名コレクション デジタル署名コレクション)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) メソッドを使用して、署名済みの Excel ファイルにデジタル署名を追加できます。

{{% alert color="primary" %}}

元のドキュメントが Aspose.Cells で生成されたドキュメントである場合、署名済みの Excel ドキュメントにデジタル署名を追加する際に注意してください。ただし、元のドキュメントが他のエンジン (例: Microsoft Excel など) によって生成された場合、Aspose.Cells は、ファイルを読み込んで再保存した後、ファイルを同じ状態に保つことができず、元の署名が無効になります。

{{% /alert %}}

## **署名済みの Excel ファイルにデジタル署名を追加する**

次のサンプル コードは、[**Workbook.addDigitalSignature(デジタル署名コレクション デジタル署名コレクション)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) メソッドを使用して、署名済みの Excel ファイルにデジタル署名を追加します。を確認してください[サンプル Excel ファイル](50528287.xlsx)このコードで使用されます。このファイルはすでにデジタル署名されています。を確認してください[出力エクセルファイル](50528288.xlsx)コードによって生成されます。という名前のデモ証明書を使用しました[AsposeTest.pfx](50528289.pfx)パスワードを持つこのコードで*アポーズ*.スクリーンショットは、実行後のサンプル Excel ファイルに対するサンプル コードの効果を示しています。

![todo:画像_代替_文章](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
