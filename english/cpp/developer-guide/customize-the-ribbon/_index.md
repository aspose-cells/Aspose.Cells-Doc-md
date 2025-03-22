---
title: Customizing the Ribbon XML with C++
linktitle: Customize Excel Menu
type: docs
weight: 1500
url: /cpp/customizing-the-ribbon-xml/
description: Learn how to customize the Ribbon XML in Excel files using Aspose.Cells with C++.
---

{{% alert color="primary" %}} 

Microsoft Office replaced menus and toolbars with a Ribbon at the top of the application window since Office 2007. The Ribbon is customizable. 
Aspose.Cells allows you to:

- Keep Ribbon XML without parsing it,
- Read and write Ribbon XML without parsing it,
- Get and set Ribbon XML data.

If you want to change the Ribbon XML, you have to parse it with an XML parser or other Ribbon XML tool.

{{% /alert %}} 

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook wb(srcDir + u"aspose-sample.xlsx");

    // Open CustomUI.xml file
    std::ifstream file((srcDir + u"CustomUI.xml").ToUtf8());
    if (!file.is_open())
    {
        std::cerr << "Failed to open CustomUI.xml" << std::endl;
        return -1;
    }

    // Read the entire content of the file
    std::string ribbonXml((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // Set the Ribbon XML to the workbook
    wb.SetRibbonXml(U16String::FromUtf8(ribbonXml));

    std::cout << "Ribbon XML set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```