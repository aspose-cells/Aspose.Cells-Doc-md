---
title: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul. Elle supporte la définition des polices de thème pour l en tête et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l apparence et le style du document. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour travailler avec les polices de thème pour l en tête et le corps dans les documents Excel.
keywords: Aspose.Cells pour Python via .NET, Document Excel, En tête, Corps, Police de Thème, Apparence, Style
type: docs
weight: 120
url: /fr/python-net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La police par défaut changera automatiquement lorsque les paramètres régionaux sont modifiés. 

Si la police par défaut est modifiée, la hauteur de la ligne et la largeur de la colonne seront également modifiées, et cela pourrait même perturber la mise en page.

Qu'est-ce qui a causé le changement de la police par défaut?

Si la police de thème Excel est définie, Excel basculera automatiquement entre différentes polices en fonction de l'environnement linguistique actuel.


{{% /alert %}}

## **Polices de thème pour les en-têtes et le corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur la liste déroulante de la police, vous verrez "Polices de thème" avec deux polices de thème : Calibri Léger (En-têtes) et Calibri (Corps) en haut avec les paramètres régionaux en anglais.

**![Polices de thème](Theme-Fonts.png)**

Si la police de thème est sélectionnée, le nom de la police s'affichera différemment dans différentes régions.
Si vous ne souhaitez pas que la police change automatiquement dans différentes régions, ne sélectionnez pas les deux polices de thème.


## **Changer la police pour les en-têtes et le corps de manière programmée**
Avec Aspose.Cells pour Python via .NET, nous pouvons vérifier si la police par défaut est une police de thème ou définir une police de thème avec la propriété [**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type).

Le code d'exemple suivant montre comment manipuler la police de thème.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Headings-and-body-font.py" >}}


## **Obtient dynamiquement la police de thème locale de manière programmée**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la propriété [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Local-Theme-Font.py" >}}

