---
title: Enregistrer en ODF 1.1, 1.2 et 1.3 avec Node.js via C++
linktitle: Enregistrer un fichier ODS dans ODF 1.1, 1.2 et 1.3
description: Convertir Excel en spécifications ODF 1.1, 1.2 et 1.3 avec Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /fr/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la sauvegarde d'un fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF (**OpenDocument Format**) 1.1, 1.2 et 1.3. Aspose.Cells dispose de la propriété [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) qui spécifie la version ODF pour la sauvegarde des fichiers ODS. La valeur par défaut de cette propriété est [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), donc le fichier ODS enregistré sans cette configuration utilise la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1, 1.2 et 1.3. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
