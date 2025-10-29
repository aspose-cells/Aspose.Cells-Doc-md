---
title: Filtrer le projet VBA lors du chargement d un classeur
type: docs
weight: 140
url: /fr/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrer le projet VBA lors du chargement d'un classeur Excel en Python**

Certains fichiers .xlsm/.xslb contiennent un nombre extrêmement élevé de macros (ou des macros très longues). Aspose.Cells pour Python via .NET chargera inconditionnellement ces données (métadonnées) lors de l'ouverture de tels classeurs. Vous pouvez nécessiter un contrôle via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) lorsque vous avez simplement besoin d'extraire les noms des feuilles pour un grand nombre de classeurs, en ignorant ainsi le contenu non nécessaire. Ce filtre est fourni en introduisant une nouvelle option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **Code d'exemple**

Le code d'exemple suivant charge un classeur de telle sorte que seul le VBA est filtré. Un fichier exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
