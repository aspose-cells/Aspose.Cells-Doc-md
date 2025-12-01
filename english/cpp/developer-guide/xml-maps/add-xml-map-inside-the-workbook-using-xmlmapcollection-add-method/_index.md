---
title: Add XML Map inside the Workbook using XmlMapCollection.Add method with C++
linktitle: Add XML Map inside the Workbook using XmlMapCollection.Add method
type: docs
weight: 10
url: /cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Add XML Map inside the workbook using XmlMapCollection.Add method with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells provides [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) method which you can use to import your XML Map inside the workbook.

## **Add XML Map inside the Workbook using XmlMapCollection.Add method**

The following sample code adds XML Map inside the workbook using the [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) method and saves it as [output excel file](5115434.xlsx). The screenshot shows the XML Map that has been imported from the [sample.xml](5115433.xml) inside the output excel file.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
