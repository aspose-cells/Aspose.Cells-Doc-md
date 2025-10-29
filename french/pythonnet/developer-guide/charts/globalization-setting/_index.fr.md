---
title: Convertir un graphique en image localisée avec Python via .NET
linktitle: Définir la région localisée
type: docs
weight: 50
url: /fr/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Découvrez comment définir des configurations de mondialisation pour les graphiques en utilisant Aspose.Cells pour Python via .NET. Configurez les graphiques pour prendre en charge plusieurs langues et formats régionaux afin d afficher correctement le texte, les dates et les nombres.
keywords: Aspose.Cells pour Python via .NET, Graphiques, Paramètres de mondialisation, Plusieurs langues, Formats régionaux, Affichage, Texte, Dates, Nombres.
---

{{% alert color="primary" %}}

Dans ce sujet, nous vous montrerons comment convertir un graphique en une image localisée et comment définir la région localisée pour un graphique.

{{% /alert %}}

## **Scénario**

Quand pourriez-vous avoir besoin de définir la région localisée pour un graphique ?

Si vous ouvrez un fichier XLSX contenant un graphique dans Excel avec les paramètres régionaux espagnols, des éléments tels que le titre du graphique et la légende apparaissent en espagnol. Cependant, en enregistrant ce graphique en tant qu'image avec Aspose.Cells, ces éléments peuvent rester en anglais par défaut :

**![Problème global](GlobalIssue.png)**

Cela se produit parce que la légende du graphique dans l'image de sortie ne correspond pas à la localisation d'Excel. Vous pouvez résoudre ce problème en configurant les paramètres de région localisée du graphique.

## **Éléments supportés**

Les éléments suivants du graphique seront rendus conformément à vos paramètres de localisation :

| **Éléments supportés**      | **Valeur par défaut (Anglais)**       |
|-----------------------------|-----------------------------------|
| Nom du titre de l'axe         | Titre de l’axe                      |
| Nom de l'unité d'axe          | Centaines, Milliers...               |
| Nom du titre du graphique     | Titre du graphique                  |
| Nom de l'augmentation de la légende | Augmentation                      |
| Nom de la diminution de la légende | Diminution                      |
| Nom du total de la légende   | Total                              |
| Autre nom                     | Autre                             |
| Nom de la série               | Série                            |

{{< app/cells/assistant language="python-net" >}}
