---
title: Node.js ile C++ kullanarak Elektronik Tablo biçiminde yazı tiplerini yapılandırma
linktitle: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for Node.js via C++ kullanarak elektronik tablolar için yazı tiplerini yapılandırmayı öğrenin. En iyi dönüşüm doğruluğu için yazı tiplerinin kullanılabilir olması gerekir.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API’leri, elektronik tabloları görüntü biçiminde render etme ve PDF & XPS formatlarına dönüştürme özelliği sağlar. Dönüşüm doğruluğunu artırmak için, elektrik tablosunda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunması gerekir. Gerekli yazı tipleri yoksa, Aspose.Cells API'leri gerekli yazı tiplerini kullanılabilir olanlarla değiştirmeye çalışacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'ları tarafından perde arkasında izlenen süreç aşağıda belirtilmiştir.

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
2. API, aynı ebeveyn düğümü altında kullanılan varsayılan yazı tipini belirleyebilecek olan [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
3. API, yazı tipini belirleyemiyorsa, [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) veya [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
4. API, yazı tipini belirleyemiyorsa, [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) özelliği altında tanımlanan yazı tipi bulunamazsa, mevcut yazı tiplerinden en uygun olanını seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, çalışsayı Arial kullanarak elektronik tabloyu oluşturur.

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells API’leri, işletim sisteminin varsayılan yazı tipi dizininde gerekli yazı tiplerini arar. Gerekli yazı tipleri mevcut değilse, API’ler özel (kullanıcı tanımlı) dizinlerde arama yapar. [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) sınıfı, özel yazı tipi dizinleri ayarlamak için çeşitli yollar sunar.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Bu yöntem, yazı tiplerinin birden fazla klasörde bulunduğu durumda ve kullanıcı tüm klasörleri tek tek birleştirmek yerine ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Bu mekanizma, kullanıcının birden fazla klasörden veya tek bir yazı tipi dosyasından veya bayt dizisinden yazı tiplerini yüklemek istemesi durumunda kullanışlıdır.

{{% alert color="primary" %}}

[**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) ve [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) yöntemleri her ikisi de ikinci olarak gelen Boolean türünde bir parametre kabul eder. İkinci parametre olarak **true** geçmek, Aspose.Cells API'lerini yazı tipleri dosyalarını aramak için alt klasörlere yönlendirir.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Lütfen uygulamanın başlangıcında yukarıda belirtilen yöntemlerden herhangi birini kullanın; diğer Aspose.Cells API nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıda bahsedilen tüm yöntemler, yazı tiplerini ayarlamak için kullanıldığında, sadece son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells API’leri ayrıca, render işlemi için yer değiştiren yazı tipi belirleme imkanını da sağlar. Bu mekanizma, dönüşüm sırasında gereken yazı tipi sistemde mevcut değilse faydalıdır. Kullanıcılar, orijinal gerekli yazı tipi yerine kullanılacak font adlarının listesini sağlayabilir. Bunu başarmak için, Aspose.Cells API'leri, 2 parametre kabul eden [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) yöntemini açığa çıkarmıştır. Birinci parametre, **string** türünde olmalı ve değiştirilmesi gereken yazı tipinin adını temsil etmelidir. İkinci parametre ise, **string** türünde bir dizidir. Kullanıcılar, orijinal font adı yerine kullanılacak font isimlerinin listesini sağlayabilir.

İşte basit bir kullanım senaryosu.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Bilgi Toplama**

Yukarıda bahsedilen yöntemlere ek olarak, Aspose.Cells API’leri, hangi kaynakların ve yer değiştirmelerin ayarlandığını gösteren bilgiler toplamaya da imkan sağlar.

1. [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) metodu, belirtilen font kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) türünde bir dizi döndürür. Hiç kaynak ayarlanmadıysa, [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) metodu boş bir dizi döndürür.
1. [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) metodu, yerine koyma işlemi yapılmış yazı tipi adını belirtmek için **string** türünde bir parametre kabul eder. Belirtilen yazı tipi için yer değiştirme ayarlanmadıysa, [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) metodu null döner.

## **Gelişmiş Konular**
- [Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme](/cells/tr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini öncelikli şekilde ayarlayın](/cells/tr/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/nodejs-cpp/supported-font-formats/)
- [Elektronik Tabloyu Görüntüye - Görüntülenen Görüntü İçin Pixel Biçimini Ayarlama](/cells/tr/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
