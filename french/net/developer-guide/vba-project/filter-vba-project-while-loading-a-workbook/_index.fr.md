---
title: Filtrer le projet VBA lors du chargement d'un classeur
type: docs
weight: 140
url: /fr/net/filter-vba-project-while-loading-a-workbook/
---
## **Filtrer le projet VBA lors du chargement d'un classeur Excel dans C#**

Certains fichiers .xlsm/.xslb contiennent une très grande quantité de macros (ou des macros très, très longues). Aspose.Cells chargera inconditionnellement ces (méta) données lors de l'ouverture de ces classeurs. Vous devrez peut-être contrôler cela cependant[**LoadDataFilterOptionsLoadDataFilterOptionsLoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) lorsque vous n'avez vraiment besoin d'extraire que des noms de feuilles pour un grand nombre de classeurs, sautant ainsi ce contenu inutile. Ce filtre est fourni en introduisant une nouvelle option,[**LoadDataFilterOptions.VBALoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Exemple de code**

L'exemple de code suivant charge un classeur de sorte que seul VBA soit filtré. Un exemple de fichier pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
