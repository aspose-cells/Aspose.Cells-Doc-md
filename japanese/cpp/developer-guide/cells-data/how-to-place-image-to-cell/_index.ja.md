---
title: C++でセルに画像を挿入する方法
linktitle: セルに画像を挿入する方法
type: docs
weight: 130
url: /ja/cpp/how-to-insert-picture-in-cell/
description: C++を使ってAspose.Cellsでセルに画像を挿入する方法を学びます。
keywords: セルに画像を挿入する方法、セルに画像を挿入する、セルに画像を配置する方法、セルの上に画像を配置する、セルに画像を配置する方法、セルの上に画像を配置する方法、セル内の画像とセルの上の画像を切り替える方法、セルに配置してセルの上に配置する方法の切り替え。
---

## **可能な使用シナリオ**
画像はワークシートに明るさを加え、内容の視覚的表現を提供します。これにより、データの理解やインサイトの抽出が容易になります。長年Excelで画像を使用できましたが、最近になって画像を実際のセル値にする機能が有効になりました。図のレイアウトを変更しても、データに添付されたままです。テーブルに使ったり、並べ替えやフィルター、数式に含めたりできます！

## **Excelを使用してセルに画像を挿入する方法**
Excelのセルに画像を挿入する方法について、以下の手順に従います:

1. [挿入] タブをクリックし、[画像] オプションを選択します。
2. **セルに挿入** を選択します。[画像の挿入元]ドロップダウンメニューから次のソースのいずれかを選択します(**このデバイス**、**標準画像**、**オンライン画像** )。このデバイスは、デバイスから画像を挿入するためのものです。標準画像は、標準画像から画像を挿入するためのものです。オンライン画像は、ウェブから画像を挿入するためのものです。
<br>
<img src="1.png" width=60% />
3. 画像を選択してセルに挿入します。
<br>
<img src="8.png" width=60% />

## **Excelを使用してセルの上に画像を挿入する方法**
Excelでセルの上に画像を挿入する方法については、次の手順に従います:

1. [挿入] タブをクリックし、[画像] オプションを選択します。
2. **セルの上に置く** を選択します。[画像の挿入] ドロップダウンメニューから以下のソースの一つを選択します（**このデバイス**、**ストック画像**、および **オンライン画像**）。デバイスの画像を挿入するには、「このデバイス」を選択します。ストック画像の画像を挿入するには、「ストック画像」を選択します。ウェブから画像を挿入するには、「オンライン画像」を選択します。
<br>
<img src="2.png" width=60% />
3. 画像を選択し、セルの上に画像を挿入します。
<br>
<img src="3.png" width=60% />

## **Excel を使用してセル内の画像からセルの上に画像に切り替える方法**
**セル内の画像** から **セルの上に画像** に簡単に切り替えることができます。次の手順に従ってください。
1. セルを右クリックし、**画像内にセル** > **セルの上に置く** を選択します。 
<br>
<img src="4.png" width=60% />
2. 切り替え後の結果は次のようになります。
<br>
<img src="5.png" width=60% />

## **Excel を使用してセルの上に画像からセル内の画像に切り替える方法**
**セルの上に画像** から **セル内の画像** に簡単に切り替えることができます。次の手順に従ってください。
1. 画像を右クリックし、**セル内に配置** を選択します。 
<br>
<img src="6.png" width=60% />
2. 切り替え後の結果は次のようになります。
<br>
<img src="7.png" width=60% />

## **C++を使ってセルに画像を挿入する方法**
Aspose.Cellsを使用してセルに画像を挿入します。次のサンプルコードをご覧ください。例のコードを実行した後、画像がセルに挿入されます。
1. Workbookオブジェクトをインスタンス化します。 
2. 画像を挿入したいセルを取得します。
3. Cell.EmbeddedImage プロパティを設定します。 
4. 最後に、[output XLSX](out.xlsx)形式でブックを保存します。 

## **サンプルコード**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
