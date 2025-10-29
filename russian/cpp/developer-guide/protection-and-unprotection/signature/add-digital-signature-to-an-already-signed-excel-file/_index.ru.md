---
title: Добавить цифровую подпись к уже подписанному файлу Excel с помощью C++
linktitle: Добавить цифровую подпись к уже подписанному файлу Excel
type: docs
weight: 20
url: /ru/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Узнайте, как добавлять цифровые подписи к подписанным файлам Excel с помощью Aspose.Cells for C++. Обеспечьте целостность документа с помощью нескольких подписей.
keywords: Добавить цифровую подпись к уже подписанному файлу Excel, цифровые подписи на C++, безопасность документа Excel
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет метод [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) для добавления цифровых подписей к уже подписанным файлам Excel.

{{% alert color="primary" %}}

Обратите внимание при добавлении цифровой подписи к уже подписанному документу Excel: если исходный документ был создан Aspose.Cells, он работает правильно. Однако, если документ создан другими движками (например, Microsoft Excel), Aspose.Cells for C++ не может сохранить точную структуру файла после загрузки и повторного сохранения, что может привести к недействительности существующих подписей.

{{% /alert %}}

## **Как добавить цифровую подпись к уже подписанному файлу Excel**

Следующий пример показывает использование [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) для добавления цифровых подписей в подписанные файлы Excel. Предварительно подписанный пример файла Excel [50528280.xlsx](50528280.xlsx). Итоговый файл [50528281.xlsx](50528281.xlsx) показывает результат. Мы используем демонстрационный сертификат [AsposeDemo.pfx](50528279.pfx) с паролем **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
