---
title: Проверьте, защищен ли и заблокирован для просмотра VBA проект в Node.js через C++
linktitle: Проверка защищен ли проект VBA и заблокирован для просмотра
type: docs
weight: 30
url: /ru/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Узнайте, как проверить, защищен ли и заблокирован для просмотра VBA проект в Excel с помощью Aspose.Cells for Node.js via C++.
---

## Проверка, защищен ли и заблокирован для просмотра VBA-проект в Node.js

Aspose.Cells позволяет проверить, защищен ли VBA-проект файла Excel и заблокирован ли для просмотра. Для этого API предоставляет свойство [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). Если он заблокирован для просмотра, то свойство [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) возвращает **true**.

## **Образец кода**

Следующий пример кода загружает [пример файла Excel](43352065.xlsm) и проверяет, защищен ли VBA (Visual Basic for Applications) проект этого файла для просмотра. Также смотрите его вывод в консоли для справки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Вывод в консоль**

Это вывод в консоль вышеупомянутого примера кода при выполнении с предоставленным [образцовым файлом Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
