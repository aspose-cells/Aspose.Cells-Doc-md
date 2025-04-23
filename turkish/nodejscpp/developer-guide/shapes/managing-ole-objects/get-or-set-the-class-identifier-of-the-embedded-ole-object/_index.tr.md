---  
title: Gömülü OLE Nesnesinin Sınıf Tanımlayıcısını Node.js ve C++ kullanarak alın veya ayarlayın  
linktitle: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın  
type: docs  
weight: 200  
url: /tr/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Aspose.Cells kullanarak Node.js de gömülü OLE nesnelerinin sınıf tanımlayıcısını nasıl alıp ayarlayacağınızı öğrenin, C++ ile.  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells, gömülü OLE nesnesinin sınıf tanımlayıcısını almak veya ayarlamak için [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) özelliği sağlar. OLE nesne sınıf tanımlayıcıları aslında GUID'ler yani, Küresel Benzersiz Tanımlayıcılar. GUID her zaman 16 bayt uzunluğundadır; bu nedenle, sınıf tanımlayıcıları da 16 bayt uzunluğundadır. Genellikle Windows Kayıt Defteri içinde bulunurlar ve ana uygulamaya, içeriğinde çeşitli embed edilmiş kaynaklar bulunan gömülü OLE nesnelerini nasıl açacağına dair bilgi sağlarlar.

## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**  
Aşağıdaki ekran görüntüsü, gömülü PowerPoint OLE nesnesi içeren örnek Excel dosyasından (5115190.xls) alınan OLE nesnesinin sınıf tanımlayıcısı yani GUID'yi gösterir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Örnek Kod**  
Lütfen aşağıdaki örnek kodu, [örnek Excel dosyası](5115190.xls) ile çalıştırıldığında ve konsol çıktısı alınırken görebileceğiniz, OLE nesnesinin sınıf tanımlayıcısını veya GUID'yi gösteren çıktı ile birlikte inceleyin. Yazdırılan GUID, ekran görüntüsünde gösterildiği gibi aynıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Konsol Çıktısı**  
Yukarıdaki örnek kodun, [örnek Excel dosyası](5115190.xls) kullanılarak çalıştırıldığında aldığı konsol çıktısı.

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

