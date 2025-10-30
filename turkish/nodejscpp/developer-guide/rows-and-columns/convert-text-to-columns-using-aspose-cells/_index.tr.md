---  
title: Aspose.Cells for Node.js via C++ kullanarak Metni Sütunlara Dönüştür  
linktitle: Metni Sütunlara Dönüştürme  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel de metni sütunlara dönüştürmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel kullanarak metninizi sütunlara dönüştürebilirsiniz. Bu özellik *Veri Araçları* altında *Veri* sekmesi üzerinden kullanılabilir. Bir sütunun içeriğini çoklu sütunlara bölmek için, verilerin belirli bir ayırıcı (örneğin virgül veya başka herhangi bir karakter) içermesi gerekir ve Microsoft Excel, içeriği çoklu hücreye böler. Aspose.Cells for Node.js via C++, bu özelliği [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) aracılığıyla da sağlar.  

## **Aspose.Cells for Node.js via C++ kullanarak Metni Sütunlara Dönüştür**  

Aşağıdaki örnek kod, [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) metodunun kullanımını açıklar. Kod önce ilk çalışma sayfasındaki A sütununa bazı kişilerin isimlerini ekler. İsimler boşluk karakteriyle ayrılmıştır. Sonra [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) metodunu A sütununda uygular ve sonucu bir Excel dosyası olarak kaydeder. Eğer [çıktı Excel dosyasını](25395213.xlsx) açarsanız, ilk isimlerin A sütununda, soy isimlerin B sütununda olduğunu göreceksiniz.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
