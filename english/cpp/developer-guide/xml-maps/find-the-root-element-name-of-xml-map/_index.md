---
title: Find the Root Element Name of XML Map with C++
linktitle: Find the Root Element Name of XML Map
type: docs
weight: 30
url: /cpp/find-the-root-element-name-of-xml-map/
description: Learn how to find the root element name of an XML map using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

You can find the *Root Element Name of Xml Map* using Aspose.Cells with [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) property. The following screenshot shows the root element name of the XML Map in Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Sample Code**

The following sample code loads the [sample Excel file](55541789.xlsx) and accesses the first XML Map and prints its [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/) property. Please see the console output of the sample code given below.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}