---
title: Excel i Fitted Pages Geniş ve Yüksek olarak yazdırmak nasıl yapılır (Node.js ve C++)
linktitle: Excel i Geniş ve Yüksek olarak Yazdırma
type: docs
weight: 200
url: /tr/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak FitToPagesWide ve FitToPagesTall ayarlarını nasıl yapacağınızı anlatan kodu gösterir.
keywords: Node.js C++ üzerinden FitToPagesWide ve FitToPagesTall nasıl ayarlanır, Node.js’de FitToPagesWide ve FitToPagesTall nasıl eklenir, Excel’de FitToPagesWide ve FitToPagesTall nasıl ayarlanır, Excel’de FitToPagesWide ve FitToPagesTall nasıl temizlenir, Excel i Geniş ve Yüksek Sığdırılmış Sayfa Olarak Yazdırma, Çalışma Sayfasını Tek Sayfa Olarak Yazdırma, Çalışma Sayfasındaki Tüm Sütunları Tek Sayfa Olarak Yazdırma.
---

## **Giriş**

FitToPagesWide ve FitToPagesTall ayarları, e-print uygulamalarında (Microsoft Excel gibi) baskı sırasında bir e-tablonun nasıl ölçekleneceğini kontrol etmek için kullanılır. Bu ayarlar, baskı alınan çıktının yatay ve dikey olarak belirli bir sayfa sayısı içinde kalmasını sağlar. İşte her ayarın detayları:

1. FitToPagesWide: Bu ayar, baskı sonucunun kaç sayfa genişliğinde olacağını belirtir. Örneğin, FitToPagesWide 1 olarak ayarlandığında, içeriğin tek bir sayfa genişliğine sığacak şekilde ölçeklendiği anlamına gelir, sayfanın genişliği ne olursa olsun.
2. FitToPagesTall: Bu ayar, yazdırılan çıktının kaç sayfa yüksekliğinde olacağını belirler. Örneğin, FitToPagesTall'i 1 olarak ayarlamak, içeriğin tek bir sayfa yüksekliğine sığacak şekilde ölçekleneceği anlamına gelir, satır sayısı ne olursa olsun.

## **Neden FitToPagesWide ve FitToPagesTall Kullanılır**
İşte FitToPagesWide ve FitToPagesTall ayarlarını kullanmanın bazı nedenleri:
1. Yazdırılan Düzen Üzerinde Kontrol: Genişlik ve yükseklik olarak sayfa sayısını belirleyerek, yazdırılan belgenin okunabilir ve iyi organize edilmiş olmasını sağlayabilirsiniz, hiçbir sütun veya satır sayfalar arasında garip şekilde bölünmez.
2. Tutarlılık: Birden fazla sayfa veya rapor yazdırıyorsanız, bu ayarları kullanmak, tutarlı bir biçim korumanıza yardımcı olur, böylece yazdırılmış belgeleri karşılaştırmak ve analiz etmek daha kolay olur.
3. Profesyonel Sunum: İçeriği uygun şekilde ölçeklendirmek ve belirli sayfa sayısına sığdırmak, verilerinizin daha profesyonel ve düzenli görünmesini sağlar.

## **Excel'de Dosyayı Geniş ve Yüksek olarak Yazdırmak için nasıl yapılır**

Microsoft Excel'de FitToPagesWide ve FitToPagesTall ayarlarını yapmak için aşağıdaki adımları izleyin:

1. Excel çalışma kitabınızı açın ve yazdırmak istediğiniz sayfaya gidin.
2. Şerit üzerindeki Sayfa Düzeni sekmesine gidin.
3. Sayfa Kurulumu grubunda, sağ alt köşedeki küçük oka tıklayarak Sayfa Yapılandırma iletişim kutusunu açın.
4. Sayfa Yapılandırma iletişim kutusunda, Sayfa sekmesine gidin.
5. Ölçeklendirme altında "Uygun Ölçek" seçeneğini seçin ve ardından şu şekilde sayfa sayısını belirtin: Genişlik için ilk kutuya (Fit to x pages wide) kaç sayfaya sığdırmak istediğinizi girin. Yükseklik için ikinci kutuya (Fit to y pages tall) kaç sayfaya sığdırmak istediğinizi girin.
<br>
<img src="2.png" width=60% />

6. Ayarları uygulamak için Tamam'a tıklayın.

## **Aspose.Cells for Node.js via C++ Kullanarak Excel'de Geniş ve Yüksek Sığdırılmış Sayfa Olarak Yazdırma**

Belirtilen bir sayfada FitToPagesWide ve FitToPagesTall ayarlarını yapmak için: İlk olarak, [örnek dosyayı](input.xlsx) yükleyin ve sonra istenilen sayfaya [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) ve [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) özelliklerini değiştirmeniz gerekir. İşte Node.js örneği:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Sayfasını Tek Sayfa Yazdırma**

Çalışma sayfasını tek sayfa olarak yazdırmak için: İlk olarak, [örnek dosyayı](sample.xlsx) yükleyin ve sonra [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) özelliğini ayarlayın. İşte Node.js örneği:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Çıktı sonucu:
<br>
<img src="3.png" width=60% />

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Sayfasındaki Tüm Sütunları Tek Sayfa Olarak Yazdırma**

Çalışma Sayfasındaki tüm sütunları tek sayfa olarak yazdırmak için: İlk olarak, [örnek dosyayı](sample.xlsx) yükleyin ve sonra [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/) nesnesinin [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) özelliğini ayarlayın. İşte Node.js örneği:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Çıktı sonucu:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="nodejs-cpp" >}}
