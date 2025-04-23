---
title: Bildhyperlinks mit C++ hinzufügen
linktitle: Bild Hyperlinks hinzufügen
type: docs
weight: 140
url: /de/cpp/add-image-hyperlinks/
description: Lernen Sie, wie Sie Bildhyperlinks durch die API Aspose.Cells for C++ hinzufügen.
keywords: Bild Hyperlinks hinzufügen, Bild Hyperlinks einfügen
---

{{% alert color="primary" %}} 

Hyperlinks sind nützlich, um auf Informationen in anderen Arbeitsblättern oder auf Websites zuzugreifen. Microsoft Excel ermöglicht es Benutzern, Hyperlinks in Textzellen und auf Bildern hinzuzufügen. Bild-Hyperlinks können die Navigation in einem Arbeitsblatt erleichtern, zum Beispiel als Schaltflächen für vorherige und nächste Seiten oder Logos, die zu bestimmten Websites verlinken. Dieses Dokument erläutert, wie man Bild-Hyperlinks in einem Arbeitsblatt unter Verwendung von Aspose.Cells einfügt.

{{% /alert %}} 

Aspose.Cells ermöglicht es Ihnen, Hyperlinks zu Bildern in Arbeitsblättern zur Laufzeit hinzuzufügen. Es ist möglich, den Bildschirmtipp und die Adresse des Links festzulegen und zu ändern. Der folgende Beispielscode veranschaulicht, wie man einen Bild-Hyperlink in ein Arbeitsblatt einfügt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
