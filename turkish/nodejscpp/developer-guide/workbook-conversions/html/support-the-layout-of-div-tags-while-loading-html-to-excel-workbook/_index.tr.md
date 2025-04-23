---  
title: Modaların düzenini destekleyin ve Node.js kullanarak HTML yi Excel çalışma kitabına yükleyin.  
linktitle: HTML yi Excel çalışma kitabına yüklerken div etiketlerinin düzenini destekleyin.  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/  
---  

{{% alert color="primary" %}}  
Genellikle, HTML'yi yüklerken div etiketlerinin düzeni göz ardı edilir. Ancak, div etiketlerinin düzeninin göz ardı edilmemesini istiyorsanız, lütfen [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--) özelliğini **true** olarak ayarlayın. Bu özelliğin varsayılan değeri **false**'dur.  
{{% /alert %}}  

Aşağıdaki örnek kod, [HtmlLoadOptions.getSupportDivTag()](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getSupportDivTag--) özelliğinin kullanımını gösterir. Lütfen giriş HTML'sinde kullanılan [Aspose Logosu](5115218.png) ve kod tarafından oluşturulan [çıktı Excel dosyasını](5115220.xlsx) indirin.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const exportHtml = `
<html>
<body>
<table>
<tr>
<td>
<div>This is some Text.</div>
<div>
<div>
<span>This is some more Text</span>
</div>
<div>
<span>abc@abc.com</span>
</div>
<div>
<span>1234567890</span>
</div>
<div>
<span>ABC DEF</span>
</div>
</div>
<div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
</td>
<td>
<img src="${dataDir}/ASpose_logo_100x100.png" />
</td>
</tr>
</table>
</body>
</html>`;

const ms = Buffer.from(exportHtml, "utf-8");

// Specify HTML load options, support div tag layouts
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setSupportDivTag(true);

// Create workbook object from the html using load options
const wb = new AsposeCells.Workbook(ms, loadOptions);

// Auto fit rows and columns of first worksheet
const ws = wb.getWorksheets().get(0);
ws.autoFitRows();
ws.autoFitColumns();

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "DivTagsLayout_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

