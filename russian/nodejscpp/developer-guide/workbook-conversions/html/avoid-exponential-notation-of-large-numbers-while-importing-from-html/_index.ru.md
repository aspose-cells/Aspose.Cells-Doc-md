---  
title: Избегайте экспоненциальной нотации больших чисел при импорте из HTML  
linktitle: Избегайте экспоненциальной нотации больших чисел при импорте из HTML  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: Узнайте, как предотвратить преобразование больших чисел в экспоненциальное нотацию при импорте из HTML с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Иногда ваш HTML содержит числа вроде 1234567890123456, которые длиннее 15 цифр, и при импорте в Excel эти числа преобразуются в экспоненциальную нотацию, например 1.23457E+15. Если вы хотите импортировать число как есть без преобразования в экспоненциальную нотацию, используйте свойство [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) и установите его в **true** при загрузке HTML.  

{{% /alert %}}  

Следующий пример кода объясняет использование свойства [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--). API импортирует число как есть, без преобразования в экспоненциальное нотацию.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";

// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);

// Convert byte array into stream
const stream = byteArray;

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
