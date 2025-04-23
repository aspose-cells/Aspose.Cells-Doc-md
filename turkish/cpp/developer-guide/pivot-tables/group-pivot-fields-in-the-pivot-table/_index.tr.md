---
title: C++ kullanarak Pivot Tablo da Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Alanları Gruplandırın
type: docs
weight: 80
url: /tr/cpp/group-pivot-fields-in-the-pivot-table/
description: Aspose.Cells for C++ kullanarak pivot tablosunda pivot alanlarını nasıl gruplayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, pivot tablosunun pivot alanlarını gruplamanıza olanak tanır. Bir pivot alanına ilişkin büyük miktarda veri olduğunda, bunları bölümlere ayırmak genellikle faydalıdır. Aspose.Cells, [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/) yöntemini kullanarak bu özelliği sağlar.

## **Pivot Tablosunda Alanları Gruplandırın**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716818.xlsx) yükler ve ilk pivot alanında [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/) yöntemini kullanarak gruplama yapar. Ardından pivot tablosunun verilerini yeniler ve hesaplar ve çalışma kitabını [çıktı Excel dosyası olarak](64716817.xlsx) kaydeder. Ekran görüntüsü, örnek kodun örneğin Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde gördüğünüz gibi, ilk pivot alanı artık aylara ve çeyreklere göre gruplandırılmış durumda.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Örnek Kod**

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
