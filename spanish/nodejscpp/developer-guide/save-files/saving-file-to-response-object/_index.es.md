---  
title: Guardar Archivo en Objeto de Respuesta con Node.js a través de C++  
linktitle: Guardando archivo en objeto de respuesta  
type: docs  
weight: 50  
url: /es/nodejs-cpp/saving-file-to-response-object/  
description: Aprende cómo generar archivos dinámicamente y enviarlos directamente a un navegador cliente usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells hace posible manipular archivos. Este artículo explica las diferentes formas en las que los archivos se pueden guardar en un objeto de respuesta.  

{{% /alert %}}  

## **Guardando archivo en objeto de respuesta**  

También es posible generar un archivo dinámicamente y enviarlo directamente a un navegador cliente. Para hacerlo, usa una versión especial sobrecargada del método [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) que acepta los siguientes parámetros:  

- Objeto de respuesta de Node.js.  
- Nombre de archivo.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), el tipo de disposición de contenido del archivo de salida.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), el tipo de formato de archivo  

La enumeración [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) determina si el archivo enviado al navegador ofrece la opción de abrirse por sí mismo directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.  

La enumeración contiene los siguientes tipos de guardado predefinidos:  

|**Tipo**|**Descripción**|  
| :- | :- |  
|Archivo adjunto|Envía la hoja de cálculo al navegador y se abre en una aplicación como un archivo adjunto asociado con .xls/.xlsx u otras extensiones|  
|En línea|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrir dentro del navegador|  

### **Archivos XLS**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const workbook = new AsposeCells.Workbook();

// If response is not null
let response = null;

if (response != null) {
// Save in Excel2003 XLS format
workbook.save(response, path.join(dataDir, "output.xls"), AsposeCells.ContentDisposition.Inline, new AsposeCells.XlsSaveOptions());
response.end();
}
```  

### **Archivos XLSX**  

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook();

if (Response != null) {
// Save in Xlsx format
workbook.saveAsync(Response, path.join(dataDir, "output.xlsx"), AsposeCells.ContentDisposition.Attachment, new AsposeCells.OoxmlSaveOptions()).then(() => {
Response.end();
```  

### **Archivos PDF**  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.pdf");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

if (Response != null) {
// Save in Pdf format
workbook.saveAsync(Response, filePath, AsposeCells.ContentDisposition.Attachment, new AsposeCells.PdfSaveOptions()).then(() => {
Response.end();
```  

### **Nota**  

Debido a la ausencia de un objeto de respuesta estándar en Node.js, esta funcionalidad no existe en Aspose.Cells for Node.js via C++. Puedes consultar el siguiente código para guardar el archivo en el flujo, luego realizar operaciones en el flujo.  

```javascript
const path = require("path");
const { Workbook, SaveFormat } = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(null, SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.end(stream);

// Return the response
return;
}
```  


