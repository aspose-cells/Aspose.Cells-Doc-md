---  
title: Laden eines Webbildes von einer URL in ein Excel Arbeitsblatt mit Node.js über C++  
linktitle: Ein Webbild von einer URL in ein Excel Arbeitsblatt laden  
type: docs  
weight: 30  
url: /de/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: So konvertieren Sie ein Bild von einer URL in ein echtes Excel Bild mithilfe von Aspose.Cells for Node.js via C++.  
keywords: excel zeigt bild von url, excel url zu bild, bild in excel von url anzeigen, excel bild von url einfügen, url in bild in excel umwandeln, excel bild von url, bild aus url in excel laden, Node.js, Excel  
---  

## Laden eines Bildes von einer URL in ein Excel-Arbeitsblatt  

Aspose.Cells for Node.js via C++ bietet eine einfache und bequeme Möglichkeit, Bilder von URLs in Excel-Tabellen zu laden. Dieser Artikel erklärt, wie man die Bilddaten in einen Stream lädt und dann mit der Aspose.Cells API in die Tabelle einfügt. Mit dieser Methode werden die Bilder Teil der Excel-Datei und werden beim Öffnen der Tabelle nicht erneut heruntergeladen.  

## Beispielcode  

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
Es kann Fälle geben, in denen Sie stets das aktualisierte Bild von einer URL möchten. Um dies zu erreichen, können Sie den Anweisungen im Artikel [Ein verknüpftes Bild aus Webadresse einfügen](/cells/de/nodejs-cpp/insert-a-linked-picture-from-web-address/) folgen. Mit dieser Methode wird das Bild jedes Mal geladen, wenn die Tabelle geöffnet wird.  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
