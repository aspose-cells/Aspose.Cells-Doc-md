---
title: دمج الملفات باستخدام C++
linktitle: دمج الملفات
type: docs
weight: 20
url: /ar/cpp/merge-files/
description: تعلم كيفية دمج ملفات إكسل بكفاءة باستخدام Aspose.Cells for C++.
---

## **مقدمة**

يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات، تنسيقات، وصيغ، يمكن استخدام طريقة [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) لدمج عدة دفاتر عمل، ويمكن استخدام طريقة [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) لنسخ أوراق العمل إلى دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك الكثير من الملفات للدمج، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)، وهو أسلوب أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells**

يوضح رمز المثال التالي كيفية دمج ملفات كبيرة باستخدام أسلوب [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/). يأخذ ملفين بسيطين لكن كبيرين، Book1.xls وBook2.xls. تحتوي الملفات على بيانات وصيغ منسقة فقط.

{{% alert color="primary" %}}

طريقة [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) تدعم فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج كائنات مثل الرسوم البيانية والصور والتعليقات أو كائنات أخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

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
