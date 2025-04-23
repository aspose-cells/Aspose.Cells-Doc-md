---
title: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrer le projet VBA lors du chargement d'un classeur Excel en C#**

Certains fichiers .xlsm/.xslb comportent une quantité extrêmement importante de macros (ou des macros très longues). Aspose.Cells chargera inconditionnellement ces données (méta) lors de l'ouverture de tels classeurs. Vous pourriez avoir besoin de contrôler cela via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) lorsque vous avez vraiment besoin d'extraire les noms de feuilles pour un grand nombre de classeurs, en sautant ainsi ces contenus inutiles. Ce filtre est fourni en introduisant une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
