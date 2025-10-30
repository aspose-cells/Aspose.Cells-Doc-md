---  
title: Converti le date in date giapponesi con Node.js tramite C++  
linktitle: Convertire le date in date giapponesi  
type: docs  
weight: 350  
url: /it/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Impara come convertire le date Gregoriane in date giapponesi usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Nel calendario giapponese, una nuova era inizia con il regno di un nuovo imperatore. Il 1° maggio 2019 un nuovo imperatore è salito al potere, concludendo l'era Heisei e iniziando l'era Reiwa.  

{{% /alert %}}  

Aspose.Cells fornisce un metodo per convertire le date Gregoriane in date giapponesi. Durante questa conversione, vengono considerate anche le variazioni dell'epoca. Il seguente frammento di codice converte il file [Excel di origine](90112015.xlsx) contenente date Gregoriane in un [PDF di output](90112016.pdf) con date giapponesi come mostrato nell'immagine sotto.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
