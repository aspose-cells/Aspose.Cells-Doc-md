---
title: ファイル形式を検出し、ファイルが暗号化されているかどうかを確認する方法
type: docs
weight: 2700
url: /ja/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

ファイル拡張子はファイルの内容が適切であるとは限らないため、ファイルを開く前にファイルの形式を検出する必要がある場合があります。ファイルは暗号化されている可能性があり (パスワードで保護されたファイル)、直接読み取ることができないか、読み取るべきではありません。 Aspose.Cells は[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index)ドキュメントを処理するために使用できる静的メソッドといくつかの関連 API が含まれています。

{{% /alert %}}

次のサンプル コードは、(ファイル パスを使用して) ファイル形式を検出し、その拡張子を確認する方法を示しています。ファイルが暗号化されているかどうかを判断することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
