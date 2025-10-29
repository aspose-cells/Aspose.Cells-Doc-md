---
title: Безопасные PDF документы с C++
linktitle: Защищенные PDF документы
type: docs
weight: 120
url: /ru/cpp/secure-pdf-documents/
description: Узнайте, как защитить PDF документы с помощью паролей владельца и пользователя, используя Aspose.Cells с C++.
---

{{% alert color="primary" %}}

Иногда разработчикам приходится работать с зашифрованными PDF-файлами. Например:

- Защитите документы паролями владельца и пользователя, чтобы открыть его могли не все.
- Установите ограничения или разрешения для документа после его открытия. например, ограничьте, можно ли печатать или извлекать содержимое документа.

Эта статья объясняет, как передавать параметры безопасности PDF при сохранении электронных таблиц в PDF.

{{% /alert %}}

Aspose.Cells предоставляет [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) для работы с безопасностью. Вы можете установить пароли владельца и пользователя при сохранении в PDF. Пароль владельца или пользователя потребуется для открытия зашифрованного PDF-документа для просмотра.

- Пароль пользователя может быть пустым или содержать пустую строку, в этом случае от пользователя не потребуется пароль при открытии PDF-документа.
- Открытие PDF-документа с правильным паролем владельца обеспечивает полный доступ (без указанных ограничений доступа) к документу.
- Открытие PDF-документа с правильным паролем пользователя (или открытие документа без пароля пользователя) дает ограниченный доступ в соответствии с установленными разрешениями.

Приведенный ниже пример кода описывает, как защищать PDF с помощью Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Если таблица содержит формулы, рекомендуется вызывать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) сразу перед преобразованием в PDF. Это обеспечивает перерасчет значений, зависимых от формул, и правильное отображение в PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
