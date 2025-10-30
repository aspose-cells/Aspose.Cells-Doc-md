---  
title: Node.js ve C++ kullanarak Tablolar ve Aralıklar  
linktitle: Tablolar ve Aralıklar  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/tables-and-ranges/  
---  

## **Giriş**  

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve onunla gelen tablo işlevleriyle çalışmak istemezsiniz. Bunun yerine, bir tablo gibi görünen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veri tutmak için tabloyu normal bir veri aralığına dönüştürün.  
Aspose.Cells, Microsoft Excel'in tablo ve liste nesneleri için bu özelliği destekler.  

## **Microsoft Excel Kullanımı**  

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:  

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.  
1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.  

## **Aspose.Cells Kullanımı**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.  

{{% /alert %}}  

## **Tablo, Aralığı Seçenekleri ile Aralığı Dönüştürme**  

Aspose.Cells, [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) sınıfı aracılığıyla Tablo'yu Aralığa dönüştürürken ek seçenekler sağlar. [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) sınıfı, belirtilen satır dizinine kadar tablo biçimlendirmesini korumanızı ve geri kalan biçimlendirmeyi kaldırmanızı sağlayan [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) özelliğini sağlar.  

Aşağıda verilen örnek kod, [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) sınıfının kullanımını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
