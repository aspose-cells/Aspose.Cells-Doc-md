---
title: C++を用いたピボットテーブルとソースデータ
linktitle: ピボットテーブルとソースデータ
type: docs
weight: 30
url: /ja/cpp/pivot-table-and-source-data/
description: Aspose.Cellsを使ってピボットテーブルのソースデータを動的に変更する方法を学びます。
---

## **Pivot Tableのソースデータ**

デザイン時にはわからない異なるデータソース（たとえばデータベースなど）からデータを取るピボットテーブルを作成したいときがあります。この記事では、ピボットテーブルのデータソースを動的に変更するアプローチについて説明します。

### **ピボットテーブルのデータソースを変更する**

1. 新しいデザイナーテンプレートを作成します。
   1. 以下のスクリーンショットに示すように、新しいデザイナーテンプレートファイルを作成します。
   1. その後、**DataSource**という名前の範囲を定義します。この範囲はこれらのセルの範囲を参照します。

      **デザイナーテンプレートの作成と名前付き範囲の定義、DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. この名前付き範囲に基づいてPivot Tableを作成します。
   1. Microsoft Excelで**データ**、**ピボットテーブル**、**ピボットテーブルおよびピボットチャートレポート**を選択します。
   1. 最初のステップで作成した名前付き範囲に基づいてピボットテーブルを作成します。

      **DataSourceに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. 対応するフィールドをピボットテーブルの行と列にドラッグし、スクリーンショットに示されているような結果のピボットテーブルを作成します。

   **対応するフィールドに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


設計したピボットテーブルが以下に示されています。
   1. **データオプション**の設定で**開くときに更新**をチェックします。

      **ピボットテーブルオプションの設定** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


これで、このファイルをデザイナーテンプレートファイルとして保存できます。

1. 新しいデータを埋め込んでピボットテーブルのソースデータを変更します。
   1. デザイナーテンプレートが作成されたら、次のコードを使用してピボットテーブルのソースデータを変更します。

以下のコード例を実行すると、ピボットテーブルのソースデータが変更されます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
