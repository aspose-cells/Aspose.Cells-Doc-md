---
title: Personnalisation de l XML du ruban avec Node.js via C++
linktitle: Personnaliser le menu Excel
type: docs
weight: 1500
url: /fr/nodejs-cpp/customizing-the-ribbon-xml/
description: Apprenez à personnaliser l XML du ruban dans Excel en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Office a remplacé les menus et les barres d'outils par un ruban en haut de la fenêtre de l'application depuis Office 2007. Le ruban est personnalisable. 
Aspose.Cells for Node.js via C++ vous permet de

- Conserver Ribbon XML sans l'analyser,
- Lire et écrire Ribbon XML sans l'analyser,
- Obtenir et définir les données de Ribbon XML.

Si vous souhaitez modifier le Ribbon XML, vous devez l'analyser avec un analyseur XML ou un autre outil Ribbon XML.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
