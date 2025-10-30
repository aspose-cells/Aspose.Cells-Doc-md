---
title: Web拡張機能  OfficeアドインをC++で
linktitle: Web拡張機能  Officeアドイン
type: docs
weight: 130
url: /ja/cpp/web-extensions-office-add-ins/
description: Aspose.Cellsを使ったExcelファイル内のWeb拡張機能（Officeアドイン）の追加とアクセス方法を学びます。
---

Web拡張機能はOfficeアプリケーションを拡張し、Officeドキュメント内のコンテンツと連携します。これにより、Officeクライアントの機能性と生産性が向上します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加できます。**挿入**タブをクリックし、その後**ストア**/**アドインを取得**リンクをクリックしてください。アドインボックスで目的のアドインを参照して追加します。

Aspose.Cellsは、[**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)クラスを使用してWeb拡張を追加する機能も提供します。次のコード例は、[**WebExtension**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextension/)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)クラスを使用してExcelファイルにWeb拡張を追加する方法を示しています。詳細は[出力Excelファイル](89849869.xlsx)を参照してください。

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the WebExtension collection from the workbook's worksheets
    WebExtensionCollection extensions = workbook.GetWorksheets().GetWebExtensions();
    WebExtensionTaskPaneCollection taskPanes = workbook.GetWorksheets().GetWebExtensionTaskPanes();

    // Add a new WebExtension and WebExtensionTaskPane
    int32_t extensionIndex = extensions.Add();
    int32_t taskPaneIndex = taskPanes.Add();

    // Get the newly added WebExtension and configure it
    WebExtension extension = extensions.Get(extensionIndex);
    extension.GetReference().SetId(u"wa104379955");
    extension.GetReference().SetStoreName(u"en-US");
    extension.GetReference().SetStoreType(WebExtensionStoreType::OMEX);

    // Get the newly added WebExtensionTaskPane and configure it
    WebExtensionTaskPane taskPane = taskPanes.Get(taskPaneIndex);
    taskPane.SetIsVisible(true);
    taskPane.SetDockState(u"right");
    taskPane.SetWebExtension(extension);

    // Save the workbook with the added WebExtension
    workbook.Save(outDir + u"AddWebExtension_Out.xlsx");

    std::cout << "WebExtension added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Web拡張機能情報へのアクセス**

Aspose.Cellsは、Excelファイル内のWeb拡張情報にアクセスする機能を提供します。次のコード例は、[サンプルExcelファイル](89849870.xlsx)をロードし、Web拡張情報にアクセスする方法を示しています。結果はコンソール出力から確認できます。

### **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook workbook(srcDir + u"WebExtensionsSample.xlsx");

    // Get the collection of web extension task panes
    WebExtensionTaskPaneCollection taskPanes = workbook.GetWorksheets().GetWebExtensionTaskPanes();

    // Iterate through each task pane and print its properties
    for (int i = 0; i < taskPanes.GetCount(); ++i)
    {
        WebExtensionTaskPane taskPane = taskPanes.Get(i);

        std::cout << "Width: " << taskPane.GetWidth() << std::endl;
        std::cout << "IsVisible: " << taskPane.IsVisible() << std::endl;
        std::cout << "IsLocked: " << taskPane.IsLocked() << std::endl;
        std::cout << "DockState: " << taskPane.GetDockState().ToUtf8() << std::endl;
        std::cout << "StoreName: " << taskPane.GetWebExtension().GetReference().GetStoreName().ToUtf8() << std::endl;
        std::cout << "WebExtension.Id: " << taskPane.GetWebExtension().GetId().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();

    return 0;
}
```

### **コンソール出力**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
