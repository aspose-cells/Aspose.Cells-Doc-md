---
title: Different Ways to Open Files with C++
linktitle: Different Ways to Open Files
type: docs
weight: 10
url: /cpp/different-ways-to-open-files/
description: This article explains how to open an Excel file using Aspose.Cells for C++ API.
keywords: C++ Open an Excel file without Excel, How do I open an Excel File.
---

{{% alert color="primary" %}}

With Aspose.Cells, it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **How to Open an Excel File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook object and open the Excel file using its file path
    Workbook workbook1(inputFilePath);

    std::cout << "Workbook opened using path successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **How to Open an Excel File via a Stream**

It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

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
    U16String inputFilePath = srcDir + u"Book2.xls";

    // Create a Workbook object, open the file from a file path
    Workbook workbook(inputFilePath);

    std::cout << "Workbook opened using stream successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **How to Open a File with Data only**

To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and [**LoadFilter**](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) classes to set the related attribute and options of the classes for the template file to be loaded.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Xlsx);

    // Set LoadFilter property to load only data & cell formatting
    LoadFilter loadFilter(LoadDataFilterOptions::CellData);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create a Workbook object and open the file from its path
    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook book(inputFilePath, loadOptions);

    std::cout << "File data imported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **How to Load Visible Sheets only**

While loading a [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), sometimes you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom function that inherits the [**LoadFilter**](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/) class and pass its instance to [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/loadfilter/) property.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class CustomLoad : public LoadFilter {
public:
    CustomLoad() : LoadFilter(LoadDataFilterOptions::All) {}

    Vector<int32_t> GetSheetsInLoadingOrder() override {
        // Load all sheets in order
        return {0, 1, 2};
    }

    void StartSheet(Worksheet& sheet) override {
        // Custom logic for starting sheet loading
        std::cout << "Loading sheet: " << sheet.GetName().ToUtf8() << std::endl;
    }
};

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String samplePath = outDir + u"output.xlsx";

    // Create a sample workbook and put some data in first cell of all 3 sheets
    Workbook createWorkbook;
    createWorkbook.GetWorksheets().Get(u"Sheet1").GetCells().Get(u"A1").SetValue(u"Aspose");
    createWorkbook.GetWorksheets().Add(u"Sheet2").GetCells().Get(u"A1").SetValue(u"Aspose");
    createWorkbook.GetWorksheets().Add(u"Sheet3").GetCells().Get(u"A1").SetValue(u"Aspose");
    createWorkbook.GetWorksheets().Get(u"Sheet3").SetVisible(false);
    createWorkbook.Save(samplePath);

    // Load the sample workbook with custom load options
    LoadOptions loadOptions;
    CustomLoad customLoad;
    loadOptions.SetLoadFilter(&customLoad);

    Workbook loadWorkbook(samplePath, loadOptions);
    std::cout << "Sheet1: A1: " << loadWorkbook.GetWorksheets().Get(u"Sheet1").GetCells().Get(u"A1").GetStringValue().ToUtf8() << std::endl;
    std::cout << "Sheet2: A1: " << loadWorkbook.GetWorksheets().Get(u"Sheet2").GetCells().Get(u"A1").GetStringValue().ToUtf8() << std::endl;
    std::cout << "Sheet3: A1: " << loadWorkbook.GetWorksheets().Get(u"Sheet3").GetCells().Get(u"A1").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Here is the implementation of the *CustomLoad* class referenced in the above snippet.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoad : public LoadFilter
{
public:
    CustomLoad() : LoadFilter() {}
    explicit CustomLoad(LoadDataFilterOptions opts) : LoadFilter(opts) {}

    void StartSheet(Worksheet& sheet) override
    {
        if (sheet.IsVisible())
        {
            // Load everything from visible worksheet
            SetLoadDataFilterOptions(LoadDataFilterOptions::All);
        }
        else
        {
            // Load nothing
            SetLoadDataFilterOptions(LoadDataFilterOptions::Structure);
        }
    }
};
```

{{% alert color="primary" %}}

An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

There are fair chances that the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) constructor may throw *std::bad_alloc* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory; therefore, the spreadsheet has to be loaded while enabling the Memory Preferences.

{{% /alert %}}