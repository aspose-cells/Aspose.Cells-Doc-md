---  
title: Aspose.Cellsを使用してC++で共有ワークブックを作成する  
linktitle: Aspose.Cellsで共有ブックを作成する  
type: docs  
weight: 40  
url: /ja/cpp/create-shared-workbook-with-aspose-cells/  
description: Aspose.Cellsを使ってC++で共有ワークブックを作成する方法を学びましょう。  
---  

## **可能な使用シナリオ**  

Microsoft Excelは、以下のスクリーンショットのようにワークブックを共有できます。ワークブックを共有すると、複数のユーザーがネットワーク上のワークブックを編集できるようになります。Aspose.Cellsは、[**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)プロパティを使って共有ワークブックを作成する機能を提供します。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cellsで共有ブックを作成する**  

以下のサンプルコードは、[**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/)プロパティを**true**に設定して共有ワークブックを作成します。Microsoft Excelで[出力Excelファイル](55541786.xlsx)を開くと、「共有」ステータスとともに出力済みのワークブック名が表示されます。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **サンプルコード**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
