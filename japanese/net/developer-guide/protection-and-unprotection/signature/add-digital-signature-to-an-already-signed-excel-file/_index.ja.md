---
title: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/net/add-digital-signature-to-an-already-signed-excel-file/
description: この記事では、Aspose.Cells for .Netを使用してC#コードですでに署名されたExcelファイルにデジタル署名を追加する方法について説明します。
keywords: すでに署名されたExcelファイルにデジタル署名を追加する方法
---

## **可能な使用シナリオ**

Aspose.Cellsは、すでに署名されたExcelファイルにデジタル署名を追加するために使用できる[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)メソッドを提供します。

{{% alert color="primary" %}}

すでに署名されたExcel文書にデジタル署名を追加する際に、元の文書がAspose.Cellsで生成された文書であれば問題ありません。ただし、元の文書が他のエンジン（例：Microsoft Excelなど）で生成された場合、Aspose.Cellsはファイルを読み込んで再保存した後、元の署名が無効になります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する方法**

次のサンプルコードは、[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)メソッドを使用してすでに署名されたExcelファイルにデジタル署名を追加する方法を示しています。このコードで使用されているサンプルExcelファイルについては、[サンプルExcelファイル](50528280.xlsx)をご確認ください。このファイルはすでにデジタルで署名されています。コードでデモ証明書である[AsposeDemo.pfx](50528279.pfx)を使用し、そのパスワードは **aspose** です。スクリーンショットは、コードの実行後にサンプルExcelファイルに与える効果を示しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
