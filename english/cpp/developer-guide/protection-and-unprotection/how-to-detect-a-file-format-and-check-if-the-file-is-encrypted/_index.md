---
title: How to Detect a File Format and Check if the File is Encrypted with C++
linktitle: How to Detect a File Format and Check if the File is Encrypted
type: docs
weight: 2700
url: /cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Learn how to detect a file's format and check if it is encrypted using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes you need to detect a file's format before opening it because the file extension does not guarantee that the file content is appropriate. The file might be encrypted (a password-protected file) so it can't be read directly, or we should not read it. Aspose.Cells provides the [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) static method and some relevant APIs that you can use to process documents.

{{% /alert %}}

The following sample code illustrates how to detect a file format (using the file path) and check its extension. You can also determine whether the file is encrypted.

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