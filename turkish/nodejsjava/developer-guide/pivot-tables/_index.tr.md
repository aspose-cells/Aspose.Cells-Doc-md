---
title: Pivot Tablo Ekle
description: Aspose.Cells for Node.js via Java kullanarak Excel elektronik tablo dosyalarında pivot tablolar oluşturun ve biçimlendirin.
linktitle: Pivot Tablolar
url: /tr/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Pivot Tablo Oluştur, Pivot Tablo Ekle, Pivot Tablo Biçimlendir, Aspose.Cells for Node.js via Java.
ai_search_scope: cells_nodejsjava
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

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
Bir hücre aralığını veri kaynağı olarak atarken, aralık sol üstten sağ alta doğru gitmelidir. Örneğin, "A1:C3" geçerlidir, ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/tr/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/tr/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}