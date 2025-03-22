---
title: Detect File Format of Encrypted Office Open XML - OOXML Files with C++
linktitle: Detect File Format of Encrypted OOXML Files
type: docs
weight: 340
url: /cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/
description: Learn how to detect the file format of encrypted Office Open XML (OOXML) files using Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

**Office Open XML** (also known as **OOXML** or **Microsoft Open XML** (MOX)) is an XML-based file format developed by Microsoft for representing office documents like spreadsheets, charts, presentations, and word processing documents.

{{% /alert %}} 

Aspose.Cells provides a way to detect the file format of encrypted **Microsoft Open XML** files. To identify the file type, use the [FileFormatUtil.DetectFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) method as shown below in the code example.

```c++
c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"encryptedBook1.out.tmp";

    auto fileStream = MakeObject<Systems::IO::FileStream>(filename, Systems::IO::FileMode::Open);
    auto fileFormatInfo = FileFormatUtil::DetectFileFormat(fileStream, u"1234");

    std::cout << "File Format: " << static_cast<int>(fileFormatInfo->GetFileFormatType()) << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```