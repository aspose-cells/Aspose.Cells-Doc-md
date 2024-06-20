---
title: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **可能な使用シナリオ**

Aspose.Cellsはすでに署名されたExcelファイルにデジタル署名を追加するための[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection))メソッドを提供します。

{{% alert color="primary" %}}

すでに署名されたExcel文書にデジタル署名を追加する際に、元の文書がAspose.Cellsで生成された文書であれば問題ありません。ただし、元の文書が他のエンジン（例：Microsoft Excelなど）で生成された場合、Aspose.Cellsはファイルを読み込んで再保存した後、元の署名が無効になります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する**

以下のサンプルコードは、すでに署名されたExcelファイルにデジタル署名を追加する[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection))メソッドの使用方法を説明しています。このコードで使用されているサンプルExcelファイルはすでにデジタル署名されています。コードで使用されているデモ証明書名は[AsposeTest.pfx](50528289.pfx)で、パスワードは*aspose*です。スクリーンショットは、コードの実行後のサンプルExcelファイルへの影響を示しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
