---
title: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法
type: docs
weight: 2700
url: /ja/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

ファイルを直接読み取ることができない場合や、読み取るべきでない場合があるため、ファイルの形式を検出する必要があることがあります。Aspose.Cellsは、ドキュメントを処理するために使用できる[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index)静的メソッドと関連するAPIを提供しています。

{{% /alert %}}

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
{{< app/cells/assistant language="csharp" >}}
