---  
title: Веб расширения  надстройки Office с Node.js через C++  
linktitle: Веб расширения  дополнения для офиса  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/web-extensions-office-add-ins/  
---  

Веб-расширения расширяют возможности приложений Office и взаимодействуют с контентом в документах Office. Веб-расширения добавляют дополнительную функциональность в клиент Office для улучшения опыта пользователя и продуктивности.

Aspose.Cells также предоставляет возможность работать с веб-расширениями.

## **Добавить веб-расширение**

Вы можете добавить расширения веб (надстройки Office) в Excel, кликнув на вкладку **Вставка**, а затем на ссылку **Магазин**/**Получить надстройки**. В окне надстроек найдите нужную надстроку и добавьте её.

Aspose.Cells также предоставляет возможность добавлять расширения веб, используя классы [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane). Следующий пример демонстрирует использование классов [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) и [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) для добавления веб-расширения в файл Excel. Пожалуйста, посмотрите на [выходной файл Excel](89849869.xlsx), созданный этим кодом.

### **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

const extensions = workbook.getWorksheets().getWebExtensions();
const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

const extensionIndex = extensions.add();
const taskPaneIndex = taskPanes.add();

const extension = extensions.get(extensionIndex);
extension.getReference().setId("wa104379955");
extension.getReference().setStoreName("en-US");
extension.getReference().setStoreType(AsposeCells.WebExtensionStoreType.OMEX);

const taskPane = taskPanes.get(taskPaneIndex);
taskPane.setIsVisible(true);
taskPane.setDockState("right");
taskPane.setWebExtension(extension);

workbook.save(path.join(outDir, "AddWebExtension_Out.xlsx"));
```

## **Доступ к информации веб-расширения**

Aspose.Cells предоставляет возможность получать информацию о расширениях веб в файле Excel. Следующий пример показывает, как получить информацию о веб-расширениях, загрузив [пример файла Excel](89849870.xlsx). Обратите внимание на вывод в консоль, сгенерированный кодом.

### **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load sample Excel file
const filePath = path.join(sourceDir, "WebExtensionsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

for (let i = 0; i < taskPanes.getCount(); i++) {
const taskPane = taskPanes.get(i);
console.log("Width: " + taskPane.getWidth());
console.log("IsVisible: " + taskPane.isVisible());
console.log("IsLocked: " + taskPane.isLocked());
console.log("DockState: " + taskPane.getDockState());
console.log("StoreName: " + taskPane.getWebExtension().getReference().getStoreName());
console.log("StoreType: " + taskPane.getWebExtension().getReference().getStoreType());
console.log("WebExtension.Id: " + taskPane.getWebExtension().getId());
}
```

### **Вывод в консоль**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
