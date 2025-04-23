---  
title: Excel den HTML ye dönüştürürken Kullanılmayan Stillleri Hariç Tutma ile Node.js via C++  
linktitle: Excel den HTML ye Dönüşüm Sırasında Kullanılmayan Stilleri Hariç Tut  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel den HTML ye dönüştürürken kullanılmayan stilleri nasıl hariç tutacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel dosyaları birçok kullanılmayan stili içerebilir. Excel dosyasını HTML'ye dışa aktardığınızda, bu kullanılmayan stiller de aktarılır. Bu, HTML'nin boyutunu artırabilir. Excel dosyalarını HTML'ye dönüştürürken [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) özelliğini kullanarak kullanılmayan stilleri hariç tutabilirsiniz. Bunu **true** olarak ayarladığınızda, tüm kullanılmayan stiller çıktı HTML'den hariç edilir. Aşağıdaki ekran görüntüsü, çıktı HTML içinde bulunan örnek kullanılmayan stil örneğini gösterir.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Excel dosyası oluşturan ve kullanılmayan isimli bir stil oluşturan aşağıdaki örnek kod. {0} **true** olarak ayarlandığından, bu kullanılmayan isimli stil [çıktı HTML'sine](61767778.zip) dışa aktarılmayacaktır. Ancak, **false**olarak ayarlarsanız, bu kullanılmayan stil çıktı HTML içinde bulunacaktır ve yukarıdaki ekran görüntüsünde HTML işaretleme dilinde görebilirsiniz.**  

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ayrıca kullanılmayan bir ad stil oluşturur. [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) **true** olarak ayarlandığı için, bu kullanılmayan ad stili [çıktı HTML'sine](61767778.zip) aktarılmaz. Ancak, onu **false** yaparsanız, bu kullanılmayan stil çıktı HTML'si içinde bulunur ve yukarıdaki ekran görüntüsünde gösterildiği gibi HTML biçiminde görebilirsiniz.  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

