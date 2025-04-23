---  
title: Extensiones Web  Complementos de Office con Node.js a través de C++  
linktitle: Extensiones Web  Complementos de Office  
type: docs  
weight: 130  
url: /es/nodejs-cpp/web-extensions-office-add-ins/  
---  

Las extensiones web extienden las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las extensiones web añaden funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puedes agregar Extensiones Web (Complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En la caja de Complementos, busca el complemento que deseas y agrégalo.

Aspose.Cells también ofrece la función de agregar Extensiones Web utilizando las clases [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane). La siguiente muestra de código demuestra cómo usar las clases [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) para agregar una extensión web a un archivo Excel. Consulta el [archivo Excel de salida](89849869.xlsx) generado por el código como referencia.

### **Código de muestra**

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

## **Acceder a la Información de la Extensión Web**

Aspose.Cells permite acceder a la información de las Extensiones Web en un archivo Excel. La siguiente muestra de código demuestra cómo acceder a la información de la extensión web cargando el [archivo Excel de ejemplo](89849870.xlsx). Consulta la salida de la consola generada por el código.

### **Código de muestra**

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

### **Salida de la consola**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

