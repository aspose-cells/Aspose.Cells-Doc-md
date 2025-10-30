---  
title: Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Kitabında İmza Çizgisi Oluşturma  
linktitle: Aspose.Cells ile Excel Çalışma Kitabında İmza Satırı Oluşturma  
type: docs  
weight: 150  
url: /tr/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Kitabında İmza Çizgisi nasıl oluşturulacağını anlatır.  
keywords: Node.js ve C++ kullanarak Excel Çalışma Kitabında İmza Çizgisi Oluşturma, İmza Çizgisi Nasıl Oluşturulur?, İmza Çizgisi Ekle, Excel dosyasına İmza Çizgisi Ekle.  
---  

## **Giriş**  

Microsoft Excel, Excel çalışma kitaplarına **İmza Satırı** eklemek için bir özellik sağlar. Aspose.Cells de bu özelliği sağlar ve bunun için {0} özelliğini sunmuştur. Bu makale, bu özelliği kullanmanın nasıl olduğunu açıklar.  

## **Excel için İmza Çizgisi Oluşturmayı**  

Aspose.Cells for Node.js via C++ ayrıca bu özelliği sağlar ve bu amaçla [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) özelliği kullanılır. Bu makale, bu özelliği kullanarak Aspose.Cells ile İmza Çizgisi ekleme yöntemini açıklar.  

Aşağıdaki örnek kod, [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) özelliğini kullanarak İmza Çizgisi ekler ve çalışma kitabını kaydeder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
