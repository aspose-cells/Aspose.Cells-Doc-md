---
title: Dosyaları C++ ile Birleştir
linktitle: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/cpp/merge-files/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını etkin bir şekilde nasıl birleştireceğinizi öğrenin.
---

## **Giriş**

Aspose.Cells, dosya birleştirme için farklı yollar sunar. Veri, biçimlendirme ve formüller içeren basit dosyalar için [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) yöntemi birkaç çalışma kitabını birleştirmek; ve [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak çok sayıda dosya birleştiriyorsanız, sistem kaynaklarınızın yoğun kullanıldığını fark edebilirsiniz. Bunu önlemek için, birkaç dosyayı birleştirmenin daha verimli yolu olan [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) statik yöntemini kullanın.

## **Aspose.Cells Kullanarak Dosyaları Birleştirme**

Aşağıdaki örnek kod, büyük dosyaları [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) yöntemi ile birleştirme yöntemini gösterir. İki basit ve büyük dosya olan Book1.xls ve Book2.xls kullanır. Dosyalar sadece biçimlendirilmiş veri ve formüller içerir.

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) yöntemi yalnızca veri, stiller, biçimlendirme ve formüllerin birleştirilmesini destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi nesneler bu yöntem kullanılarak birleştirilmeyebilir. Ayrıca, geçici verileri depolamak için önbelleğe alınmış bir dosya kullanılır.

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
