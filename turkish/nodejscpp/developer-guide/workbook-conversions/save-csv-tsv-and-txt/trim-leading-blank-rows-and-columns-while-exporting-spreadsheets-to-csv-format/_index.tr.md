---
title: Çizgi ve Sütun Baştaki Boş Satır ve Sütunları Keserek CSV Formatına Exporot Etmek Node.js ve C++ ile
linktitle: CSV formatına yayılım tablolarını dışa aktarırken Önde Gelen Boş Satırları ve Sütunları Kırpmak
type: docs
weight: 100
url: /tr/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Node.js via C++ kullanarak, çalışma sayfalarını CSV ye aktarırken başlangıçtaki boş satır ve sütunların nasıl kesileceğini öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, Excel veya CSV dosyanızın önde gelen boş sütunları veya satırları bulunur. Örneğin, şu satırı düşünün

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Burada ilk üç hücre veya sütun boştur. Bu tür bir CSV dosyasını Microsoft Excel'de açarsanız, Microsoft Excel bu önde gelen boş satırları ve sütunları atar.

Varsayılan olarak, Aspose.Cells for Node.js via C++ kaydederken başlangıçtaki boş satır ve sütunları kaldırmaz, fakat Microsoft Excel gibi kaldırmak isterseniz, Aspose.Cells [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) özelliği sağlar. Bunu **true** yapın ve ardından tüm başlangıç boş satır ve sütunlar kaldırılacaktır.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ sürümünden önce, varsayılan değeri [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **false**'dür. 20.4 sürümünden itibaren, varsayılan değer [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **true**'dır.

{{% /alert %}}

## **CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp**

Aşağıdaki örnek kod, iki başlangıç boş sütunu olan [kaynak excel dosyasını](sampleTrimBlankColumns.xlsx) yükler. İlk olarak, excel dosyasını değişiklik yapmadan CSV formatında kaydeder, ardından [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) özelliğini **true** yapıp tekrar kaydeder. Ekran görüntüsü, [kaynak excel dosyasını](sampleTrimBlankColumns.xlsx), [düzenlenmemiş çıktı CSV dosyasını](outputWithoutTrimBlankColumns.csv) ve [düzenlenmiş çıktı CSV dosyasını](outputTrimBlankColumns.csv) gösterir.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
