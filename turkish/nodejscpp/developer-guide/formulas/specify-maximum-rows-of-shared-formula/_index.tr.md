---  
title: Paylaşılan Formül için Maksimum Satır Sayısını Node.js ile C++ kullanarak belirtin  
linktitle: Paylaşılan Formülün Maksimum Satırlarını Belirtme  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Aspose.Cells for Node.js via C++ kullanarak paylaşılan formüllerin maksimum satır sayısını nasıl belirleyeceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Varsayılan olarak, paylaşılan formülün maksimum satır sayısı 64'tür. Bu herhangi bir sayı olabilir örneğin 1000 olabilir. Paylaşılan formülün performansı, satır sayısı ile değişir. Bu nedenle, Aspose.Cells, paylaşılan formülün maksimum satır sayısını belirlemek için kullanılabilecek [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) özelliği sağlar. Paylaşılan formül toplam satır sayısı bu değerden büyükse, birkaç paylaşılan formüle bölünecektir, aşağıdaki ekran görüntüsünde gösterildiği gibi.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**  

Aşağıdaki örnek kod, [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) özelliğinin kullanımı açıklamaktadır. Paylaşılan formülün maksimum satır sayısını 5 olarak ayarlar ve D1 hücresinde 100 satır için paylaşılan formülü ekler ve sonucu [çıktı Excel dosyasına](61767856.xlsx) kaydeder. Eğer çıktı Excel dosyasının içeriğini çıkarırsanız ve *sheet1.xml* dosyasını kontrol ederseniz, paylaşılan formülün her 5 satırda bir bölündüğünü görebilirsiniz, yukarıdaki ekran görüntüsünde vurgulanmıştır.  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

