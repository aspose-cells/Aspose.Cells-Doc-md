---
title: Setting ScaleCrop and LinksUpToDate Properties of Built-In Document Properties with C++
linktitle: Setting ScaleCrop and LinksUpToDate Properties
type: docs
weight: 320
url: /cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Learn how to set ScaleCrop and LinksUpToDate properties of built-in document properties using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) and [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) are two extended built-in document properties defined inside the OpenXml format. The purpose of these properties are as follows:

## **1) ScaleCrop**
This element indicates the display mode of the document thumbnail. Set this element to **TRUE** to enable scaling of the document thumbnail to the display. Set this element to **FALSE** to enable cropping of the document thumbnail to show only sections that fit the display.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **2) LinksUpToDate**
This element indicates whether hyperlinks in a document are up-to-date. Set this element to **TRUE** to indicate that hyperlinks are updated. Set this element to **FALSE** to indicate that hyperlinks are outdated.

The possible values for this element are defined by the W3C XML Schema boolean datatype.

## **Screenshot showing these properties inside the app.xml file**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Setting ScaleCrop and LinksUpToDate Properties of Built-In Document Properties**
The following sample code sets the [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) and [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) extended built-in document properties of the workbook. Please check the [output excel file](5115500.xlsx) generated with this code, change its extension to .zip and extract its contents and view the app.xml as shown in the screenshot above.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create directory if it is not already present.
    if (!System::IO::Directory::Exists(outDir))
    {
        System::IO::Directory::CreateDirectory(outDir);
    }

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```