---  
title: Node.js üzerinden C++ ile Excel yi PDF ye dönüştürürken Timeline Çizimi  
linktitle: Excel i PDF ye dönüştürürken Zaman Çizelgesi çizin  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Aspose.Cells for Node.js via C++ ile Excel dosyalarının zaman çizelgelerini yönetin.  
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 kullanmadan Timeline ı PDF ye dönüştürme, Node.js üzerinden C++  
---  

## **Excel'i PDF'ye dönüştürürken Zaman Çizelgesi çizin**  
Bir zaman çizelgesinin uygulandığı bir Excel dosyanız varsa ve bu Excel'i zaman çizelgesi ayarlarıyla PDF'ye aktarmak istiyorsanız, Aspose.Cells for Node.js via C++ artık varsayılan olarak bunu destekler. Basitçe, zaman çizelgesi içeren Excel dosyasını PDF olarak dışa aktarın ve oluşturulan PDF'de zaman çizelgesi görülecektir.  

Aşağıdaki örnek kod, var olan bir zaman çizelgesi içeren [örnek Excel dosyasını](input.xlsx) yükler. Ardından, çalışma kitabını [çıktı PDF dosyası](out.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, kaynak Excel dosyasını ve oluşturulan PDF dosyasını karşılaştırır.  

<img src="out.png" width="60%">  

## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
