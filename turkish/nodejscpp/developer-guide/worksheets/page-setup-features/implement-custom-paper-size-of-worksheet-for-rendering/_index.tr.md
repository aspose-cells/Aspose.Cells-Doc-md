---  
title: Render işlemi sırasında çalışma sayfası için Özel Kağıt Boyutu Uygulama  
linktitle: Otomatik Olarak Çalışma Sayfası Kağıt Boyutunun Oluşturulması için Özelleştirilmiş Kağıt Boyutunun Uygulanması  
type: docs  
weight: 70  
url: /tr/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Bu makale, Excel dosyasını PDF formatına programlı olarak dönüştürürken, istediğiniz çalışma sayfaları için C++ üzerinden Node.js API sini kullanarak özel bir kağıt boyutu ayarlamayı açıklar.  
keywords: Excel i PDF ye dönüştürürken özel kağıt boyutu ayarla Node.js ve C++ kullanımı  
---  

## **Olası Kullanım Senaryoları**  

MS Excel'de doğrudan özel kağıt boyutları oluşturmak için bir seçenek olmamasına rağmen, Excel dosyasını PDF'ye dönüştürürken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlayabilirsiniz. Bu belge, Aspose.Cells API'leri kullanarak çalışma sayfasının özel kağıt boyutunun nasıl ayarlanacağını açıklar.  

## **Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması**  

Aspose.Cells, çalışma sayfasının istediğiniz kağıt boyutunu uygulamanıza olanak tanır. [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) metodunu kullanarak özel bir sayfa boyutu belirtebilirsiniz. Aşağıdaki örnek kod, çalışma kitabının ilk çalışma sayfası için özel bir kağıt boyutunun nasıl belirtileceğini gösterir. Ayrıca, aşağıdaki kodla oluşturulan [çıktı PDF](45056028.pdf) örneği de referans alınabilir.  

## **Ekran Görüntüsü**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
