---
title: ファイルの結合（C++）
linktitle: ファイルの結合
type: docs
weight: 20
url: /ja/cpp/merge-files/
description: Aspose.Cells for C++を使用してExcelファイルを効率よく結合する方法を学びます。
---

## **紹介**

Aspose.Cellsはファイルのマージにさまざまな方法を提供しています。データ、書式設定、数式を含むシンプルなファイルには [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) 方法が複数のブックを結合するのに適しており、[**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) 方法はシートを新しいブックにコピーするのに適しています。これらの方法は使いやすく効果的ですが、多数のファイルをマージする場合、システムリソースを大量に使用することがあります。これを避けるために、より効率的な [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) 静的メソッドを使用します。

## **Aspose.Cellsを使用してファイルをマージする**

以下のサンプルコードは、[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) メソッドを使用して大きなファイルをマージする例です。Book1.xlsとBook2.xlsの2つの大きなファイルを対象とし、それらには書式設定済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)メソッドはデータ、スタイル、フォーマット、数式のマージのみをサポートします。チャートや画像、コメントなどのオブジェクトはこの方法ではマージされないことがあります。また、一時データを保存するキャッシュファイルが使用されます。

{{% /alert %}}

```c++
#include <iostream>
#include <string>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
	Aspose::Cells::Startup();

	U16String srcDir(u"../Data/01_SourceDirectory/");
	U16String outDir(u"../Data/02_OutputDirectory/");

	Vector<U16String> data{
	  srcDir + u"Book1.xls",
	  srcDir + u"Book2.xls"
	};

	U16String cacheFile = outDir + u"test.txt";
	U16String dest = outDir + u"output.xlsx";

	CellsHelper::MergeFiles(data, cacheFile, dest);

	Workbook workbook(dest);

	WorksheetCollection sheets = workbook.GetWorksheets();
	int count = sheets.GetCount();
	for (int idx = 0; idx < count; ++idx)
	{
		Worksheet sheet = sheets.Get(idx);
		U16String sheetName = U16String(u"Sheet_");
		U16String numStr = U16String(std::to_string(idx+1).c_str());
		sheet.SetName(sheetName + numStr);
	}

	workbook.Save(dest);

	Aspose::Cells::Cleanup();
	return 0;
}
```
