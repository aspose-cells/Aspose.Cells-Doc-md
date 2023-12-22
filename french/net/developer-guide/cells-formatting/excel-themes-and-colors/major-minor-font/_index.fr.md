---
title: Titres et police du thème du corps
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul. Il prend en charge la définition des polices de thème de titre et de corps dans les documents Excel, permettant aux utilisateurs de personnaliser l'apparence et le style du document. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème de titre et de corps dans les documents Excel.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /fr/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 La police par défaut changera automatiquement lorsque le paramètre de regoin est modifié.

Si la police par défaut est modifiée, la hauteur des lignes et la largeur des colonnes sont également modifiées, et cela peut même gâcher la mise en page.

Qu’est-ce qui a causé le changement de la police par défaut ?

Si la police du thème Excel est définie, Excel basculera automatiquement entre les différentes polices en fonction de l'environnement linguistique actuel.


{{% /alert %}}

##  **Titres et police du thème du corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur la liste déroulante des polices, vous verrez "Polices thématiques" avec deux polices thématiques : Calibri Light (Titres) et Calibri (Corps) en haut avec réglage de la région anglaise.

**![Polices du thème](Theme-Fonts.png)**

Si la police du thème est sélectionnée, le nom de la police s'affichera différemment selon les régions.
Si vous ne souhaitez pas que la police soit automatiquement modifiée dans différentes régions, ne sélectionnez pas les deux polices thématiques.


##  **Modification des titres et de la police du corps par programme**
 Avec Aspose.Cells pour .Net, nous pouvons vérifier si la police par défaut est la police du thème ou définir la police du thème avec[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) propriété.

L'exemple de code suivant montre comment manipuler la police du thème.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Obtient dynamiquement la police du thème local par programme**
Parfois, nos serveurs et les machines des utilisateurs ne se trouvent pas dans la même région. Comment pouvons-nous obtenir la même police que celle souhaitée par les utilisateurs pour le traitement des fichiers ?

 Nous devons définir les paramètres régionaux du système avant de charger le fichier avec[**LoadOptions.Région**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) propriété

L’exemple de code suivant montre comment obtenir la police du thème local.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}