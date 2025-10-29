---
title: Police de thème pour les titres et le corps avec Golang via C++
linktitle: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableur. Elle supporte la définition des polices de thème pour les titres et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l apparence et le style du document. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème pour les titres et le corps dans les documents Excel.
keywords: Aspose.Cells, Document Excel, En tête, Corps, Police de thème, Apparence, Style
type: docs
weight: 120
url: /fr/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La police par défaut changera automatiquement lorsque le paramètre régionale est modifié.

Si la police par défaut est modifiée, la hauteur de la ligne et la largeur de la colonne seront également modifiées, et cela pourrait même perturber la mise en page.

Qu'est-ce qui a causé le changement de la police par défaut?

Si la police de thème Excel est définie, Excel basculera automatiquement entre différentes polices en fonction de l'environnement linguistique actuel.

{{% /alert %}}

## **Polices de thème pour les en-têtes et le corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur la liste déroulante de police, vous verrez "Polices de thème" avec deux polices de thème : Calibri Light (Titres) et Calibri (Corps) en haut avec le paramètre régional en anglais.

**![Polices de thème](Theme-Fonts.png)**

Si la police de thème est sélectionnée, le nom de la police s'affichera différemment selon les régions.
Si vous ne souhaitez pas que la police soit automatiquement modifiée dans différentes régions, ne sélectionnez pas les deux polices de thème.

## **Modifier la police des titres et du corps de manière programmée**
Avec Aspose.Cells for C++, nous pouvons vérifier si la police par défaut est une police de thème ou définir la police de thème avec la propriété [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/).

Le code d'exemple suivant montre comment manipuler la police de thème.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **Récupération dynamique de la police de thème locale de manière programmatique**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la propriété [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
