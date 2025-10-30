---  
title: Excel Dosyasına Kaydedilecek Önemli Rakamları Node.js ile C++ kullanarak Belirtmek  
linktitle: Excel Dosyasında Saklanacak Anlamlı Basamakları Belirtme  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel dosyasına kaydedilecek önemli rakamların nasıl belirtileceğini öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Varsayılan olarak, Aspose.Cells for Node.js via C++ Excel dosyasında çift değerlerin 17 önemli rakamını saklar, MS-Excel ise yalnızca 15 önemli rakamı saklar. Aspose.Cells'in varsayılan davranışını 17 önemli rakamdan 15 önemli rakama değiştirmek için [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) özelliğini kullanabilirsiniz.  

## **Excel dosyasında saklanacak anlamlı basamakları belirtme**  

Aşağıdaki örnek kod, Aspose.Cells'in düzeltilmiş değerleri saklarken 15 önemli rakam kullanmasını sağlar. Lütfen [çıktı excel dosyasını](22774105.xlsx) kontrol edin. Uzantısını .zip yapıp açın, ve içinde sadece 15 önemli rakam saklandığını göreceksiniz. Aşağıdaki ekran görüntüsü, [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) özelliğinin çıktı Excel dosyasına etkisini açıklar.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
