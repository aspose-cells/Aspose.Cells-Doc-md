---
title: Filtrer le projet VBA lors du chargement d'un classeur
type: docs
weight: 70
url: /fr/java/filter-vba-project-while-loading-a-workbook/
---
## **Scénarios d'utilisation possibles**
Certains fichiers .xlsm/.xslb contiennent une très grande quantité de macros (ou des macros très, très longues). Aspose.Cells chargera inconditionnellement ces (méta) données lors de l'ouverture de ces classeurs. Vous devrez peut-être contrôler cela via LoadDataFilterOptions, alors que vous n'avez vraiment besoin que d'extraire les noms de feuille pour un grand nombre de classeurs, sautant ainsi ce contenu inutile. Ce filtre est fourni en introduisant une nouvelle option LoadDataFilterOptions.VBA.
## **Exemple de code**
L'exemple de code suivant charge un classeur de sorte que seul VBA soit filtré. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Définissez les options de chargement, nous ne voulons pas charger VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(nouveau LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Créer un objet de classeur à partir d'un exemple de fichier Excel à l'aide des options de chargement
Livre de classeur = nouveau classeur (srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Enregistrer la sortie au format pdf
livre.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
