---  
title: Caricare un immagine da URL in un foglio di calcolo Excel con Node.js tramite C++  
linktitle: Carica un immagine web da un URL in un foglio di calcolo di Excel  
type: docs  
weight: 30  
url: /it/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Come convertire un immagine da URL in un’immagine Excel reale usando Aspose.Cells for Node.js via C++.  
keywords: excel mostra immagine da url, excel url a immagine, mostra immagine in excel da url, excel inserisci immagine da url, converti url in immagine in excel, excel immagine da url, carica immagine da url in excel, Node.js, Excel  
---  

## Caricare un'immagine da un URL in un foglio di lavoro di Excel  

Aspose.Cells for Node.js via C++ fornisce un modo semplice e facile per caricare immagini da URL nei fogli di lavoro Excel. Questo articolo spiega come scaricare i dati dell'immagine in un flusso e poi inserirli nel foglio usando l’API di Aspose.Cells. Con questo metodo, le immagini diventano parte del file Excel e non vengono scaricate ogni volta che si apre il foglio di lavoro.  

## Codice di esempio  

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
Potrebbero esserci casi in cui si desidera sempre l'immagine aggiornata da un URL. Per raggiungere questo obiettivo, puoi seguire le istruzioni fornite nell’articolo [Inserisci un'immagine collegata da indirizzo web](/cells/it/nodejs-cpp/insert-a-linked-picture-from-web-address/). Seguendo questa metodologia, l’immagine viene caricata dall’URL ogni volta che si apre il foglio di lavoro.  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
