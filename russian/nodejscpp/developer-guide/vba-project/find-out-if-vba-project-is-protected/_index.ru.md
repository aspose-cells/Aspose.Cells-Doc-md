---
title: Узнайте, защищен ли проект VBA паролем с помощью Node.js через C++
linktitle: Определение, защищен ли проект VBA
type: docs
weight: 20
url: /ru/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Узнайте, защищен ли проект VBA паролем в Node.js**

Вы можете определить, защищен ли проект VBA (Visual Basic Applications) вашего файла Excel, используя свойство [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) Aspose.Cells.

## **Образец кода**

Следующий пример создает рабочую книгу и проверяет, защищен ли ее проект VBA, затем защищает проект VBA и снова проверяет, защищен ли его проект VBA. Ознакомьтесь с выводом этой программы в консоли в качестве примера. Перед защитой [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) возвращает **false**, но после защиты — **true**.

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **Вывод в консоль**

Это вывод консоли приведенного выше образца кода для справки.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
