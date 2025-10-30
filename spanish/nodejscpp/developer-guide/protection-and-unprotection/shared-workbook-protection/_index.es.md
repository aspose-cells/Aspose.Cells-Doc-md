---
title: Protege o desbloquea por contraseña el libro compartido con Node.js via C++
linktitle: Proteger o Quitar Protección al Libro de Trabajo Compartido
type: docs
weight: 10
url: /es/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Escenarios de uso posibles**

Puedes proteger o desbloquear el libro compartido con Microsoft Excel como se muestra en la siguiente captura. Aspose.Cells for Node.js via C++ también soporta esta función con los métodos [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) y [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteger o Quitar Protección al Libro de Trabajo Compartido**

El siguiente código de ejemplo crea un libro de trabajo y lo protege mientras habilita el uso compartido y lo guarda como [archivo de Excel de salida](55541777.xlsx). La captura de pantalla muestra que cuando intentas quitar la protección, Microsoft Excel te pedirá que ingreses la contraseña para quitarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
