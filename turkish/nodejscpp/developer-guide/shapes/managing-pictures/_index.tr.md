---  
title: C++ kullanarak Node.js ile Resimleri Yönetmek  
linktitle: Resim Yönetimi  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/managing-pictures/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma tablolarına resim ekleme ve konumlandırmayı öğrenin.  
---  

Aspose.Cells, geliştiricilere çalışma zamanında elektron mikroskobu resimlerini elektron mikroskobuna eklemelerine olanak tanır. Dahası, bu resimlerin konumu çalışma zamanında kontrol edilebilir, bu daha sonra detaylı olarak tartışılacaktır.

Bu makale, resimleri nasıl ekleyeceğinizi ve belirli hücrelerin içeriğini gösteren bir resmi nasıl ekleyeceğinizi açıklar.

## **Resim Ekleme**

Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:  
Sadece [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) metodunu çağırın ve [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) koleksiyonunu kullanarak (bunun içinde [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) nesnesi). [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) metodu aşağıdaki parametreleri alır:

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

## **Resim Konumlandırma**

Aspose.Cells kullanarak resimlerin konumlandırılmasını kontrol etmek için iki olası yol bulunmaktadır:

- Oransal konumlandırma: satır yüksekliği ve genişliğine oranla bir konum tanımlayın.
- Mutlak konumlandırma: resmi ekleyeceğiniz sayfa üzerindeki tam konumu tanımlayın, örneğin, hücrenin solundan 40 piksel ve altından 20 piksel.

### **Oransal Konumlandırma**

Geliştiriciler, [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) ve [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) özelliklerini kullanarak resimleri satır yüksekliğine ve sütun genişliğine orantılı şekilde konumlandırabilir. Bir [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) nesnesi, onun resim dizini verilerek [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) koleksiyonundan alınabilir. Bu örnek, F6 hücresine bir resim yerleştirir.

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
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Mutlak Konumlandırma**

Geliştiriciler ayrıca, [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) ve [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) özelliklerini kullanarak resimleri mutlak konumlandırabilir. Bu örnek, F6 hücresine, soldan 60 piksel ve üstten 10 piksel uzaklıkta bir resmi yerleştirir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Hücre Referansına Dayalı Resim Ekleme**

Aspose.Cells, bir çalışma sayfası hücresinin içeriğini bir görüntü şeklinde görüntülemenizi sağlar. Verilerin görüntülenmesini istediğiniz hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlandığından, o hücre veya hücre aralığındaki değişiklikler otomatik olarak grafik nesnesinde görünür.

Bir resmi, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) nesnesinin [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) metodunu çağırarak çalışma sayfasına ekleyin. Hücre aralığını, [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) nesnesinin [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) özelliği kullanılarak belirleyin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Gelişmiş Konular**
- [Hücre Metni ile Koşullu İkon Takımı Ekle](/cells/tr/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Hücre Referansına Dayalı Resim Ekle](/cells/tr/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Bir URL'den Web Resmi Yükleyerek Excel Çalışma Sayfasına Ekleyin](/cells/tr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

