---
title: Police de thème pour les en têtes et le corps
linktitle: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de feuille de calcul. Elle supporte la définition des polices de thème pour l en tête et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l apparence et le style du document. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème d en tête et de corps dans les documents Excel.
keywords: Aspose.Cells, Document Excel, En tête, Corps, Police de thème, Apparence, Style, Node.js via C++
type: docs
weight: 120
url: /fr/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La police par défaut changera automatiquement lorsque le paramètre régionale est modifié.

Si la police par défaut est modifiée, la hauteur de la ligne et la largeur de la colonne seront également modifiées, et cela pourrait même perturber la mise en page.

Qu'est-ce qui a causé le changement de la police par défaut?

Si la police de thème Excel est définie, Excel basculera automatiquement entre différentes polices en fonction de l'environnement linguistique actuel.

{{% /alert %}}

## **Polices de thème pour les en-têtes et le corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur le menu déroulant de la police, vous verrez « Polices de thème » avec deux polices de thème : Calibri Light (En-têtes) et Calibri (Corps) en haut avec le paramètre régional en anglais.

**![Polices de thème](Theme-Fonts.png)**

Si la police de thème est sélectionnée, le nom de la police s'affichera différemment selon les régions. Si vous ne souhaitez pas que la police change automatiquement en fonction des régions, ne sélectionnez pas les deux polices de thème.

## **Modifier la police des titres et du corps de manière programmée**
Avec Aspose.Cells for Node.js via C++, nous pouvons vérifier si la police par défaut est une police de thème ou définir la police de thème avec la méthode [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-).

Le code exemple suivant montre comment manipuler la police de thème.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Récupération dynamique de la police de thème locale de manière programmatique**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la méthode [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
