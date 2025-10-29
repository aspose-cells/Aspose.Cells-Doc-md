---
title: Блокировка или разблокировка фигур с помощью Node.js через C++
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/nodejs-cpp/lock-or-unlock-shapes/
description: Эта статья содержит код, объясняющий, как блокировать или разблокировать фигуры для их защиты с использованием библиотеки Aspose.Cells для Node.js через C++.
keywords: Блокировка фигур в Node.js для их защиты. Как блокировать или разблокировать фигуры с помощью Node.js через C++, Заблокировать или разблокировать фигуры для защиты в Node.js через C++.
---

## **Возможные сценарии использования**

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе. 

Блокировка фигур в таблице или документе может быть полезна по нескольким причинам:
1. Предотвращение случайных изменений: блокировка фигур гарантирует, что их случайно не переместят, не изменят размер или не удалят пользователи. Особенно важно в сложных документах, где фигуры используются для аннотаций, иллюстраций или как часть дизайна документа.
1. Поддержание макета и дизайна: фигуры часто играют важную роль в раскладке и внешнем виде документа. Блокировка сохраняет задуманный внешний вид, делая документ профессиональным и визуально привлекательным.
1. Целостность данных: в таблицах фигуры могут использоваться для выделения важных данных, добавления комментариев или предоставления визуальных объяснений. Блокировка этих фигур обеспечивает сохранение точности и целостности предоставляемой ими контекстной информации.
1. Последовательность в совместных документах: при совместной работе над документами разные пользователи могут обладать разным уровнем опыта. Блокировка фигур помогает поддерживать согласованность документа, предотвращая непреднамеренные изменения.
1. Безопасность: в чувствительных документах блокировка фигур может быть частью общей стратегии защиты информации. Например, в финансовых отчетах или юридических документах заблокированные фигуры используются для защиты конкретных аннотаций или выделений, предоставляющих важный контекст.

Иногда необходимо иметь возможность изменять определенные фигуры в защищенных листах, в таком случае нужно разблокировать эти фигуры. Эта статья подробно расскажет, как блокировать и разблокировать указанные фигуры.

## **Как заблокировать фигуры для их защиты в Excel**

Вот как можно заблокировать ячейки в Microsoft Excel:

1. Откройте файл Excel: Откройте файл Excel, содержащий фигуры, которые вы хотите заблокировать.

1. Выберите фигуру: Щелкните по фигуре, которую хотите заблокировать. Также можно выбрать несколько фигур, зажав клавишу Ctrl и щелкая по каждой фигуре.

1. Откройте панель форматирования фигуры: Щелкните правой кнопкой по выбранной фигуре(ям) и выберите "Размер и свойства". Или перейдите на вкладку "Формат" на ленте и в группе "Размер" нажмите на значок диалогового окна (маленькая стрелка) для открытия панели "Формат фигуры".
1. Заблокируйте фигуру: В панели "Формат фигуры" перейдите на вкладку "Размер и свойства" (значок, похожий на квадрат со стрелками). В разделе "Свойства" установите галочку возле "Заблокировано".
<br>
<img src="1.png" width=60% />
1. Защитите лист: Перейдите на вкладку "Рецензирование" на ленте. Нажмите "Защитить лист." Установите пароль (по желанию) и выберите разрешения, которые хотите разрешить (например, выбор заблокированных ячеек, форматирование ячеек и т.д.). Нажмите "ОК."
<br>
<img src="2.png" width=60% />

## **Как заблокировать все фигуры в определенном листе**

Для защиты всех фигур на указанном листе используйте метод `worksheet.protect(ProtectionType.Objects)`, как показано в следующем примере кода.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Как разблокировать указанные фигуры в защищённом листе**

Чтобы разблокировать указанную фигуру на защищённом листе, используйте `shape.isLocked`, как показано в следующем примере кода.

Примечание: `shape.isLocked` имеет смысл только при защищённом листе.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
