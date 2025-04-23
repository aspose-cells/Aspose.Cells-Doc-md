---  
title: Grafiği SVG formatında görsele dönüştürmek Node.js ve C++ kullanımıyla  
linktitle: SVG Formatında Görüntüye Grafik Dönüştürme  
type: docs  
weight: 240  
url: /tr/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Aspose.Cells for Node.js via C++ kullanarak bir grafiği SVG formatında görsele dönüştürmeyi öğrenin.  
---  

{{% alert color="primary" %}}  

Ölçeklenebilir Vektör Grafikleri (SVG), aynı zamanda etkileşimliliği ve animasyonu destekleyen iki boyutlu grafikler için XML tabanlı bir vektör görüntü formatıdır. SVG belirtmesi, 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.  

SVG görüntüleri ve davranışları, XML metin dosyalarında tanımlanır. Bu, aranabilir, dizine eklenir, betiklenir ve sıkıştırılabilir anlamına gelir. XML dosyaları olarak, SVG görüntüleri herhangi bir metin düzenleyici ile oluşturulabilir ve düzenlenebilir, ancak genellikle çizim yazılımı ile oluşturulur.  

Aspose.Cells, grafikleri BMP, JPEG, PNG, GIF, SVG ve diğer formatlarda görsellere kaydedebilir. Bu makale, bir grafiği SVG formatında kaydetme yöntemini anlatmaktadır.  

{{% /alert %}}  

Aşağıdaki örnek kod, Aspose.Cells'in bir grafiği SVG biçimli bir resme dönüştürmek için nasıl kullanılacağını açıklar. Kod, kaynak Microsoft Excel dosyasını yükler ve ardından ilk çalışta bulunan ilk grafiği SVG biçiminde kaydeder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

