---
title: Obtenir des avertissements lors du chargement du fichier Excel avec Node.js via C++
linktitle: Obtenir des avertissements lors du chargement du fichier Excel
type: docs
weight: 110
url: /fr/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Découvrez comment capturer les avertissements lors du chargement d’un fichier Excel avec Aspose.Cells for Node.js via C++. Gérer efficacement les classeurs corrompus mais chargeables.
---

## **Scénarios d'utilisation possibles**

Parfois, l’utilisateur tente de charger un classeur qui est quelque peu corrompu mais pouvant être chargé. Dans ce cas, Aspose.Cells génère des avertissements lors du chargement du classeur. Ces avertissements peuvent être interceptés en implémentant l’interface [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) et en configurant la propriété [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--).

## **Obtenir des avertissements lors du chargement d'un fichier Excel**

Le code d’exemple suivant explique comment obtenir des avertissements lors du chargement d’un fichier Excel. Le code charge le [fichier Excel d’exemple](sampleDuplicateDefinedName.xlsx) qui affiche un avertissement [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) lors du chargement. Cet avertissement est ensuite capturé par la méthode [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) qui affiche les messages d’avertissement sur la console. Ensuite, le code enregistre le classeur sous le nom [fichier Excel de sortie](outputDuplicateDefinedName.xlsx). Si vous ouvrez le fichier Excel dans Microsoft Excel, ce dernier affichera également cet avertissement comme montré dans cette capture d’écran. Veuillez également vérifier la sortie de la console pour mieux comprendre.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Sortie console**

Voici la sortie de la console du code ci-dessus lors de son exécution avec le [fichier Excel d'exemple fourni](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
