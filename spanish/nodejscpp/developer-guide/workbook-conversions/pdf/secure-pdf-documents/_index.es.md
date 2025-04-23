---
title: Documentos PDF seguros con Node.js mediante C++
linktitle: Documentos PDF seguros
type: docs
weight: 120
url: /es/nodejs-cpp/secure-pdf-documents/
description: Aprenda cómo asegurar documentos PDF usando contraseñas de propietario y usuario, y establecer permisos para archivos PDF usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan trabajar con archivos PDF encriptados. Por ejemplo:

- Asegurar los documentos con contraseñas de propietario y usuario para que no cualquier persona pueda abrirlo.
- Establecer restricciones o permisos al documento después de que se abra. Por ejemplo: restringir si el contenido del documento puede imprimirse o extraerse.

Este artículo explica cómo pasar opciones de seguridad en PDF al guardar hojas de cálculo en PDF.

{{% /alert %}}

Aspose.Cells proporciona [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) para trabajar con seguridad. Puede establecer contraseñas de propietario y de usuario al guardar en PDF. La contraseña de propietario o de usuario será necesaria para abrir el documento PDF encriptado para su visualización.

- La contraseña de usuario puede ser nula o una cadena vacía; en este caso, no se requerirá contraseña del usuario al abrir el documento PDF.
- Abrir el documento PDF con la contraseña de propietario correcta permite acceso completo (sin restricciones de acceso especificadas) al documento.
- Abrir el documento PDF con la contraseña de usuario correcta (o abrir un documento que no tenga una contraseña de usuario) permite acceso limitado, según los permisos especificados.

El código de muestra a continuación describe cómo asegurar PDFs con Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizarla en PDF. Esto asegura que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
