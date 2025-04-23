---
title: Node.js üzerinden C++ kullanarak Çoklu Çalışma Kitaplarını Tek Bir Çalışma Kitabına Birleştirme
linktitle: Çalışma Kitabı Birleştirme
type: docs
weight: 66
url: /tr/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aspose.Cells for Node.js via C++ kullanarak birden çok çalışma kitabını tek bir çalışma kitabına nasıl birleştireceğinizi öğrenin. 
---

{{% alert color="primary" %}}

Bazen, resimler, grafikler ve veriler gibi çeşitli içeriklerle çalışma kitaplarını tek bir çalışma kitabında birleştirmeniz gerekebilir. Aspose.Cells for Node.js via C++ bu özelliği destekler. Bu makale, nasıl bir konsol uygulaması oluşturulup, birkaç basit kod satırıyla Aspose.Cells kullanılarak çalışma kitaplarının birleştirileceğini gösterir.

{{% /alert %}}

## **Resimler ve Grafiklerle Çalışma Kitaplarını Birleştirme**

Örnek kod, Aspose.Cells for Node.js via C++ kullanarak iki çalışma kitabını tek bir çalışma kitabına birleştirir. Kod kaynak çalışma kitaplarını yükler, [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) metodunu kullanarak bunları birleştirir ve çıktı çalışma kitabını kaydeder.

### **Kaynak Çalışma Kitapları**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Çıktı Çalışma Kitapları**

- [combined.xlsx](5473095.xlsx)

### **Ekran Görüntüleri**

Aşağıda, kaynak ve çıktı çalışma kitaplarının ekran görüntüleri bulunmaktadır.

{{% alert color="primary" %}}

Herhangi bir kaynak çalışma kitabını kullanabilirsiniz. Bu resimler sadece görsel amaçlar içindir.

{{% /alert %}}

**Grafik çalışma kitabının ilk çalışsayfası - yığılmış** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Grafik çalışma kitabının ikinci çalışsayfası - çizgi** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Resim çalışma kitabının ilk çalışma sayfası - resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Birleşik çalışma kitabındaki tüm üç çalışma sayfası - yığılmış, çizgi, resim** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Gelişmiş Konular**
- [Birden Fazla Çalışma Sayfasını Tek Bir Çalışma Sayfasına Birleştirme](/cells/tr/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Dosyaları Birleştirme](/cells/tr/nodejs-cpp/merge-files/)

