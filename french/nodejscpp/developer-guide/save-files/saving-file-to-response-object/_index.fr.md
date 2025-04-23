---  
title: Enregistrement du fichier dans l objet Response avec Node.js via C++  
linktitle: Enregistrement du fichier dans l objet de réponse  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/saving-file-to-response-object/  
description: Apprenez comment générer dynamiquement des fichiers et les envoyer directement au navigateur du client en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells permet de manipuler des fichiers. Cet article explique les différentes façons de sauvegarder des fichiers dans un objet de réponse.  

{{% /alert %}}  

## **Enregistrer le fichier dans l'objet Response**  

Il est également possible de générer un fichier dynamiquement et de l'envoyer directement au navigateur du client. Pour ce faire, utilisez une version surchargée spéciale de la méthode [**Save**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-stream-string-contentDisposition-saveOptions-) qui accepte les paramètres suivants :  

- Objet réponse Node.js.  
- Nom du fichier.  
- [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/), le type de disposition de contenu du fichier de sortie.  
- [**SaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/saveoptions/), le type de format de fichier.  

L'énumération [**ContentDisposition**](https://reference.aspose.com/cells/nodejs-cpp/contentdisposition/) détermine si le fichier envoyé au navigateur offre l'option de l'ouvrir directement dans le navigateur ou dans une application associée à .xls/.xlsx ou une autre extension.  

L'énumération contient les types de sauvegarde prédéfinis suivants :  

|**Type**|**Description**|  
| :- | :- |  
|Pièce jointe|Envoie la feuille de calcul au navigateur et l'ouvre dans une application en tant que pièce jointe associée à .xls/.xlsx ou autres extensions.|  
|Incorporée|Envoie le document au navigateur et offre la possibilité de sauvegarder la feuille de calcul sur le disque ou l'ouvrir dans le navigateur.|  

### **Fichiers XLS**  

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

### **Fichiers XLSX**  

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

### **Fichiers PDF**  

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

### **Remarque**  

En raison de l'absence d'un objet réponse standard dans Node.js, cette fonctionnalité n'existe pas dans Aspose.Cells for Node.js via C++. Vous pouvez consulter le code suivant pour enregistrer le fichier dans le flux, puis effectuer des opérations sur le flux.  

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


