---  
title: Как контролировать панель вкладок листа с помощью Node.js через C++  
linktitle: Как управлять панелью вкладок листа  
type: docs  
weight: 600  
url: /ru/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Узнайте, как управлять панелью вкладок листа с помощью Aspose.Cells for Node.js via C++.  
keywords: Как управлять панелью вкладок листа Node.js через C++, выполнять действия с панелью вкладок Node.js через C++, устанавливать панель вкладок Node.js через C++, управлять панелью вкладок Node.js через C++.  
---  

## **Возможные сценарии использования**  
Если вам нужно настроить отображение панели листов Excel, необходимо знать, как управлять панелью вкладок листа, например, скрывать или показывать панель вкладок, изменять ширину панели вкладок, устанавливать первый видимый вкладка и так далее. Aspose.Cells for Node.js via C++ поддерживает эти функции. Aspose.Cells предоставляет следующие свойства и методы, которые помогут вам в достижении ваших целей.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Как управлять панелью вкладок листа с помощью Aspose.Cells for Node.js via C++**  
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Отобразите панель вкладок и установите ширину панели вкладок.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Предварительный просмотр результирующего файла:  
<br>  
<image src="result.png" width="70%" />  


