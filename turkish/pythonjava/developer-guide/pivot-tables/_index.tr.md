---
title: Pivot Tabloları
description: Excel elek tablo dosyalarının pivot tablolarını oluşturun ve biçimlendirin.
linktitle: Pivot Tabloları
url: /tr/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Pivot Tablosu Oluştur, Pivot Tablosu Ekle, Pivot Tablosu Biçimlendir.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Pivot Tablo Oluşturma**
Aspose.Cells kullanarak elektronik tablolara programlı olarak pivot tablolar eklemek mümkündür.

### **Pivot Tablo Nesne Modeli**
Aspose.Cells, pivot tabloları oluşturmak ve kontrol etmek için kullanılan bir dizi sınıf sağlar. Yapı taşları şunlardır:
- `PivotField`, bir `PivotTable` içindeki bir alanı temsil eder.
- `PivotFieldCollection`, `PivotTable` içindeki tüm `PivotField` nesnelerinin bir koleksiyonunu temsil eder.
- `PivotTable`, çalışma sayfasındaki bir pivot tabloyu temsil eder.
- `PivotTableCollection`, çalışma sayfasındaki tüm `PivotTable` nesnelerinin bir koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Pivot Tablo Oluşturma**
1. Hücrenin `putValue` yöntemini kullanarak çalışma sayfasına veri ekleyin. Bu veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
2. Çalışma sayfası nesnesinde kapsüllenmiş `PivotTables` koleksiyonunun `add` yöntemini çağırarak çalışma sayfasına bir pivot tablo ekleyin.
3. Pivot tablonun dizinini geçirerek `PivotTables` koleksiyonundan yeni `PivotTable` nesnesine erişin.
4. Pivot tabloyu yönetmek için yukarıda açıklanan `PivotTable` nesnelerinden herhangi birini kullanın.

Örnek kod çalıştırıldıktan sonra çalışma sayfasına bir pivot tablo eklenir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Bir hücre aralığını veri kaynağı olarak atarken, aralık sol üstten sağ alta doğru gitmelidir. Örneğin, "A1:C3" geçerlidir, ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## İlgili Makaleler
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/tr/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/tr/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}