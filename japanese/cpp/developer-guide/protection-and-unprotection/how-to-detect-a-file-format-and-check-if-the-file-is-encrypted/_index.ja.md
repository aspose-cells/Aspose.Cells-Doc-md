---
title: ファイル形式を検出し、C++を使用してファイルが暗号化されているかどうかを確認する方法
linktitle: ファイルフォーマットを検出してファイルが暗号化されているかどうかをチェックする方法
type: docs
weight: 2700
url: /ja/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Aspose.Cellsを使用して、C++でファイルの形式を検出し、それが暗号化されているかどうかを確認する方法を学びます。
---

{{% alert color="primary" %}}

時には、ファイルの拡張子だけでは内容が適切であると保証できないため、ファイルを開く前にファイルの形式を検出する必要があります。ファイルは暗号化（パスワード保護されたファイル）されている可能性があり、直接読み取れない場合や、読み取るべきでない場合もあります。Aspose.Cellsは、ドキュメント処理に使用できる[**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/)静的メソッドといくつかの関連APIを提供します。

{{% /alert %}}

次のサンプルコードは、ファイルパスを使用してファイルの形式を検出し、その拡張子をチェックし、ファイルが暗号化されているかどうかを判断する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Detect file format
    FileFormatInfo info = FileFormatUtil::DetectFileFormat(srcDir + u"Book1.xlsx");

    // Gets the detected load format
    std::cout << "The spreadsheet format is: " << FileFormatUtil::LoadFormatToExtension(info.GetLoadFormat()).ToUtf8() << std::endl;

    // Check if the file is encrypted
    std::cout << "The file is encrypted: " << (info.IsEncrypted() ? "true" : "false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
