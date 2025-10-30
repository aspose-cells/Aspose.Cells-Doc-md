---
title: Hücreleri Birleştir ve Serbest Bırakmak için Node.js üzerinden C++
linktitle: Hücreleri Birleştirme ve Ayırma
description: Aspose.Cells, hücrelerin birleştirilmesi ve serbest bırakılması destekleyen Node.js kütüphanesidir. Bu makalede Aspose.Cells kütüphanesi kullanılarak hücrelerin nasıl birleştirileceği ve serbest bırakılacağı, ayrıca birleşik hücre stilinin nasıl özelleştirileceği anlatılacaktır.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, hücreleri birleştir, serbest bırak, stil ayarları, özel stiller
type: docs
weight: 190
url: /tr/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, bu özelliği destekler ve çalışsheet'lerde hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçilen aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 
## **Giriş**
Her zaman her satır veya sütunda aynı hücre sayısını istemezsiniz. Örneğin, birkaç sütunu kapsayan bir hücreye başlık koymak isteyebilirsiniz. Veya, bir fatura oluştururken toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için hücreleri birleştirin. Microsoft Excel, kullanıcılara dosyaları seçme ve istedikleri şekilde elektronik tabloyu yapılandırmak için birleştirmelerine izin verir.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde, yalnızca en sol üst hücredeki veri korunur. Aralıkta diğer hücrelerde veri varsa, bu veri silinir. Biçimlendirme de, aralıktaki referans hücreye göre ayarlandığından, hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilen hücreye uygulanır. Hücre bölündüğünde, yeni hücreler orijinal biçimlendirme ayarlarını korur.

{{% /alert %}} 
## **Çalışsheet'te Hücreleri Birleştirme**
### **Microsoft Excel'de Hücreleri Birleştirme**
Aşağıdaki adımlar, MS Excel kullanarak çalışsheet'te hücreleri birleştirmeyi açıklar.

1. İstenen veriyi aralıktaki en sol üst hücreye kopyalayın.
2. Birleştirmek istediğiniz hücreleri seçin.
3. Bir satır veya sütunda hücreleri birleştirmek ve hücre içeriğini ortalamak için, **Biçimlendirme** araç çubuğundaki **Birleştir ve Ortala** simgesine tıklayın.

### **Aspose.Cells ile Hücreleri Birleştirmek**
Aspose.Cells.Cells Sınıfı, görev için kullanışlı bazı yöntemler içerir. Örneğin, `merge()` yöntemi, belirli bir aralıkta hücreleri tek bir hücreye birleştirir.

Aşağıdaki örnek, bir çalışsheet'te (C6:E7) hücrelerin nasıl birleştirileceğini göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Hücreleri Ayırma (Birleştirmeyi Bölmek)**
### **Microsoft Excel Kullanımı**
Aşağıdaki adımlar, Microsoft Excel kullanarak birleştirilmiş hücreleri nasıl ayıracağınızı açıklar.

1. Birleştirilmiş hücreyi seçin.
   Hücreler birleştirildiğinde, **Birleştir ve Ortala**, **Biçimlendirme** araç çubuğunda seçilidir.
1. **Biçimlendirme** araç çubuğunda **Birleştir ve Ortala**'ya tıklayın.

### **Aspose.Cells Kullanımı**
Aspose.Cells.Cells sınıfında, hücreleri orijinal durumlarına ayıran `unmerge()` adlı bir yöntem vardır. Bu yöntem, hücreleri birleştirilen hücre aralığında hücrelerin referansını kullanarak ayırır.

Aşağıdaki örnek, birleştirilmiş hücreleri (C6) nasıl ayıracağınızı göstermektedir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri ayırır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Gelişmiş Konular**
- [Çalışsheet'teki Birleştirilmiş Hücreleri Bulma](/cells/tr/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
