---
title: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法
type: docs
weight: 2700
url: /ja/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

時には、ファイルを開く前にフォーマットを検出する必要があります。ファイル拡張子だけでは内容が適している保証はなく、パスワード保護された暗号化ファイルは直接読めませんし、読むべきではありません。Aspose.Cells for Python via .NETは、[**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format)の静的メソッドと関連APIを提供し、ドキュメントの処理に利用できます。

{{% /alert %}}

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

