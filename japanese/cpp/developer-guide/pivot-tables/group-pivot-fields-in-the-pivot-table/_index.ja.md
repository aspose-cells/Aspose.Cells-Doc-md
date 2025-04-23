---
title: C++を使用してピボットフィールドをグループ化する
linktitle: ピボットテーブル内のPivot Fieldをグループ化
type: docs
weight: 80
url: /ja/cpp/group-pivot-fields-in-the-pivot-table/
description: Aspose.Cells for C++を使用してピボットテーブルのピボットフィールドをグループ化する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelには、ピボットテーブルのピボットフィールドをグループ化する機能があります。ピボットフィールドに関連するデータが多い場合、それをセクションにグループ化することはしばしば役立ちます。Aspose.Cellsも[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)メソッドを使用して、この機能を提供します。

## **ピボットテーブル内のPivot Fieldをグループ化**

以下のサンプルコードは、[サンプルExcelファイル](64716818.xlsx)をロードし、[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)メソッドを使用して最初のピボットフィールドにグループ化を行います。それからピボットテーブルのデータをリフレッシュして計算し、ブックを[出力Excelファイル](64716817.xlsx)として保存します。スクリーンショットは、サンプルコードのサンプルExcelファイルに対する効果を示しています。スクリーンショットに示されているように、最初のピボットフィールドは現在月ごとと四半期ごとにグループ化されています。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
	Aspose::Cells::Startup();

	U16String srcDir(u"../Data/01_SourceDirectory/");
	U16String outDir(u"../Data/02_OutputDirectory/");

	Workbook wb(srcDir + u"sampleGroupPivotFieldsInPivotTable.xlsx");

	Worksheet ws = wb.GetWorksheets().Get(1);

	PivotTable pt = ws.GetPivotTables().Get(0);

	Date dtStart{ 2023, 12, 31, 0, 0, 0, 0 };
	Date dtEnd{ 2025, 9, 5 , 0, 0, 0, 0 };

	Vector<PivotGroupByType> groupTypeList{
		 PivotGroupByType::Months,
		 PivotGroupByType::Quarters
	};

	PivotField field = pt.GetRowFields().Get(0);
	field.GroupBy(dtStart, dtEnd, groupTypeList, 1, true);

	pt.RefreshData();
	pt.CalculateData();

	wb.Save(outDir + u"outputGroupPivotFieldsInPivotTable2.xlsx");

	std::cout << "Pivot field grouped successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```
