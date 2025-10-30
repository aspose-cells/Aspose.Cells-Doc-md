---  
title: Node.js ile C++ kullanarak Excel dosyalarına Resimler ve Şekiller Ekleme  
linktitle: Şekiller  
type: docs  
weight: 140  
url: /tr/nodejs-cpp/insert-shapes/  
description: Excel dosyalarında resimleri, OLE nesnelerini ve şekilleri Aspose.Cells for Node.js via C++ kullanarak yönetin.  
---  

{{% alert color="primary" %}}  
Bazen çalışma sayfasına gerekli şekillerden bazılarını eklemeniz gerekir. Aynı şekli farklı konumlara eklemeniz gerekebilir. Veya çalışma sayfasına toplu halde şekil eklemek isteyebilirsiniz.  
Endişelenmeyin! [Aspose.Cells](https://products.aspose.com/cells/), tüm bu operasyonları destekler.  
{{% /alert %}}  

Excel'deki şekiller esasen aşağıdaki türlere ayrılır:  
- **Resimler**  
- **OleObjects**  
- **Çizgiler**  
- **Dikdörtgenler**  
- **Temel Şekiller**  
- **Blok Okları**  
- **Denklem Şekilleri**  
- **Akış Şemaları**  
- **Yıldızlar ve Pankartlar**  
- **Çağrılar**  

Bu kılavuz belgesi, her türden bir veya iki şekli örnek olarak seçecek. Bu örnekler aracılığıyla, [Aspose.Cells](https://products.aspose.com/cells/) kullanarak belirli şekli çalışma sayfasına nasıl ekleyeceğinizi öğreneceksiniz.  

## **Node.js kullanarak Excel çalışma sayfasına Resim Ekleme**  

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:  
Sadece [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) metodunu çağırın ve [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) koleksiyonunu kullanarak (bunun içinde [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) nesnesi). [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) metodu aşağıdaki parametreleri alır:  

- **Sol üst satır dizini**, sol üst sütunun dizini.  
- **Sol üst sütun dizini**, sol üst sütunun dizini.  
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Node.js kullanarak Excel Çalışma Sayfasına OLE Nesnesi Ekleme**  

Aspose.Cells, çalışma sayfalarında OLE nesneleri ekleme, çıkarma ve düzenleme desteği sağlar. Bu nedenle, Aspose.Cells, koleksiyon listesine yeni bir OLE Nesnesi ekmek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection) sınıfına sahiptir. Diğer bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri şunlardır:  

- [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) özelliği, bayt dizisi biçiminde olan resim (simge) verisini belirtir. Bu görüntü, çalışma sayfasında OLE Nesnesini göstermek için gösterilecektir.  
- [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) özelliği, nesne verisini bayt dizisi biçiminde belirtir. Bu veriyi çift tıklayarak ilgili programda gösterilir.  

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Node.js kullanarak Excel Çalışma Sayfasına Çizgi Ekleme**  

Çizgi şekli, **çizgiler** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Satırı eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından çizgiyi seçin  

![](line.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir satır eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Yöntem, bir [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl çizgi ekleyeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](line2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Çizgi okuğu Ekleme**  

Çizgi okuğu şekli, **Çizgiler** kategorisine aittir. Bu, çizginin özel bir durumudur.  

***Microsoft Excel'de (örneğin 2007):***  

- Ok satırını eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Çizgiler' arasından çizgi okuğu seçin  

![](line_arrow1.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir ok satırı eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Yöntem, bir [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl çizgi okuğu ekleyeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](line_arrow2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Dikdörtgen Ekleme**  

Dikdörtgen şekli, **Dikdörtgenler** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Dikdörtgeni eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Daha sonra, 'Son Kullanılan Şekiller' veya 'Dikdörtgenler' arasından dikdörtgeni seçin  

![](rectangle.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir dikdörtgen eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Yöntem, bir [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape) nesnesi döner.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına nasıl dikdörtgen ekleyeceğinizi gösterir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](rectangle2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Bir Küp Ekleyin**  

Küpün şekli **Temel Şekiller** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Küpü eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Temel Şekiller**'den Küpü seçin  

![](cube.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir küp eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına küp nasıl ekleneceğini gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](cube2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Bir çağrı kutusu dörtlü ok ekleyin**  

Çağrı kutusu dörtlü ok şekli **Blok Oklar** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Çağrı ok dört ok eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Blok Oklar**'dan çağrı kutusu dörtlü ok seçin  

![](callout_quad_arrow.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına bir çağrı oku dört ok eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çağrı kutusu dörtlü ok nasıl eklenir gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](callout_quad_arrow2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Çarpım İşareti Ekleyin**  

Çarpım işaretinin şekli **Denklem Şekilleri** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Çarpma işareti eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Denklem Şekilleri**'nden çarpım işaretini seçin  

![](multiplication_sign.png)  

***Aspose.Cells Kullanarak***  

Çarpma işaretini çalışma sayfasına eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çarpım işareti nasıl eklenir gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](multiplication_sign2.png)  

## **Node.js kullanarak Çoklu Belge Ekleyin**  

Çoklu belgenin şekli **Akış Diyagramları** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Çoklu belgeyi eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Akış Diyagramları**'ndan çoklu belgeyi seçin  

![](multidocument.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına çoklu belge eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına çoklu belge nasıl eklenir gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](multidocument2.png)  

## **Node.js kullanarak Excel Çalışma Sayfasına Beş Uçlu Yıldız Ekleyin**  

Beş Uçlu Yıldızın şekli **Yıldızlar ve Bayraklar** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Beş köşeli yıldızı eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Yıldızlar ve Bayraklar**'ndan Beş Uçlu Yıldızı seçin  

![](star_5_points.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına beş köşeli yıldız eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına Beş Uçlu Yıldız nasıl eklenir gösterir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](star_5_points2.png)  

## **Node.js kullanarak Düşünce Balonu Bulutunu Excel Çalışma Sayfasına Ekleyin**  

Düşünce balonu bulutunun şekli **Çağrı** kategorisine aittir.  

***Microsoft Excel'de (örneğin 2007):***  

- Düşünce balonu bulutu eklemek istediğiniz hücreyi seçin  
- Insert menüsünü tıklayın ve Şekiller'e tıklayın.  
- Ardından, **Çağrı**'dan Düşünce Balonu Bulutunu seçin  

![](thought_bubble_cloud.png)  

***Aspose.Cells Kullanarak***  

Çalışma sayfasına düşünce balonu bulutu eklemek için aşağıdaki yöntemi kullanabilirsiniz.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Yöntem, bir [Şekil](https://reference.aspose.com/cells/nodejs-cpp/shape) nesnesi döndürür.  
{{% /alert %}}  

Aşağıdaki örnek, bir çalışma sayfasına Düşünce Balonu Bulutu nasıl eklenir gösterir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Yukarıdaki kodu çalıştırın, aşağıdaki sonuçları elde edersiniz:  

![](thought_bubble_cloud2.png)  

## **Gelişmiş Konular**  
- [Şekil Ayar Değerlerini Değiştirme](/cells/tr/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Çalışma Sayfaları Arasında Şekilleri Kopyalama](/cells/tr/nodejs-cpp/copy-shapes-between-worksheets/)  
- [İlkel Olmayan Şekildeki Veri](/cells/tr/nodejs-cpp/data-in-non-primitive-shape/)  
- [Çalışma Sayfası İçindeki Şeklin Mutlak Konumunu Bulma](/cells/tr/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Şekilden Bağlantı Noktalarını Al](/cells/tr/nodejs-cpp/get-connection-points-from-shape/)  
- [Denetimleri Yönetme](/cells/tr/nodejs-cpp/managing-controls/)  
- [Çalışma Sayfasına Simgeler Ekleme](/cells/tr/nodejs-cpp/insert-svg-to-excel/)  
- [OLE Nesnelerini Yönetme](/cells/tr/nodejs-cpp/managing-ole-objects/)  
- [Resimleri Yönetme](/cells/tr/nodejs-cpp/managing-pictures/)  
- [Akıllı Sanatı Yönetme](/cells/tr/nodejs-cpp/managing-smartart/)  
- [Metin Kutularını Yönetme](/cells/tr/nodejs-cpp/managing-textbox-of-excel/)  
- [Çalışma Sayfasına WordArt Fili Ekleme](/cells/tr/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Bağlantılı Şekillerin Değerlerini Yenileme](/cells/tr/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme](/cells/tr/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Şekil Seçeneklerini Yönetme](/cells/tr/nodejs-cpp/managing-shape-options/)  
- [Şekil Metin Seçeneklerini Yönetme](/cells/tr/nodejs-cpp/managing-shape-text-options/)  
- [Web Uzantıları - Office Eklentileri](/cells/tr/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
