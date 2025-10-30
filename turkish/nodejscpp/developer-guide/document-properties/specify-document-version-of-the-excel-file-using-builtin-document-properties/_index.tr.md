---  
title: Node.js ve C++ kullanarak Excel Dosyasının Belge Sürümünü Belge Özellikleri ile belirtin  
linktitle: Aspose.Cells ile Yerleşik Belge Özelliklerini Kullanarak Excel Dosyasının Belge Sürümünü Belirtme  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Node.js ve C++ kullanarak dahili belge özellikleri ile bir Excel dosyasının belge sürümünü programlı olarak nasıl belirteceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Bir Excel dosyasının **Sürüm numarası**nı sağ tıklayarak ve sonra Özellikler > Ayrıntılar seçerek değiştirebilirsiniz. Programlı olarak değiştirmek için lütfen [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) özelliğini Aspose.Cells API'leri ile kullanın.  

## **Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme**  

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve bu kitabın Title, Yazarlar ve Sürüm numarası gibi dahili belge özelliklerini değiştirir. Bu kod tarafından oluşturulan [çıktı Excel dosyasını](64716811.xlsx) ve modifiye edilen Sürüm numarasını gösteren ekran görüntüsünü inceleyin.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
