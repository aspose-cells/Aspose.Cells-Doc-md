---  
title: Как установить свойство AutoRecover книги с помощью Node.js через C++  
linktitle: Как установить свойство AutoRecover в Рабочей книге  
type: docs  
weight: 220  
url: /ru/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Узнайте, как установить свойство AutoRecover книги с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Вы можете использовать Aspose.Cells для установки свойства AutoRecover книги. Значение по умолчанию этого свойства — **true**. При установке его в **false** в книге Excel отключается автоматическое восстановление (Авохранение).  

Aspose.Cells предоставляет свойство [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) для включения или отключения этой опции.  
{{% /alert %}}  

Следующий код объясняет, как использовать свойство [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) книги. Сначала он считывает значение по умолчанию, которое равно **true**, затем устанавливает его в **false** и сохраняет книгу. После этого он снова читает книгу и получает значение этого свойства, которое в настоящее время равно **false**.  

## Код Node.js для установки свойства AutoRecover книги  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Вывод**  

Вот вывод в консоль вышеуказанного образца кода.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

