---  
title: C++を使用してチャートのデータラベルシェイプを調整し、テキストにフィットさせる  
description: Aspose.Cells for C++のチャートにおいて、データラベルのシェイプのサイズを調整し、テキストにフィットさせる方法を学びます。ラベルコンテナのサイズと形状を調整し、トリミングや重なりを避けて正しく表示されるようにします。  
keywords: Aspose.Cells for C++、チャート作成、データラベル、シェイプ調整、テキストフィッティング、切り詰め、重なり。  
type: docs  
weight: 220  
url: /ja/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Excelアプリケーションでは、チャートのデータラベルの**テキストに合わせて形状を変更**するオプションが提供されており、これによりテキストが形状内に収まるように形状のサイズが拡大されます。  

{{% /alert %}}  

## **Microsoft Excelのインタフェース上で、チャートのデータラベルを選択して、**フォーマットデータラベル**メニューを右クリックします。**サイズとプロパティ**タブで、**配置**を展開して、**テキストに合わせて形状を変更**オプションを含む関連プロパティを表示します。**  

 このオプションは、チャート上の任意のデータラベルを選択し、右クリックして**データラベルの書式設定**メニューからアクセスできます。**サイズとプロパティ**タブの下にある**整列**を展開すると、必要な関連プロパティが表示されます、その中に**テキストに合わせて形状をリサイズ**オプションがあります。  

## **Aspose.Cells for C++を使用してチャートのデータラベルシェイプをリサイズする方法**  

 Excelの機能に似せて、データラベルの形状をテキストにフィットさせるために、Aspose.Cells APIはブール型の[**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext)プロパティを公開しています。以下のコード例は、その[**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext)プロパティの簡単な使用例を示しています。  

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Create an instance of Workbook containing the Chart
    Workbook book(inputFilePath);

    // Access the Worksheet that contains the Chart
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Iterate through each Chart in the Worksheet
    for (int32_t i = 0; i < sheet.GetCharts().GetCount(); i++)
    {
        Chart chart = sheet.GetCharts().Get(i);

        // Iterate through each NSeries in the Chart
        for (int32_t index = 0; index < chart.GetNSeries().GetCount(); index++)
        {
            // Access the DataLabels of indexed NSeries
            DataLabels labels = chart.GetNSeries().Get(index).GetDataLabels();

            // Set ResizeShapeToFitText property to true
            labels.SetIsResizeShapeToFitText(true);
        }

        // Calculate Chart
        chart.Calculate();
    }

    // Save the result
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    book.Save(outputFilePath);

    std::cout << "Chart calculations and modifications completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

{{< app/cells/assistant language="cpp" >}}
