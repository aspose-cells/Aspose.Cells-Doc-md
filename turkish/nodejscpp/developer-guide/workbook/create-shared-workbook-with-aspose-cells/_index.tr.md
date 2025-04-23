---  
title: Aspose.Cells for Node.js via C++ ile Paylaşılan Çalışma Kitabı Oluşturma  
linktitle: Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Aspose.Cells for Node.js via C++ kullanarak paylaşılan bir çalışma kitabı nasıl oluşturulacağını öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Microsoft Excel, aşağıdaki ekran görüntüsünde gösterildiği gibi çalışma kitabını paylaşmanıza izin verir. Çalışma kitabını paylaştığınızda, ağda birden fazla kullanıcı çalışmayı düzenleyebilir. Aspose.Cells for Node.js via C++, [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) özelliği kullanılarak paylaşılan çalışma kitabı oluşturmanıza olanak sağlar.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cells ile Paylaşılan Çalışma Kitabı Oluşturma**  

Aşağıdaki örnek kod, [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) özelliğini **true** olarak ayarlayarak paylaşılan bir çalışma kitabı oluşturur. [Çıktı Excel dosyasını](55541786.xlsx) Microsoft Excel'de açtığınızda, bu ekran görüntüsüyle gösterildiği gibi **Paylaşılan** olarak göreceksiniz.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Örnek Kod**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

