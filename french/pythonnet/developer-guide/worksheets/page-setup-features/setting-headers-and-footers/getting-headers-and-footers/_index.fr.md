---
title: Obtenir les en têtes ou pieds de page
type: docs
weight: 30
url: /fr/python-net/get-headers-or-footers/
description: Cet article explique comment obtenir de manière programmatique les en têtes et pieds de page à partir de fichiers Excel ou OpenOffice en utilisant l API Aspose.Cells for Python via .NET.
keywords: Bibliothèque Excel Python, obtenir les en têtes et pieds de page en Python, analyser les en têtes et pieds de page en liste de commandes à l aide de Python.
---

{{% alert color="primary" %}}

Les en-têtes et pieds de page ne s'affichent qu'en mode Mise en page, Aperçu avant impression et sur les pages imprimées. 

Vous pouvez également utiliser la boîte de dialogue Mise en page si vous souhaitez afficher les en-têtes ou pieds de page pour plus d'une feuille de calcul à la fois. 

Pour d'autres types de feuilles, tels que les feuilles de graphique ou les graphiques, vous pouvez insérer des en-têtes et pieds de page uniquement en utilisant la boîte de dialogue Mise en page.

{{% /alert %}}

## **Comment obtenir les en-têtes et pieds de page dans MS Excel**
1. Cliquez sur la feuille de calcul où vous souhaitez afficher ou modifier les en-têtes ou les pieds de page.
2. Dans l'onglet Affichage, dans le groupe Affichages de classeur, cliquez sur Mise en page.
  Excel affiche la feuille de calcul en mode Mise en page.
3. Pour afficher ou modifier un en-tête ou un pied de page, cliquez sur la zone de texte de l'en-tête ou du pied de page de gauche, du centre ou de droite en haut ou en bas de la page de la feuille de calcul (sous En-tête ou au-dessus de Pied de page).


## **Comment obtenir les en-têtes et pieds de page avec la bibliothèque Excel Aspose.Cells for Python**
Avec les méthodes [**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int) et [**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int), le développeur .Net peut simplement obtenir des en-têtes ou des pieds de page à partir du fichier.

1. Construisez un classeur pour ouvrir le fichier.
2. Obtenez la feuille de calcul où vous souhaitez obtenir les en-têtes ou les pieds de page.
3. Obtenez l'en-tête ou le pied de page avec un identifiant de section spécifique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **Comment analyser les en-têtes et pieds de page en liste de commandes**
Le texte de l'en-tête ou du pied de page peut contenir des commandes spéciales, par exemple un espace réservé pour le numéro de page, la date actuelle ou des attributs de formatage de texte.

Les commandes spéciales sont représentées par une seule lettre avec un esperluette en tête ("&").

Les chaînes d'en-tête et de pied de page sont construites en utilisant la grammaire ABNF. Ce n'est pas facile à comprendre sans visionneuse .

Aspose.Cells for Python via .NET fournit la méthode [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str) pour analyser les en-têtes et pieds de page en tant que liste de commandes.

Le code suivant montre comment analyser l'en-tête ou le pied de page en tant que liste de commandes et traiter les commandes :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
{{< app/cells/assistant language="python-net" >}}
