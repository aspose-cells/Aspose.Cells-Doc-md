---
title: C++を使用してテンプレートからターゲットワークブックへVBAマクロユーザーフォームデザイナーのストレージをコピーします
linktitle: VBAマクロUserFormのデザイナーストレージをコピーする方法について学びます。
type: docs
weight: 130
url: /ja/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Aspose.Cells for C++を使用してテンプレートからターゲットワークブックにVBAマクロUserFormのデザイナーストレージをコピーする方法を学習します。
---

## **可能な使用シナリオ**

Aspose.Cellsを使用すると、一つのExcelファイルから別のExcelファイルへVBAプロジェクトをコピーできます。VBAプロジェクトは、ドキュメント、手続き、デザイナーなどのさまざまなタイプのモジュールで構成されます。すべてのモジュールは簡単なコードでコピーできますが、デザイナーモジュールについては、Designer Storageと呼ばれる追加のデータにアクセスしたりコピーしたりする必要があります。次の２つの方法はDesigner Storageを扱います：

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**

以下のサンプルコードをご覧ください。このコードは、[テンプレートExcelファイル](50528345.xlsm)から空のブックにVBAプロジェクトをコピーし、それを[出力Excelファイル](50528346.xlsm)として保存します。テンプレートExcelファイルのVBAプロジェクトを開くと、以下のようなユーザーフォームが見えます。ユーザーフォームはデザイナーストレージから構成されており、[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)と[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)の方法を使ってコピーされます。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。ボタン1をクリックすると、VBAユーザーフォームが開き、その中のコマンドボタンをクリックするとメッセージボックスが表示されます。

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook target;

    Workbook templateFile(srcDir + u"sampleDesignerForm.xlsm");

    WorksheetCollection templateSheets = templateFile.GetWorksheets();
    WorksheetCollection targetSheets = target.GetWorksheets();

    for (int i = 0; i < templateSheets.GetCount(); ++i)
    {
        Worksheet ws = templateSheets.Get(i);
        if (ws.GetType() == SheetType::Worksheet)
        {
            Worksheet s = targetSheets.Add(ws.GetName());
            s.Copy(ws);
            s.GetCells().Get(u"A2").PutValue(u"VBA Macro and User Form copied from template to target.");
        }
    }

    VbaProject templateVbaProject = templateFile.GetVbaProject();
    VbaProject targetVbaProject = target.GetVbaProject();
    VbaModuleCollection templateModules = templateVbaProject.GetModules();

    for (int i = 0; i < templateModules.GetCount(); ++i)
    {
        VbaModule vbaItem = templateModules.Get(i);
        if (vbaItem.GetName() == u"ThisWorkbook")
        {
            targetVbaProject.GetModules().Get(u"ThisWorkbook").SetCodes(vbaItem.GetCodes());
        }
        else
        {
            std::wcout << reinterpret_cast<const wchar_t*>(vbaItem.GetName().GetData()) << std::endl;

            int vbaMod = 0;
            Worksheet sheet = targetSheets.GetSheetByCodeName(vbaItem.GetName());
            if (sheet.IsNull())
            {
                vbaMod = targetVbaProject.GetModules().Add(vbaItem.GetType(), vbaItem.GetName());
            }
            else
            {
                vbaMod = targetVbaProject.GetModules().Add(sheet);
            }

            targetVbaProject.GetModules().Get(vbaMod).SetCodes(vbaItem.GetCodes());

            if (vbaItem.GetType() == VbaModuleType::Designer)
            {
                Vector<uint8_t> designerStorage = templateVbaProject.GetModules().GetDesignerStorage(vbaItem.GetName());
                targetVbaProject.GetModules().AddDesignerStorage(vbaItem.GetName(), designerStorage);
            }
        }
    }

    target.Save(outDir + u"outputDesignerForm.xlsm", SaveFormat::Xlsm);

    Aspose::Cells::Cleanup();
}
```
