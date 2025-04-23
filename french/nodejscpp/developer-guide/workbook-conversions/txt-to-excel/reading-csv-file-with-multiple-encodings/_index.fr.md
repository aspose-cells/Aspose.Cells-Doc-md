---
title: Lecture d’un fichier CSV avec plusieurs encodages en utilisant Node.js via C++
linktitle: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Apprenez comment lire des fichiers CSV avec plusieurs encodages en utilisant Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple PDF ou XLSX.

{{% /alert %}}

Aspose.Cells fournit la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--), que vous devez définir à **true** pour charger correctement votre fichier CSV avec plusieurs encodages.

La capture d'écran suivante montre un exemple de fichier CSV contenant deux lignes. La première ligne est en encodage **ANSI** et la deuxième ligne est en encodage **Unicode**

|**Fichier d'entrée**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus sans définir la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) à **true**. Comme vous pouvez le voir, le texte Unicode n'a pas été converti correctement.

|**Fichier de sortie 1: aucune adaptation pour plusieurs encodages**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus après avoir défini la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) à **true**. Comme vous pouvez le voir, le texte Unicode est maintenant converti correctement.

|**Fichier de sortie 2: IsMultiEncoded est défini sur true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ci-dessous se trouve le code d'exemple qui convertit le fichier CSV ci-dessus en format XLSX correctement.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Articles Connexes

- [Ouverture des fichiers CSV](/cells/fr/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
