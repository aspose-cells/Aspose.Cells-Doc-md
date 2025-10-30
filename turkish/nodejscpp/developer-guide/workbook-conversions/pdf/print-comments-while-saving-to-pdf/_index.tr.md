---  
title: Node.js ile C++ kullanarak PDF’ye kaydederken Yorumları Yazdırın  
linktitle: PDF ye kaydederken Yorumları Yazdır  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Excel belgelerini PDF’ye kaydederken yorumları nasıl yazdıracağınızı Aspose.Cells for Node.js via C++ ile öğrenin.  
---  

{{% alert color="primary" %}}  

Microsoft Excel, aşağıdaki seçeneklerle PDF biçimine yazdırırken veya kaydederken yorumları yazdırmanıza izin verir  

- Hiçbiri  
- Sayfa sonunda  
- Sayfada gösterildiği gibi  

Aspose.Cells, aynı özelliği desteklemek için [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enumunu sağlar. [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enumunun üyeleri şunlardır  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **PDF'ye kaydederken yorumları yazdır**  

Aşağıdaki örnek kod, yorumları PDF'ye kaydederken nasıl kullanılacağını gösterir [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) kullanımı.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleWorkbookWithComments.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

/*
* For print no comments use "PrintCommentsType.PrintNoComments"
* and for print the comments as displayed on sheet use "PrintCommentsType.PrintInPlace"
* For Print the comments at the end of sheet we use "PrintCommentsType.PrintSheetEnd"
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save workbook in pdf format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
