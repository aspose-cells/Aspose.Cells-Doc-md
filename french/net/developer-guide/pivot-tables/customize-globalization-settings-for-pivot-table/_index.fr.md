---
title: Personnaliser les paramètres de globalisation pour le tableau croisé dynamique
type: docs
weight: 50
url: /fr/net/customize-globalization-settings-for-pivot-table/
---
##  **Scénarios d'utilisation possibles**

 Parfois, vous souhaitez personnaliser le*Total croisé, sous-total, total général, tous les éléments, éléments multiples, étiquettes de colonnes, étiquettes de lignes, valeurs vides*texte selon vos besoins. Aspose.Cells vous permet de personnaliser les paramètres de globalisation du tableau croisé dynamique pour faire face à de tels scénarios. Vous pouvez également utiliser cette fonctionnalité pour modifier les étiquettes dans d'autres langues comme l'arabe, l'hindi, le polonais, etc.

##  **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

L'exemple de code suivant explique comment personnaliser les paramètres de globalisation pour le tableau croisé dynamique. Cela crée une classe*CustomPivotTableGlobalizationSettings* dérivé d'une classe de base[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)et remplace toutes ses méthodes nécessaires. Ces méthodes renvoient le texte personnalisé pour le *Total pivot, le sous-total, le total général, tous les éléments, plusieurs éléments, les étiquettes de colonne, les étiquettes de ligne, les valeurs vides*. Ensuite, il attribue l'objet de cette classe à[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) propriété. Le code charge le[fichier Excel source](40468488.xlsx) qui contient le tableau croisé dynamique, actualise et calcule ses données et les enregistre sous[sortie PDF](40468487.pdf) déposer. La capture d'écran suivante montre l'effet de l'exemple de code sur la sortie PDF. Comme vous pouvez le voir sur la capture d'écran, différentes parties du tableau croisé dynamique ont désormais un texte personnalisé renvoyé par les méthodes remplacées de[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)classe.

![tâche : image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
