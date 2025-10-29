---
title: 使用C++移除Excel文件中工作表的现有PrinterSettings
linktitle: 移除工作表的现有PrinterSettings
type: docs
weight: 60
url: /zh/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 学习如何通过Aspose.Cells的Page Setup对象，使用C++以编程方式移除Excel文件中工作表的现有PrinterSettings。
keywords: 用C++移除工作表的打印设置，移除Excel工作表的打印设置
---

## **可能的使用场景**
有时开发人员希望阻止Excel在保存的XLSX文件中包含打印机设置的*.bin*文件。打印机设置文件位于*“[file "root"]\xl\printerSettings”*。本文介绍了如何使用Aspose.Cells API移除现有的打印机设置。

## **删除Excel文件中工作表的现有打印设置**
Aspose.Cells允许您移除Excel文件中不同工作表的现有打印机设置。以下示例代码说明了如何移除工作簿中所有工作表的现有打印机设置。请参阅其示例Excel文件，输出Excel文件，控制台输出以及屏幕截图以供参考。

## **屏幕截图**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **控制台输出**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
