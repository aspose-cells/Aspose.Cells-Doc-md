---
title: Descubra si el proyecto VBA está protegido con Node.js mediante C++
linktitle: Descubrir si el Proyecto VBA está Protegido
type: docs
weight: 20
url: /es/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Descubrir si el proyecto VBA está protegido en Node.js**

Puede verificar si el proyecto VBA (Visual Basic for Applications) de su archivo de Excel está protegido o no usando Aspose.Cells y la propiedad [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--).

## **Código de muestra**

El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto VBA y vuelve a verificar si está protegido o no. Consulte la salida de la consola para referencia. Antes de la protección, [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) devuelve **false** pero después de la protección, devuelve **true**.

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

## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
