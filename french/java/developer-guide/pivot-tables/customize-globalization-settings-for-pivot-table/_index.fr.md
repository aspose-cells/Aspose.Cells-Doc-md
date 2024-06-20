---
title: Personnaliser les paramètres de globalisation pour la table croisée dynamique
type: docs
weight: 20
url: /fr/java/customize-globalization-settings-for-pivot-table/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez personnaliser le *Total des éléments de la table, le Sous-total, le grand total, tous les éléments, plusieurs éléments, étiquettes de colonnes, étiquettes de lignes, valeurs vides* selon vos besoins. Aspose.Cells vous permet de personnaliser les paramètres de globalisation de la table croisée dynamique pour traiter de tels scénarios. Vous pouvez également utiliser cette fonctionnalité pour changer les libellés dans d'autres langues comme l'arabe, l'hindi, le polonais, etc.

## **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

Le code d'exemple suivant explique comment personnaliser les paramètres de globalisation pour la table croisée dynamique. Il crée une classe *CustomPivotTableGlobalizationSettings* dérivée d'une classe de base [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) et remplace toutes ses méthodes nécessaires. Ces méthodes renvoient le texte personnalisé pour le *Total des éléments de la table, Sous-total, Grand total, Tous les éléments, plusieurs éléments, étiquettes de colonnes, étiquettes de lignes, valeurs vides*. Ensuite, il attribue l'objet de cette classe à la propriété [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings). Le code charge le [fichier excel source](40468491.xlsx) qui contient la table croisée dynamique, rafraîchit et calcule ses données et l'enregistre sous forme de [fichier PDF de sortie](40468490.pdf). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier PDF de sortie. Comme vous pouvez le voir sur la capture d'écran, différentes parties de la table croisée dynamique ont maintenant un texte personnalisé renvoyé par les méthodes remplacées de la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
