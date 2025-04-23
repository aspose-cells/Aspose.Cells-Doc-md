---  
title: İçeriğe Yorum veya Şekil Kenar Boşluklarını Node.js kullanarak C++ ile Ayarla  
linktitle: Çalışma Sayfası İçindeki Yorum veya Şeklin Kenar Boşluklarını Ayarlama  
type: docs  
weight: 1500  
url: /tr/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel çalışma sayfası içindeki yorumların veya şekillerin kenar boşluklarını nasıl ayarlayacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells, herhangi bir şekil veya yorumun kenar boşluklarını [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/) özelliği kullanarak ayarlamanıza olanak tanır. Bu özellik, [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) sınıfının nesnesini döner ve [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--) vb. farklı özelliklere sahiptir; bunlar üst, sol, alt ve sağ kenar boşluklarını ayarlamak için kullanılabilir.  

## **Çalışma Sayfası İçindeki Yorum veya Şeklin Kenar Boşluklarını Ayarlama**  

Lütfen aşağıdaki örnek koda bakınız. [Örnek Excel dosyasını](61767851.xlsx) yükler, içinde iki şekil bulunan kod, şekilleri sırayla erişir ve bunların üst, sol, alt ve sağ kenar boşluklarını ayarlar. Kodun çıktısı olan [çıktı Excel dosyasına](61767852.xlsx) ve çıktı Excel dosyasındaki kodun etkisini gösteren ekran görüntüsüne aşağıdan bakınız.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

