---  
title: Cargar una imagen web desde una URL en una hoja de cálculo de Excel con Node.js mediante C++  
linktitle: Cargar una Imagen Web desde una URL en una Hoja de Excel  
type: docs  
weight: 30  
url: /es/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Cómo convertir una imagen desde URL a una imagen real de Excel usando Aspose.Cells for Node.js via C++.  
keywords: excel mostrar imagen desde URL, excel URL a imagen, mostrar imagen en excel desde URL, excel insertar imagen desde URL, convertir URL en imagen en excel, imagen de excel desde URL, cargar imagen desde URL en excel, Node.js, Excel  
---  

## Cargar una imagen desde una URL en una hoja de Excel  

Aspose.Cells for Node.js via C++ proporciona una forma sencilla y fácil de cargar imágenes desde URLs en hojas de cálculo de Excel. Este artículo explica cómo descargar los datos de la imagen en un stream y luego insertarla en la hoja de cálculo usando la API Aspose.Cells. Con este método, las imágenes se convierten en parte del archivo de Excel y no se descargan cada vez que se abre la hoja de cálculo.  

## Código de Muestra  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const https = require("https");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "webimagebook.out.xlsx");
const url = "https://www.aspose.com/Images/aspose-logo.jpg"; // Changed http to https

let objImage;

https.get(url, (res) => {
const chunks = [];

res.on("data", (chunk) => {
chunks.push(chunk);
```  

{{% alert color="primary" %}}  
Puede haber casos en los que siempre deseas la imagen actualizada desde una URL. Para lograr esto, puedes seguir las instrucciones dadas en el artículo [Insertar una Imagen Vinculada desde Dirección Web](/cells/es/nodejs-cpp/insert-a-linked-picture-from-web-address/). Siguiendo este método, la imagen se carga desde la URL cada vez que se abre la hoja de cálculo.  
{{% /alert %}}  


