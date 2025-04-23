---  
title: Node.js ile C++ kullanarak Boş İş Sayfalarını Tespit Etme  
linktitle: Boş Çalışsayfası Bulma  
type: docs  
weight: 410  
url: /tr/nodejs-cpp/detecting-empty-worksheets/  
description: Bu makale, Node.js API sini ve C++ kütüphanesini kullanarak Excel iş kitaplarının boş iş sayfalarını programlı olarak nasıl tespit edeceğinizi gösterir.  
keywords: Node.js ile C++ kullanarak boş iş sayfasını tespit et, boş excel iş sayfasını bul Node.js ve C++ ile  
---  

## **Doldurulmuş Hücreleri Kontrol Etme**

İş sayfaları, içinde değerler bulunan bir veya daha fazla hücreye sahip olabilir, burada değer basit olabilir (metin, sayısal, tarih/zaman) veya bir formül ya da formül tabanlı bir değer olabilir. Bu durumda, verilen bir iş sayfasının boş olup olmadığını kolayca tespit edebilirsiniz. Kontrol etmemiz gereken tek şey [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) veya [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) özellikleridir. Yukarıda belirtilen özellikler sıfır veya pozitif değer döndürüyorsa, bu bir veya daha fazla hücreye değer atanmış anlamına gelir; ancak bu özelliklerden herhangi biri -1 ise, bu, ilgili iş sayfasında hiçbir hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonlarının sıfır tabanlı indeksleri vardır; bu nedenle, satır 0 ve sütun 0'daki bir hücre, iş sayfasındaki ilk hücre anlamına gelir, bu da A1.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerleri olan tüm hücreler otomatik olarak başlatılır; ancak, bir iş sayfasında sadece biçimlendirme uygulanan hücrelerin olma ihtimali de vardır. Bu durumda, [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) veya [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) özellikleri -1 döndürür ve bu, doldurulmuş değerlerin olmadığı anlamına gelir, ancak biçimlendirme nedeniyle başlatılmış hücreler bu yöntemle tespit edilemez. Bir iş sayfasında boş başlatılmış hücrelerin olup olmadığını kontrol etmek için, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundan alınan sayıcıda `Enumerator.MoveNext` metodunu kullanmanız önerilir. Eğer `Enumerator.MoveNext` metodu **true** dönerse, bu, ilgili iş sayfasında bir veya daha fazla başlatılmış hücre olduğunu gösterir.

## **Şekilleri Kontrol Etme**

Bir iş sayfasının herhangi bir hücre içermemesi mümkündür; ancak, şekiller ve nesneler (kontroller, grafikler, resimler vb.) içerebilir. Bir iş sayfasında şekil olup olmadığını kontrol etmek istiyorsak, [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--) özelliğini inceleyebiliriz. Pozitif herhangi bir değer, iş sayfasında şekil(s) olduğunu gösterir.

## **Programlama Örneği**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

