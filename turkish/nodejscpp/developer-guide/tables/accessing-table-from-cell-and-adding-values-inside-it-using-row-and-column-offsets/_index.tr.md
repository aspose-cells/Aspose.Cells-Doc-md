---  
title: Node.js ve C++ kullanarak Hücreden Tabloya Erişme ve Satır ve Sütun Ofsetleri ile Değerler Ekleme  
linktitle: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek  
type: docs  
weight: 230  
url: /tr/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalde, Tablo veya List Objesi içine değerleri [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.  

Bir hücreden Tablo veya Liste Nesnesine erişmek için [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--) metodunu kullanın. İçine değerler eklemek için satır ve sütun ofsetlerini kullanarak [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-) metodunu kullanın.  

{{% /alert %}}  

Aşağıdaki ekran görüntüsü, kod içinde kullanılan kaynak Excel dosyasını gösterir. Boş bir tablo içerir ve tablonun içinde yer alan D5 hücresini vurgular. Bu tabloya [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--) metodu ile erişeceğiz ve ardından [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) ve [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-) metodlarıyla içindeki değerleri ekleyeceğiz.  

## Örnek  

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Node.js kodu ile hücreden tabloya erişip satır ve sütun ofsetleri kullanarak değer ekleme  

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

