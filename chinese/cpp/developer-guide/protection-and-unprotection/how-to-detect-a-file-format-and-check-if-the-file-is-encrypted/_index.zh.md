---
title: 如何检测文件格式并使用 C++ 判断文件是否被加密
linktitle: 如何检测文件格式并检查文件是否已加密
type: docs
weight: 2700
url: /zh/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: 学习如何用 Aspose.Cells 和 C++检测文件格式及判断文件是否被加密。
---

{{% alert color="primary" %}}

 有时你需要在打开文件之前检测文件格式，因为文件扩展名不能保证文件内容的正确性。文件可能已加密（密码保护的文件），不能直接读取，或者不应读取。Aspose.Cells 提供了 [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) 静态方法及相关API，可用来处理文档。

{{% /alert %}}

以下示例代码说明如何通过文件路径检测文件格式并检查其扩展名。您还可以确定该文件是否已加密。

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
