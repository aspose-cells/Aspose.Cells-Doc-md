---  
title: Печатать комментарии при сохранении в PDF через Node.js и C++  
linktitle: Печать комментариев при сохранении в формат PDF  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Узнайте, как печатать комментарии при сохранении документов Excel в PDF с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel позволяет печатать комментарии при печати или сохранении в формате PDF с помощью следующих параметров  

- Нет  
- В конце листа  
- Как отображено на листе  

Aspose.Cells предоставляет перечисление [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype), поддерживающее ту же функцию. Перечисление [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) содержит следующие члены  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Печать комментариев при сохранении в формат PDF**  

Следующий пример кода показывает, как использовать [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) для печати комментариев при сохранении в PDF.  

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

