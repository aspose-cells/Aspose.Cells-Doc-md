---  
title: Charger une image web depuis une URL dans une feuille Excel avec Node.js via C++  
linktitle: Charger une image web à partir d une URL dans une feuille de calcul Excel  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Comment convertir une image depuis une URL en une image Excel réelle en utilisant Aspose.Cells for Node.js via C++.  
keywords: excel afficher l image depuis url, url excel vers image, afficher image dans excel depuis url, excel insérer image depuis url, convertir url en image dans excel, image excel depuis url, charger image depuis url dans excel, Node.js, Excel  
---  

## Charger une image à partir d'une URL dans une feuille de calcul Excel  

Aspose.Cells for Node.js via C++ fournit une méthode simple et facile pour charger des images depuis des URLs dans des feuilles de calcul Excel. Cet article explique comment télécharger les données d'image dans un flux, puis l'insérer dans la feuille en utilisant l'API Aspose.Cells. Avec cette méthode, les images deviennent une partie intégrante du fichier Excel et ne sont pas téléchargées à chaque ouverture de la feuille de calcul.  

## Code d'exemple  

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
Il peut y avoir des cas où vous souhaitez toujours avoir l'image mise à jour depuis une URL. Pour ce faire, vous pouvez suivre les instructions données dans l'article [Insérer une image liée depuis une adresse Web](/cells/fr/nodejs-cpp/insert-a-linked-picture-from-web-address/). En suivant cette méthode, l'image est chargée depuis l'URL à chaque ouverture de la feuille.  
{{% /alert %}}  


