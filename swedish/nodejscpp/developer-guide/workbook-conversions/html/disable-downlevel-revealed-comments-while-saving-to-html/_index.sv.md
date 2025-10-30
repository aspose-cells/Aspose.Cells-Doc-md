---
title: Inaktivera Downlevel Revealed Comments vid sparande till HTML med Node.js via C++
linktitle: Inaktivera kommentarer med låg nivå som upptäcks medan du sparar till HTML
type: docs
weight: 20
url: /sv/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Lär dig hur du inaktiverar Downlevel Revealed Comments när du sparar en Excel fil till HTML med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, visar Aspose.Cells Downlevel Conditional Comments. Dessa villkorade kommentarer är mest relevanta för äldre versioner av Internet Explorer och är ointressanta för moderna webbläsare. Du kan läsa mer i detalj på länken.

- [Villkorlig kommentar - Låg nivå - avslöjad villkorlig kommentar](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ låter dig eliminera dessa Downlevel Revealed Comments genom att ställa in [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--)-egenskapen till **true**.

## **Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML**

Följande kodexempel visar användningen av [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på true. Vänligen ladda ner [exempel-Excelfilen](50528257.xlsx) som används i detta kodexempel och [utdata HTML](50528258.zip) som genererats, som referens.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
