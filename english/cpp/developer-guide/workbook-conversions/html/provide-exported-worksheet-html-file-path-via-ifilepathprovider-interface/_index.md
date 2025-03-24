---
title: Provide exported worksheet HTML file path via IFilePathProvider interface with C++
linktitle: Provide exported worksheet HTML file path via IFilePathProvider interface
type: docs
weight: 70
url: /cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
description: Learn how to export worksheets to HTML files and fix broken links using the IFilePathProvider interface in Aspose.Cells with C++.
---

## **Possible Usage Scenarios**
Suppose you have an Excel file with multiple sheets and you want to export each sheet to an individual HTML file. If any of your sheets have links to other sheets, those links will be broken in the exported HTML. To deal with this problem, Aspose.Cells provides the [IFilePathProvider](https://reference.aspose.com/cells/cpp/aspose.cells/ifilepathprovider/) interface, which you can implement to fix the broken links.

## **Provide exported worksheet HTML file path via IFilePathProvider interface**
Please download the [sample Excel file](5115213.zip) used in the following code and its exported HTML files. All these files are inside the Temp directory. You should extract it on the C: drive. Then it will become the C:\Temp directory. You can then open the Sheet1.html file in the browser and click the two links inside it. These links refer to the two exported HTML worksheets, which are inside the C:\Temp\OtherSheets directory.

```plaintext
file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1
file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
```

The following screenshot shows how the C:\Temp\Sheet1.html and its links look like:

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

The following screenshot shows the HTML source. As you can see, the links are now referring to the C:\Temp\OtherSheets directory. This was achieved using the [IFilePathProvider](https://reference.aspose.com/cells/cpp/aspose.cells/ifilepathprovider/) interface.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Sample Code**
Please note that the C:\Temp directory is just for illustration purposes. You can use any directory of your choice and place the [sample Excel file](5115211.xlsx) inside it, then execute the provided sample code. It will create an OtherSheets sub-directory inside your directory and export the second and third worksheets as HTML files inside it. Please change the `dirPath` variable inside the provided code to refer to the directory of your choice before execution.

{{% alert color="primary" %}}

The sample code will only work when you set the Aspose.Cells license. If you try to run the code without setting the license, it will go into an infinite loop. Therefore, we have added a check to print a message and stop execution when the license is not set. You can either purchase a license or request a 30-day temporary license from the Aspose.Purchase team.

{{% /alert %}}

Please note that commenting out these lines inside the code will break the links in Sheet1.html, and Sheet2.html or Sheet3.html will not open when their links are clicked inside Sheet1.html.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    auto options = std::make_shared<HtmlSaveOptions>();
    options->SetFilePathProvider(std::make_shared<FilePathProvider>());

    Aspose::Cells::Cleanup();
}
```

Here is the complete sample code that you can execute with the provided [sample Excel file](5115211.xlsx).

```cpp
#include <iostream>
#include <memory>
#include <system/io/directory.h>
#include <system/io/path.h>
#include <system/environment.h>
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace System::IO;

class FilePathProvider : public IFilePathProvider {
public:
    FilePathProvider() {}

    U16String GetFullName(const U16String& sheetName) override {
        if (sheetName == u"Sheet2") {
            return u"file:///" + u"OtherSheets\\Sheet2.html";
        } else if (sheetName == u"Sheet3") {
            return u"file:///" + u"OtherSheets\\Sheet3.html";
        }
        return u"";
    }
};

void SetLicense(const U16String& dirPath) {
    U16String licPath = dirPath + u"Aspose.Cells.lic";

    License lic;
    lic.SetLicense(licPath);

    std::cout << CellsHelper::GetVersion().ToUtf8() << std::endl;
    System::Diagnostics::Debug::WriteLine(CellsHelper::GetVersion());

    Environment::SetCurrentDirectory(dirPath);
}

void TestFilePathProvider(const U16String& dirPath) {
    // Create subdirectory for second and third worksheets
    Directory::CreateDirectory(dirPath + u"OtherSheets");

    // Load sample workbook from your directory
    Workbook wb(dirPath + u"Sample.xlsx");

    // Save worksheets to separate html files
    // Because of IFilePathProvider, hyperlinks will not be broken.
    for (int i = 0; i < wb.GetWorksheets().GetCount(); i++) {
        // Set the active worksheet to current value of variable i
        wb.GetWorksheets().SetActiveSheetIndex(i);

        // Create html save option
        HtmlSaveOptions options;
        options.SetExportActiveWorksheetOnly(true);
        // If you will comment this line, then hyperlinks will be broken
        options.SetFilePathProvider(new FilePathProvider());
        // Sheet actual index which starts from 1 not from 0
        int sheetIndex = i + 1;

        U16String filePath;

        // Save first sheet to same directory and second and third worksheets to subdirectory
        if (i == 0) {
            filePath = dirPath + u"Sheet1.html";
        } else {
            filePath = dirPath + u"OtherSheets\\Sheet" + U16String::FromInt(sheetIndex) + u"_out.html";
        }

        // Save the worksheet to html file
        wb.Save(filePath, options);
    }
}

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Check if license is set, otherwise do not proceed
    SetLicense(srcDir);

    Workbook wb;
    if (!wb.IsLicensed()) {
        std::cout << "You must set the license to execute this code successfully." << std::endl;
        std::cin.get();
    } else {
        // Test IFilePathProvider interface
        TestFilePathProvider(srcDir);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```