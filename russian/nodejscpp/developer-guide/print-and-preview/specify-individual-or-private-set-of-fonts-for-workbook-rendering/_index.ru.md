---  
title: Укажите отдельный или приватный набор шрифтов для рендеринга книги с помощью Node.js через C++  
linktitle: Указание индивидуального или частного набора шрифтов для рендеринга книги  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Узнайте, как указывать отдельные или приватные наборы шрифтов для рендеринга книги с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

 Обычно вы указываете директорию шрифтов или список шрифтов для всех книг, но иногда необходимо указывать индивидуальные или приватные наборы шрифтов для ваших книг. Aspose.Cells for Node.js via C++ предоставляет класс [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs), который можно использовать для указания отдельных или приватных наборов шрифтов для вашей книги.  

## **Указание индивидуального или частного набора шрифтов для рендеринга книги**  

 Следующий пример загружает [пример файла Excel](67338268.xlsx) с его индивидуальным или приватным набором шрифтов, указанных с помощью класса [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). Ознакомьтесь с [шрифтом](67338271.zip), используемым внутри кода, а также с [выходным PDF](67338269.pdf), сгенерированным этим кодом. Следующий скриншот показывает, как выглядит итоговый PDF, если шрифт найден успешно.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
