---  
title: Node.js kullanarak C++ ile sütunlar halinde bir elektronik tabloyu HTML ye dönüştürürken Varsayılan Yazı Tipini Ayarla  
linktitle: Elektronik tabloyu HTML e dönüştürürken varsayılan yazı tipini ayarlayın  
type: docs  
weight: 370  
url: /tr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells, elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlamanıza olanak tanır. Bu amaçla [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) özelliğini kullanın. Bu özellik, elektronik tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip hücreler varsa kullanışlıdır. O zaman bu hücreler [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) özelliği ile belirtilen bir yazı tipinde oluşturulacaktır.  
{{% /alert %}}  

## Elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlayın  

Aşağıdaki örnek kod bir çalışma kitabı oluşturur, ilk çalışma sayfasının B4 hücresine bir metin ekler ve yazı tipini bilinmeyen/bulunmayan bir yazı tipine ayarlar. Daha sonra, çalışma kitabını farklı varsayılan yazı tipi adları olarak Courier New, Arial, Times New Roman vb. ayarlayarak HTML olarak kaydeder.  

Ekran görüntüsü, farklı varsayılan yazı tipi adlarını [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) özelliği aracılığıyla ayarlamanın etkisini gösterir.  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Kod, [Courier New ile](5115516), [Arial ile](5115518) ve [Times New Roman ile](5115517) çıktı HTML dosyasını oluşturur.  

## Örnek Kod  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
