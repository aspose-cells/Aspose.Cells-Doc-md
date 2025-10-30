---  
title: Web adresinden (http //) bir bağlantılı resmi bir çalışma sayfasına nasıl ekleyeceğinizi öğrenin.  
linktitle: Web Adresinden Bağlantılı Bir Resim Eklemek  
type: docs  
weight: 450  
url: /tr/nodejs-cpp/insert-a-linked-picture-from-web-address/  
description: Aspose.Cells for Node.js via C++ kullanarak bir web adresinden bağlanmış resmi çalışma sayfasına nasıl ekleyeceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  
Bazen, bir çalışma sayfasına web'den (http://) bir resim eklemeniz gerekir. Bunun için, resmin URL'sini belirtin ve çalışma sayfası her açıldığında resmi indirir. Resim, Excel dokümanına fiziksel olarak gömülü değildir, ancak bir web kaynağına işaret eder.  
{{% /alert %}}  

## **Microsoft Excel Kullanımı**  

Microsoft Excel'de (örneğin 2007):  

1. **Ekle** menüsünü tıklayın ve **Resim**'i seçin.  
1. Resim Ekle iletişim kutusunda resmin web adresini belirtin.  

## **Aspose.Cells for Node.js via C++ kullanımıyla**  

Aspose.Cells for Node.js via C++, [**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-) kullanarak bağlantılı resim eklemeyi destekler. Yöntem, bir [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture) nesnesi döndürür.  

Aşağıdaki örnek, bir web adresinden bağlı bir resmi çalışma sayfasına nasıl ekleyeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();
// Insert a linked picture (from Web Address) to B2 Cell.
const pic = workbook.getWorksheets().get(0).getShapes().addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");
// Set the height and width of the inserted image.
pic.setHeightInch(1.04);
pic.setWidthInch(2.6);
// Save the Excel file.
workbook.save(path.join(dataDir, "outLinkedPicture.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
