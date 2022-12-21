---
title: ファイル形式を検出し、ファイルが暗号化されているかどうかを確認する方法
type: docs
weight: 2000
url: /ja/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

ファイル拡張子はファイルの内容が適切であるとは限らないため、ファイルを開く前にファイルの形式を検出する必要がある場合があります。ファイルは暗号化されている可能性があり (パスワードで保護されたファイル)、直接読み取ることができないか、読み取るべきではありません。 Aspose.Cells は[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)静的メソッドと、ドキュメントの処理に使用できるいくつかの関連 API です。

{{% /alert %}}

## **Java ファイル形式を検出し、ファイルが暗号化されているかどうかを確認するコード**

次のサンプル コードは、(ファイル パスを使用して) ファイル形式を検出し、その拡張子を確認する方法を示しています。ファイルが暗号化されているかどうかを判断することもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
