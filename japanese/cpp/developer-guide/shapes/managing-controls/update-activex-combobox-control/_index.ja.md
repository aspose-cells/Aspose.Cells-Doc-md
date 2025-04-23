---
title: C++でActiveXコンボボックスコントロールを更新する
linktitle: ActiveX ComboBoxコントロールを更新
type: docs
weight: 170
url: /ja/cpp/update-activex-combobox-control/
description: Aspose.Cellsを使用してActiveXコンボボックスコントロールの値を読み書きする方法を学ぶ。
---

## **可能な使用シナリオ**
Aspose.Cellsを使用してActiveXコンボボックスコントロールの値を読み書きできます。ActiveXコントロールには [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) プロパティを介してアクセスし、そのタイプを [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/) プロパティで確認してください。これは [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) の値を返すはずです。その後、[ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) オブジェクトにキャストして、そのさまざまなプロパティを読み書きします。

以下のサンプルコードで使用される[サンプルExcelファイル](5115124.xlsx)をダウンロードしてください。

## **ActiveX ComboBoxコントロールを更新**
以下のスクリーンショットは、[サンプルExcelファイル](5115124.xlsx)に対するサンプルコードの効果を示しています。見るとおり、ActiveX ComboBoxの値が"これはコンボボックスコントロールです"に更新されています。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **サンプルコード**
次のサンプルコードでは、[サンプルExcelファイル](5115124.xlsx)内のActiveX ComboBoxコントロールの値を更新します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"SourceFile.xlsx");

    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    ActiveXControl c = shape.GetActiveXControl();

    if (c.GetType() == ControlType::ComboBox)
    {
        ComboBoxActiveXControl comboBoxActiveX = static_cast<ComboBoxActiveXControl>(c);
        comboBoxActiveX.SetValue(u"This is combo box control with updated value.");
    }

    wb.Save(outDir + u"OutputFile_out.xlsx");

    std::cout << "Workbook saved successfully with updated ComboBox value!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
