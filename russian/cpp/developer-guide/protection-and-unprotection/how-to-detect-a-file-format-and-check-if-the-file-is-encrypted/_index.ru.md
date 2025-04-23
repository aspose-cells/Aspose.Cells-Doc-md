---
title: Как определить формат файла и проверить, зашифрован ли файл с помощью C++
linktitle: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2700
url: /ru/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Узнайте, как обнаружить формат файла и проверить, зашифрован ли он, используя Aspose.Cells с C++.
---

{{% alert color="primary" %}}

Иногда необходимо определить формат файла перед его открытием, потому что расширение файла не гарантирует, что содержимое файла подходит. Файл может быть зашифрован (защищен паролем), поэтому его нельзя чита��ь напрямую, или его не следует читать. Aspose.Cells предоставляет статический метод [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) и некоторые связанные API, которые вы можете использовать для обработки документов.

{{% /alert %}}

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

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
