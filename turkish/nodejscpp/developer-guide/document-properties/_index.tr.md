---
title: Belge Özelliklerini Node.js ile C++ kullanarak yönetin
linktitle: Belge Portalları
type: docs
weight: 80
url: /tr/nodejs-cpp/managing-document-properties/
description: Belge özelliklerini Aspose.Cells for Node.js via C++ API leriyle nasıl yöneteceğinizi öğrenin.
keywords: Node.js üzerinden C++ kullanarak Belge Özelliklerini Yönetme, Node.js kullanarak Belge Özelliklerini Alma veya Ayarlama, Node.js üzerinden C++ kullanarak Belge Özellikleri Ekle veya Sil, Node.js ile Belge Özellikleri Ekle veya Kaldır, C++ üzerinden Node.js ile Belge Özelliklerini Ekle veya Kaldır, Aspose.Cells for Node.js via C++ API leri kullanarak Belge Özelliklerine Nasıl Erişilir.
---


## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellik eklemek için yetenek sunmaktadır. Bu belge özellikleri kullanışlı bilgiler sağlar ve ayrıntıları aşağıdaki gibi 2 kategoriye ayrılmıştır.

- Sistem tanımlı (hazır) özellikler: Hazır özellikler belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Kullanıcı tanımlı özellikler son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özelleştirilmiş özelliklerdir.

{{% alert color="primary" %}}

Hazır ve özel özellikler hakkında bilinmesi gereken en önemli nokta hazır özelliklerin erişilebilir ve değiştirilebilir olduğudur, ancak oluşturulamaz veya kaldırılamaz. Öte yandan, özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel ile Belge Portalları Nasıl Yönetilir**

Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG tarzında yönetmenize olanak tanır. Lütfen Excel 2016'da **Özellikler** diyaloğunu açmak için aşağıdaki adımları izleyiniz.

1. **Dosya** menüsünden **Bilgi**'yi seçin.

|**Bilgi Menüsünü Seçme**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **Özellikler** başlığına tıklayıp "Gelişmiş Özellikler”'i seçin.

|**Gelişmiş Özellikler Seçimini Tıklama**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosya ile ilgili farklı türde bilgileri yapılandırmaya yardımcı olur. Gümrük sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Portalları İle Nasıl Çalışılır**

Geliştiriciler, Aspose.Cells ara yüz yöntemleri kullanarak belge portal değişkenlerini dinamik olarak yönetebilirler. Bu özellik, geliştiricilere dosya ile birlikte alınan bilgiyi depolama olanağı sağlar, örneğin dosyanın ne zaman alındığı, işlendiği, zaman damgalandığı v.b.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++, çıktı belgelerine API ve Sürüm Numarası bilgilerini doğrudan yazar. Örneğin, belgeyi PDF olarak dışa aktarırken, Aspose.Cells for Node.js via C++ **Uygulama** alanını 'Aspose.Cells' değeriyle doldurur ve **PDF Üreticisi** alanını, örneğin 'Aspose.Cells v17.9' ile doldurur.

Lütfen dikkat edin, Aspose.Cells for Node.js via C++'ye çıktı Belgelerinden bu bilgiyi değiştirmesini veya kaldırmasını söyleyemezsiniz.

{{% /alert %}}

### **Belge Portallarına Erişim Yöntemleri**

Aspose.Cells API'leri, hem yerleşik hem de özel belge özelliklerini destekler. Aspose.Cells'in [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasını temsil eder ve tıpkı bir Excel dosyası gibi, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı birçok çalışma sayfası içerebilir ve her biri [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfıyla temsil edilir; çalışma sayfaları koleksiyonu ise [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) sınıfı tarafından temsil edilir.

Dosyanın belge özelliklerine aşağıda anlatıldığı gibi erişmek için [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) kullanın.

- Hazır belge özelliklerine ulaşmak için [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) kullanın.
- Özel belge özelliklerine ulaşmak için [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) kullanın.

Hem [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) hem de [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--), [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) örneğinde gösterildiği gibi [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) örneğinin örneğini döndürür. Bu koleksiyon, her biri tek bir yerleşik veya özel belge özelliğini temsil eden [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) nesnesinden oluşur.

Bir özelliğe erişmek uygulama gereksinimlerine bağlıdır; yani, örneğin [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) ile gösterildiği gibi, özelliğin indeks veya adını kullanabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) sınıfı, belge özelliğinin adını, değerini ve türünü almak için izin verir:

- Özellik adını almak için [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--) kullanın.
- Özellik değerini almak için [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) değeri bir Nesne olarak döndürür.
- Özellik türünü almak için [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Bu, [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/) sıralama değeri içinden birini döndürür. Özellik türünü aldıktan sonra, uygun değeri almak için **DocumentProperty.ToXXX** metodlarından birini kullanın; [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) kullanmak yerine. **DocumentProperty.ToXXX** metodları aşağıdaki tabloda açıklanmıştır.

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) sınıfı ayrıca diğer veri tiplerinin değerlerini döndüren metodlar da sağlar.

{{% /alert %}}

|**Üye Adı**|**Açıklama**|**ToXXX Yöntemi**|
| :- | :- | :- |
|Boolean| Özellik veri türü Boolean'dır|ToBool|
|Date| Özellik veri türü DateTime'dir. Microsoft Excel'in bu tür özel bir özelliğinde sadece tarih kısmının saklandığına dikkat edin, zaman saklanamaz|ToDateTime|
|Float| Özellik veri türü Double'dır|ToDouble|
|Number| Özellik veri türü Int32'dir|ToInt|
|String|Özellik veri tipi string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Özel Belge Özellikleri Nasıl Eklenir veya Kaldırılır**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı olduğu için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Nasıl Eklenir**

Aspose.Cells API'leri, koleksiyonlara özel özellikler eklemek için [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) metodunu [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) sınıfı ile açığa çıkarmıştır. [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) metodu, özelliği Excel dosyasına ekler ve yeni belge özelliğine referans olarak bir [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) nesnesi döner.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **“İçeriğe bağlantı” Özel Özelliğin Yapılandırılması Nasıl Yapılır**

Belirli bir alanın içeriğiyle bağlantılı özel bir özellik oluşturmak için [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) metodunu çağırın ve özellik adını ve kaynağını iletin. Bir özelliğin içeriğe bağlı olarak yapılandırılıp yapılandırılmadığını [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--) özelliği ile kontrol edebilirsiniz. Ayrıca, [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) özelliği kullanılarak kaynak alan alınabilir ve [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) sınıfının.

Örneğin basit bir şablon Microsoft Excel dosyası kullanıyoruz. Çalışma kitabında, **MyRange** olarak etiketlenmiş tanımlanan bir adlandırılmış aralık, bir hücre değerine atıfta bulunur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Özel Özellikler Nasıl Kaldırılır**

Aspose.Cells kullanarak özel özellikleri kaldırmak için, [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) metodunu çağırın ve kaldırılacak belge özelliği adını iletin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Gelişmiş Konular**
- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme](/cells/tr/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme](/cells/tr/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
