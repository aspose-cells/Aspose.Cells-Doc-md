---
title: Insert Background Image to Excel with C++
linktitle: Insert Background Image to Excel
type: docs
weight: 90
url: /cpp/insert-background-image-to-excel/
description: "How to insert background image to Excel using Aspose.Cells for C++."
---

{{% alert color="primary" %}} 

You can make a worksheet more appealing by adding a picture as a worksheet background. This feature can be quite effective if you have a special corporate graphic that adds a hint of the background without obscuring the data on the sheet. You can set background picture for a sheet using Aspose.Cells API.

{{% /alert %}} 

## **Setting Sheet Background in Microsoft Excel**

To set a sheet's background image in Microsoft Excel (for example, Microsoft Excel 2019):

1. From the **Page Layout** menu, find the **Page Setup** option, and then click the **Background** option.
1. Select a picture to set the sheet's background picture.

   **Setting a sheet background**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Setting Sheet Background with Aspose.Cells**

The code below sets a background image using an image from a stream.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Read the background image file
    std::ifstream file("background.jpg", std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Failed to open background image file." << std::endl;
        return -1;
    }

    file.seekg(0, std::ios::end);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size) {
        std::cerr << "Failed to read background image file." << std::endl;
        return -1;
    }

    // Set the background image for the worksheet
    sheet.SetBackgroundImage(buffer);

    // Save the Excel file
    workbook.Save(u"outputBackImageSheet.xlsx");

    // Save the HTML file
    workbook.Save(u"outputBackImageSheet.html", SaveFormat::Html);

    std::cout << "Files saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Related Articles

- [Working with Background in ODS Files](/cells/cpp/working-with-background-in-ods-files/)