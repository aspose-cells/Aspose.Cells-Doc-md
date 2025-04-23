---
title: 找出VBA项目是否受密码保护，通过Node.js和C++
linktitle: 查看 VBA 项目是否已受保护
type: docs
weight: 20
url: /zh/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **在Node.js中查找VBA项目是否受保护**

你可以使用[**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)属性，判断Excel文件中的VBA（Visual Basic for Applications）项目是否被保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检测其VBA项目是否受保护，然后保护此VBA项目，再次检测。请查看控制台输出作为参考。在保护前，[**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)返回**false**，保护后返回**true**。

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

## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
