---  
title: Node.js ve C++ kullanarak Çalışma Kitabından OLE Nesnelerini Çıkarın  
linktitle: Çalışma Kitabından OLE Nesneleri Çıkarma  
type: docs  
weight: 110  
url: /tr/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
 Bazen, çalışma kitabından OLE nesnelerini çıkarmanız gerekir. Aspose.Cells, bu OLE nesnelerini çıkarmayı ve kaydetmeyi destekler.

 Bu makale, Node.js ve C++ kullanarak bir konsol uygulaması oluşturmayı ve birkaç basit kod satırıyla çalışma kitabından farklı OLE nesneleri çıkarmayı gösterir.  
{{% /alert %}}  

## **Bir Çalışma Kitabından OLE Nesneleri Çıkarma**  

### **Bir Şablon Çalışma Kitabı Oluşturma**  

1. Microsoft Excel'de bir çalışma kitabı oluşturun.  
1. İlk çalışma sayfasına bir Microsoft Word belgesi, bir Excel çalışma kitabı ve bir PDF belgesi OLE nesnesi olarak ekleyin.  

|**OLE nesneleri bulunan şablon belge (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Daha sonra, OLE nesnelerini çıkarın ve ilgili dosya türleriyle sabit diske kaydedin.  

### **Aspose.Cells'i İndirin ve Yükleyin**  

1. [Aspose.Cells for Node.js via C++'ü İndiriniz](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Geliştirme bilgisayarınıza kurun.  

Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.  

### **Bir Proje Oluşturun**  

Başlat **Node.js** ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir Node.js konsol uygulamasını gösterecek, ancak herhangi bir JavaScript uyumlu ortam da kullanabilirsiniz.  

1. Bağımlılıkları Ekle  
   1. Projenize Aspose.Cells bileşenine referans ekleyin, örneğin, paketi `require` fonksiyonunu kullanarak dahil edin:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **OLE Nesnelerini Çıkarın**  

Aşağıdaki kod, OLE nesnelerini bulma ve çıkarma işlemini gerçekleştirir. OLE nesneleri (DOC, XLS ve PDF dosyaları) diske kaydedilir.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

