---
title: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法
type: docs
weight: 2000
url: /ja/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

ファイルの拡張子だけでファイルの形式を特定することができないまたは直接読み込めない（パスワードで保護されている）場合、ファイルの形式を特定する必要があることがあります。Aspose.Cellsは、[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat-java.io.InputStream-)静的メソッドおよびそれに関連するAPIを提供しており、これらを使用してドキュメントを処理することができます。

{{% /alert %}}

## **Javaコードでファイル形式を検出し、ファイルが暗号化されているかどうかをチェックする**

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
{{< app/cells/assistant language="java" >}}
