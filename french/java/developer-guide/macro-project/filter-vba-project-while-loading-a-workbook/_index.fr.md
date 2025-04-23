---
title: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 70
url: /fr/java/filter-vba-project-while-loading-a-workbook/
---

## **Scénarios d'utilisation possibles**
Certains fichiers .xlsm/.xslb ont un très grand nombre de macros (ou des macros très, très longues). Aspose.Cells chargera inconditionnellement ces métadonnées lors de l'ouverture de tels classeurs. Vous pouvez avoir besoin de contrôler cela avec les LoadDataFilterOptions, lorsque vous avez vraiment seulement besoin d'extraire les noms de feuille pour un grand nombre de classeurs, en sautant ainsi un tel contenu inutile. Ce filtre est fourni en introduisant la nouvelle option LoadDataFilterOptions.VBA.
## **Code d'exemple**
Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA soit filtré. Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé depuis le lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Définir les options de chargement, nous ne voulons pas charger le VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Créer un objet classeur à partir du fichier Excel d'exemple en utilisant les options de chargement
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Enregistrer la sortie au format pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
{{< app/cells/assistant language="java" >}}
