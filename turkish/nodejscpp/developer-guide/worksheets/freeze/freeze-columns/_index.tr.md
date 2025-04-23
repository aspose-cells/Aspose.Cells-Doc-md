---  
title: Node.js ile C++ kullanarak Excel Çalışma Sayfasının İlk Sütun(ları)nı Dondurun  
linktitle: Sütunları Sabitle  
type: docs  
weight: 190  
url: /tr/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Sayfalarının sol sütunlarını programatik olarak nasıl donduracağınızı öğrenin.  
keywords: Sol sütunları dondurun, ilk sütunları dondurun, sütunu(sütunları) kilitleyin  
---  

## **Giriş**  

Bu makalede, sol sütunu(ları) nasıl donduracağımızı öğreneceğiz. Bir satırda büyük miktarda veri olduğunda, yatay kaydırma yaparken sol sütunları göremeyebilirsiniz. Dondurup kilitleyerek kalan veriyi kaydırırken bile dondurulmuş bölümü görebilirsiniz. Sol sütunlarda başlıkları kolayca görebilirsiniz.  

## **Excel'de Sütunları Sabitle**  

**![Excel'de sol sütunları sabitle](freeze-columns.png)**  

1. Sol sütunu(sütunları) dondurmak istiyorsanız, önce dondurulması gereken sütunun altındaki sütunu seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden İlk Sütunu Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk sütun her zaman sol görünümde kalır.

**![Dondurulmuş sütun](frozen-columns.png)**  

Görüleceği üzere, 1. sütun dondurulmuş ve yatay kaydırırken ilk sütun her zaman görünüp sabit kalır.

Sütunları Dondurmak, uzun verinizi ilk sütunu takip etme zahmeti olmadan görüntülemenizi sağlar.

## **Aspose.Cells for Node.js via C++ ile Sütunları Dondurun**  
Aspose.Cells for Node.js via C++ kullanarak ilk sütun(ları) dondurmak çok basittir.  
Seçilen sütunu dondurmak için lütfen [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) metodunu kullanın.  
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.freezePanes() metodunu kullanarak ilk sütunu dondurun.
3. Dosyayı kaydedin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).  

