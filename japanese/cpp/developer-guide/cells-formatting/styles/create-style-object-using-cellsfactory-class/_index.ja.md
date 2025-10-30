---  
title: CellsFactoryクラスを使用したスタイルオブジェクトの作成（C++）  
description: Aspose.Cellsは、セルのスタイルをカスタマイズできるスタイルオブジェクトを提供するC++ライブラリです。この記事では、Aspose.CellsライブラリのCellsFactoryクラスを使用してセルスタイルオブジェクトを作成し、必要に応じてセルの外観をカスタマイズする方法を紹介します。  
keywords: Aspose.Cells、C++ライブラリ、電子スプレッドシート、スタイルオブジェクト、セルスタイル、カスタマイズ  
type: docs  
weight: 70  
url: /ja/cpp/create-style-object-using-cellsfactory-class/  
---  

## **CellsFactoryクラスを使用してスタイルオブジェクトを作成する**  
以下のサンプルコードは、【Style】オブジェクトを作成し、【CellsFactory】クラスを使用し、その後、ワークブックの既定スタイルを設定します。結果を確認するには、【出力Excelファイル】(5115153.xlsx)をダウンロードしてください。  

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
