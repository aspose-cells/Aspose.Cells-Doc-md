---  
title: C++ kullanarak Node.js ile OLE Nesnelerini Yönetmek  
linktitle: OLE Nesneleri Yönetme  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/managing-ole-objects/  
description: Aspose.Cells for Node.js via C++ numaralı çalışma sayfasında OLE nesnelerini nasıl yöneteceğinizi öğrenin. Çalışma sayfalarında OLE nesneleri ekleyin, çıkarın ve manipüle edin.  
---  

## **Giriş**  

OLE (Nesne Bağlama ve Gömme), karmaşık belge teknolojileri için bir çerçevedir. Kısaca, karmaşık bir belge, görsel ve bilgi nesnelerini içerebilen bir masaüstü görünümüne sahip şeydir: metinler, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller ve diğerleri. Her masaüstü nesnesi, kullanıcıyla etkileşim kurabilen ve ayrıca masaüstündeki diğer nesnelerle iletişim kurabilen bağımsız bir program birimidir.  

OLE birçok farklı program tarafından desteklenir ve bir programda oluşturulan içeriğin başka bir programda kullanılabilir hale getirilmesi amacıyla kullanılır. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Hangi içerik türlerinin ekleneceğine bakmak için, **Ekle** menüsünden **Nesne**'ye tıklayın. Yüklenmiş ve OLE nesnelerini destekleyen programlar **Nesne Türü** kutusunda görünür.  

### **Çalışsayan Elemanları Çalışsayan Eleman (OLE) Nesnesi Ekleme**  

Aspose.Cells for Node.js via C++, çalışma sayfalarında OLE nesneleri ekleme, çıkarma ve manipüle etme işlemlerini destekler. Bu nedenle, Aspose.Cells'de yeni bir OLE Nesnesi koleksiyona ekmek için [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection) sınıfı bulunmaktadır. Başka bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri vardır:  

- [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) özelliği, bayt dizisi biçiminde olan resim (simge) verisini belirtir. Bu görüntü, çalışma sayfasında OLE Nesnesini göstermek için gösterilecektir.  
- [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) özelliği, nesne verisini bayt dizisi biçiminde belirtir. Bu veriyi çift tıklayarak ilgili programda gösterilir.  

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.  

```javascript
const fs = require("fs");
const path = require("path");
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
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**  

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.  

Kodu çalıştırdıktan sonra, ilgili Çalışsayan Elemanın biçim türlerine dayalı olarak farklı dosyaları kaydedebiliriz.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Gömülü MOL Dosyasının Çıkarılması**  

Aspose.Cells for Node.js via C++, MOL (Moleküler veri dosyası, atomlar ve bağlar hakkındaki bilgileri içerir) gibi nadir türdeki nesnelerin çıkarılmasını destekler. Aşağıdaki kod parçası, gömülü bir MOL dosyasını çıkarmayı ve [örnek excel dosyası](94896196.xlsx) kullanarak diske kaydetmeyi gösterir.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Gelişmiş Konular**  
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme](/cells/tr/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Ole Nesnesi Olarak Bir WAV Dosyası Eklemek](/cells/tr/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


