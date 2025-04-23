---  
title: Ladda ett webbbild från en URL till ett Excel ark med Node.js via C++  
linktitle: Ladda en webbild från en URL till ett Excel kalkylblad  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Hur man konverterar en bild från URL till en faktisk Excel bild med Aspose.Cells for Node.js via C++.  
keywords: excel visa bild från url, excel url till bild, visa bild i excel från url, excel infoga bild från url, konvertera url till bild i excel, excel bild från url, ladda bild från url i excel, Node.js, Excel  
---  

## Ladda en bild från en URL till ett Excel-kalkylblad  

Aspose.Cells for Node.js via C++ ger ett enkelt och lätt sätt att ladda bilder från URL:er till Excel-ark. Denna artikel förklarar hur man laddar ner bilddata till en ström och sedan infogar den i kalkylbladet med Aspose.Cells API. Med denna metod blir bilder en del av Excel-filen och laddas inte ner varje gång kalkylbladet öppnas.  

## Exempelkod  

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
Det kan finnas fall där du alltid vill ha den uppdaterade bilden från en URL. För att göra detta kan du följa instruktionerna i artikeln [Infoga en länkad bild från webbadress](/cells/sv/nodejs-cpp/insert-a-linked-picture-from-web-address/). Genom att följa denna metod laddas bilden från URL:en varje gång kalkylbladet öppnas.  
{{% /alert %}}  


