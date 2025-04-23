---
title: Personnaliser les paramètres de globalisation pour la table croisée dynamique
type: docs
weight: 50
url: /fr/net/customize-globalization-settings-for-pivot-table/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez personnaliser le *Total des éléments de la table, le Sous-total, le grand total, tous les éléments, plusieurs éléments, étiquettes de colonnes, étiquettes de lignes, valeurs vides* selon vos besoins. Aspose.Cells vous permet de personnaliser les paramètres de globalisation de la table croisée dynamique pour traiter de tels scénarios. Vous pouvez également utiliser cette fonctionnalité pour changer les libellés dans d'autres langues comme l'arabe, l'hindi, le polonais, etc.

## **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

Le code d'exemple suivant explique comment personnaliser les paramètres de globalisation pour le tableau croisé dynamique. Il crée une classe *CustomPivotTableGlobalizationSettings* dérivée d'une classe de base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) et remplace toutes ses méthodes nécessaires. Ces méthodes renvoient le texte personnalisé pour les *Total des valeurs, Sous-total, Total général, Tous les éléments, Plusieurs éléments, Étiquettes de colonne, Étiquettes de ligne, Valeurs vides*. Ensuite, il affecte l'objet de cette classe à la propriété [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/). Le code charge le [fichier Excel source](40468488.xlsx) qui contient le tableau croisé dynamique, actualise et calcule ses données et le sauvegarde sous la forme d'un [fichier PDF de sortie](40468487.pdf). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier PDF de sortie. Comme vous pouvez le voir sur la capture d'écran, différentes parties du tableau croisé dynamique ont désormais un texte personnalisé renvoyé par les méthodes remplacées de la classe [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
