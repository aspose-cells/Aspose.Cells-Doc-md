---
title: Personnalisez les paramètres de globalisation pour le tableau croisé dynamique avec Golang via C++
linktitle: Personnaliser les paramètres de globalisation pour la table croisée dynamique
type: docs
weight: 50
url: /fr/go-cpp/customize-globalization-settings-for-pivot-table/
description: Apprenez comment personnaliser les paramètres de mondialisation du tableau croisé dynamique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

 Parfois, vous souhaitez personnaliser le texte *Total Pivot, Sous-total, Total général, Tous les éléments, plusieurs éléments, Étiquettes de colonne, Étiquettes de ligne, Valeurs vides* selon vos besoins. Aspose.Cells for C++ vous permet de personnaliser les paramètres de mondialisation du tableau croisé dynamique pour gérer de tels scénarios. Vous pouvez également utiliser cette fonctionnalité pour changer les étiquettes dans d'autres langues comme l'arabe, l'hindi, le polonais, etc.

## **Personnaliser les paramètres de globalisation pour le tableau croisé dynamique**

Le code d'exemple ci-dessous explique comment personnaliser les paramètres de mondialisation pour le tableau croisé dynamique en C++. Il crée une classe *CustomPivotTableGlobalizationSettings* dérivée de la classe de base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) et surcharge toutes les méthodes nécessaires. Ces méthodes renvoient du texte personnalisé pour divers éléments du tableau croisé dynamique. Le code assigne ensuite cette mise en œuvre à la propriété [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). L'exemple charge un [fichier Excel source](40468488.xlsx), actualise les données du tableau croisé dynamique, et l'enregistre sous forme de [PDF de sortie](40468487.pdf). La capture d'écran ci-dessous montre des étiquettes personnalisées dans la sortie.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
