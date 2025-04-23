---
title: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des fichiers de feuille de calcul. Il prend en charge le paramétrage des polices de thème pour les en têtes et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l apparence et le style du document. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème pour les en têtes et le corps dans les documents Excel.
keywords: Aspose.Cells, Document Excel, En tête, Corps, Police de thème, Apparence, Style
type: docs
weight: 120
url: /fr/net/headings-and-body-theme-font/
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
Avec Aspose.Cells pour .Net, nous pouvons vérifier si la police par défaut est une police de thème ou définir une police de thème avec la propriété [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/).

Le code d'exemple suivant montre comment manipuler la police de thème.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Obtient dynamiquement la police de thème locale de manière programmée**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la propriété [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
{{< app/cells/assistant language="csharp" >}}
