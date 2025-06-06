---
title: Digitally Sign a VBA Code Project with Certificate in C++
linktitle: Digitally Sign a VBA Code Project with Certificate
type: docs
weight: 110
url: /cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Learn how to digitally sign your VBA code project using Aspose.Cells for C++ with a certificate.
---

{{% alert color="primary" %}} 

You can digitally sign your VBA code project using Aspose.Cells with its [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) method. Please follow these steps to check if your Excel file is digitally signed with a certificate.

- Click **Visual Basic** from the **Developer** tab to open **Visual Basic for Applications IDE**.
- Click **Tools** > **Digital Signatures...**  of **Visual Basic for Applications IDE**.

It will show the **Digital Signature Form** indicating whether the document is digitally signed with a certificate or not.

{{% /alert %}} 

## **Digitally Sign a VBA Code Project with Certificate in C++**

The following sample code illustrates how to use the [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) method. Here are the input and output files of the sample code. You can use any Excel file and any certificate to test this code.

- [Source Excel file](5115028.xlsm) used in the sample code.
- [Sample pfx file](5115039.pfx) to create Digital Signature. Please install it on your computer to run this code. Its password is 1234.
- [Output Excel file](5115029.xlsm) generated by the sample code.

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```