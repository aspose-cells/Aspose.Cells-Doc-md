---  
title: Belirtilen Yazıcı Kağıt Boyutuyla Çalışma Kitabını Node.js ve C++ kullanarak Yükleyin  
linktitle: Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle  
type: docs  
weight: 430  
url: /tr/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabını yüklerken yazıcı kağıt boyutunu nasıl ayarlayacağınızı öğrenin.  
---  

{{% alert color="primary" %}}  
Belirtilen Yazıcı Kağıdı Boyutu ile Çalışma Kitabını Yükle  
{{% /alert %}}  

Aşağıdaki örnek kod, [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-) metodunun kullanımını gösterir. Önce bir çalışma kitabı oluşturur, sonra hafıza akışına XLSX formatında kaydeder. Ardından, A5 kağıt boyutuyla yükler ve PDF olarak kaydeder. Daha sonra tekrar A3 kağıt boyutuyla yükler ve tekrar PDF olarak kaydeder. Çıkış PDF'leri açıp kağıt boyutlarını kontrol ederseniz, farkı göreceksiniz; biri A5, diğeri A3. Lütfen, kod tarafından üretilen [A5 çıkış PDF'sini](5115234.pdf) ve [A3 çıkış PDF'sini](5115233.pdf) indirin ve inceleyin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
