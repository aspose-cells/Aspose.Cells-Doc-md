---
title: 使用 C++ 合并文件
linktitle: 合并文件
type: docs
weight: 20
url: /zh/cpp/merge-files/
description: 学习如何使用 Aspose.Cells for C++ 高效合并Excel文件。
---

## **介绍**

Aspose.Cells 提供多种合并文件的方法。对于包含数据、格式和公式的简单文件，可以使用 [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) 方法合并多个工作簿，使用 [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) 方法将工作表复制到新工作簿。这些方法使用简单且有效，但如果需要合并大量文件，可能会占用大量系统资源。为了避免此问题，可以使用更高效的 [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) 静态方法来合并多个文件。

## **使用Aspose.Cells合并文件**

以下示例代码演示如何使用 [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) 方法合并大文件。它处理两个简单但较大的文件 Book1.xls 和 Book2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) 方法仅支持合并数据、样式、格式和公式。图表、图片、评论或其他对象可能无法通过此方法合并。此外，使用缓存文件存储临时数据以支持该过程。

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
{{< app/cells/assistant language="cpp" >}}
