---
title: Use Custom XML Parts in Aspose.Cells with C++
linktitle: Use Custom XML Parts
type: docs
weight: 390
url: /cpp/use-custom-xml-parts-in-aspose-cells/
description: Learn how to use custom XML parts in Excel files programmatically using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Using Custom XML Parts in Aspose.Cells

Custom XML Parts are XML data stored by different applications like SharePoint inside an Excel file. This data is consumed by various applications that require it. Microsoft Excel does not use this data, so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** to **.zip** and then opening it using **WinZip**. You can also open the ZIP file using any third-party Windows zip utility such as WinRAR or WinZip. The data is present inside the **customXml** folder.

You can add custom XML parts using Aspose.Cells via the [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) method.

The following sample code uses the [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) method to add the **Book Catalog XML**, and its name is **BookStore**. The following image shows the result of this code. As you can see, the Book Catalog XML is added inside the BookStore node, which is the name of this property.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++ Code to Use Custom XML Parts

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Related Article

- [Adding Custom Properties Visible Inside Document Information Panel](/cells/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
