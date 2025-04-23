---
title: DrawObjectEventHandler sınıfını kullanarak PDF ye dönüştürürken DrawObject ve Bound u alın (Node.js C++)
linktitle: DrawObjectEventHandler sınıfını kullanarak PDF ye render ederken DrawObject ve Bound almak
type: docs
weight: 70
url: /tr/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) adlı soyut bir sınıf sağlar ve bunun içinde [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yöntemi bulunur. Kullanıcı, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)yi uygulayabilir ve [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yöntemini kullanarak Excel'i PDF veya Görüntü’ye dönüştürürken [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) ve Sınır bilgilerini alabilir. İşte [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yönteminin parametrelerinin kısa bir açıklaması.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject), görünüm sırasında başlatılır ve döndürülür.

- x: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)'ın Solu.

- y: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)'ın Üstü.

- width: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) genişliği.

- height: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) yüksekliği.

Excel dosyasını PDF’ye dönüştürüyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) sınıfını [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) ile kullanabilirsiniz. Benzer şekilde, Excel dosyasını Görüntüye dönüştürüyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) sınıfını [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--) ile kullanabilirsiniz.

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın**

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [örnek Excel dosyasını](64716821.xlsx) yükler ve [çıkış PDF'si](64716822.pdf) olarak kaydeder. PDF’ye dönüştürürken, [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) özelliğini kullanır ve mevcut hücreler ile nesnelerin (örneğin görsellerin) [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) ve sınırlarını yakalar. Eğer [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) tipi Hücre ise, sınırını ve StringValue’sunu yazdırır. Eğer [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) tipi Görüntü ise, sınırını ve Nesne İsmini yazdırır. Daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakabilirsiniz.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");

class ClsDrawObjectEventHandler extends AsposeCells.DrawObjectEventHandler {
draw(drawObject, x, y, width, height) {
console.log("");

// Print the coordinates and the value of Cell object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Cell) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.getCell().getStringValue()}`);
}

// Print the coordinates and the shape name of Image object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Image) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.getShape().getName()}`);
}

console.log("----------------------");
}
}

async function run() {
// Load sample Excel file
const workbook = new AsposeCells.Workbook("sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");

// Specify Pdf save options
const opts = new AsposeCells.PdfSaveOptions();

// Assign the instance of DrawObjectEventHandler class
opts.setDrawObjectEventHandler(new ClsDrawObjectEventHandler());

// Save to Pdf format with Pdf save options
await workbook.saveAsync("outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

run();
```

## **Konsol Çıktısı**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
