---
title: Gestionar códigos VBA del libro de trabajo habilitado para macros de Excel
linktitle: Proyecto de Macros
type: docs
weight: 200
url: /es/nodejs-cpp/manage-vba-project/
description: Añadir módulo VBA y modificar VBA o Macro con Aspose.Cells for Node.js via C++.
---

## **Agregar un módulo VBA en Node.js**
{{% alert color="primary" %}}

Aspose.Cells permite agregar un nuevo módulo VBA y código macro usando Aspose.Cells for Node.js via C++. Por favor, usa el método [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) para agregar un nuevo módulo VBA dentro del libro de trabajo

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y añade un nuevo módulo VBA y Código Macro y guarda la salida en formato XLSM. Una vez que abras el archivo XLSM en Microsoft Excel y hagas clic en **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y en su interior, el siguiente código macro.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Aquí tienes el código de ejemplo para generar el archivo XLSM de salida con módulo VBA y código macro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Modificar VBA o Macro en Node.js**

{{% alert color="primary" %}} 

Puedes modificar el código VBA o Macro usando Aspose.Cells for Node.js via C++. Aspose.Cells ha añadido el siguiente módulo y clases para leer y modificar el proyecto VBA en el archivo de Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código de VBA o macro dentro del archivo de Excel fuente utilizando Aspose.Cells.

{{% /alert %}} 

El siguiente código de ejemplo carga el archivo de Excel fuente que contiene el siguiente código VBA o Macro:

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Después de la ejecución del código de ejemplo de Aspose.Cells, el código de VBA o macro será modificado de la siguiente manera

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5112508.xlsm) y el [archivo de Excel de salida](5112511.xlsm) desde los enlaces proporcionados.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Temas avanzados**
- [Agregar una referencia de librería al proyecto de VBA en el libro de trabajo](/cells/es/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Asignar Macro a un control de formulario](/cells/es/nodejs-cpp/assign-macro-to-form-control/)
- [Comprobar si la firma digital del código VBA es válida](/cells/es/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Comprobar si el código VBA está firmado](/cells/es/nodejs-cpp/check-if-vba-code-is-signed/)
- [Comprobar si el proyecto de VBA en un libro de Excel está firmado](/cells/es/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Comprobar si el proyecto de VBA está protegido y bloqueado para ver](/cells/es/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino](/cells/es/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firmar digitalmente un proyecto de código VBA con certificado](/cells/es/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado de VBA a archivo o flujo de datos](/cells/es/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrar proyecto de VBA al cargar un libro de Excel](/cells/es/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Descubrir si el proyecto de VBA está protegido](/cells/es/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto de VBA del libro de Excel](/cells/es/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

