---
title: Support for XAdES Signature with C++
linktitle: Support for XAdES Signature
type: docs
weight: 110
url: /cpp/support-for-xades-signature/
description: This article describes Support for XAdES Signature using C++ codes with Aspose.Cells for C++.
keywords: Support for XAdES Signature, How to sign Excel with XAdES Signature, How to add XAdES signature.
---

## **Introduction**

Aspose.Cells provides support for signing workbooks with XAdES Signature. For this, the API provides the [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) class and the [**XAdESType**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/xadestype/) enumeration.

## **How to Add XAdES Signature for Excel**

The following code snippet demonstrates the use of the [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) class to sign the [source](101089323.xlsx) workbook.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"sourceFile.xlsx");

    // Password for the PFX file
    U16String password(u"pfxPassword");

    // Path to the PFX file
    U16String pfxFile(u"pfxFile");

    // Read PFX file into a byte vector
    Vector<uint8_t> pfxData;
    // Assuming a function to read file into byte vector exists
    // pfxData = ReadFileToByteVector(pfxFile);

    // Create digital signature
    DigitalSignature signature(pfxData, password, u"testXAdES", Date::Now());

    // Set XAdES type
    signature.SetXAdESType(XAdESType::XAdES);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    // Set digital signature to the workbook
    workbook.SetDigitalSignature(dsCollection);

    // Save the workbook
    workbook.Save(outDir + u"XAdESSignatureSupport_out.xlsx");

    std::cout << "Digital signature added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```