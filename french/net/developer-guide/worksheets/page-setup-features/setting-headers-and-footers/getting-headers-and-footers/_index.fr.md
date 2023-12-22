---
title: Obtenir des en-têtes ou des pieds de page
type: docs
weight: 30
url: /fr/net/get-headers-or-footers/
description: Cet article explique comment obtenir par programme l'en-tête et les pieds de page à partir de fichiers Excel ou OpenOffice à l'aide de la bibliothèque C# API ou .NET.
---
{{% alert color="primary" %}}

 Les en-têtes et les pieds de page s'affichent uniquement en mode Mise en page, Aperçu avant impression et sur les pages imprimées.

 Vous pouvez également utiliser la boîte de dialogue Mise en page si vous souhaitez afficher les en-têtes ou les pieds de page de plusieurs feuilles de calcul à la fois.

Pour les autres types de feuilles, tels que les feuilles de graphiques ou les graphiques, vous pouvez insérer des en-têtes et des pieds de page uniquement à l'aide de la boîte de dialogue Mise en page.

{{% /alert %}}

##  **Obtenir des en-têtes et des pieds de page dans MS Excel**
1. Cliquez sur la feuille de calcul dans laquelle vous souhaitez afficher ou modifier les en-têtes ou les pieds de page.
2. Sous l'onglet Vie, dans le groupe Vues du classeur, cliquez sur Mise en page.
Excel affiche la feuille de calcul en mode Mise en page.
3. Pour afficher ou modifier un en-tête ou un pied de page, cliquez sur la zone de texte d'en-tête ou de pied de page gauche, centrale ou droite en haut ou en bas de la page de la feuille de calcul (sous En-tête ou au-dessus du pied de page).


##  **Obtenir des en-têtes et des pieds de page à l'aide de Aspose.Cells pour .Net**
 Avec[**Feuille de calcul.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) et[**Feuille de calcul.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) méthodes, le développeur .Net peut simplement obtenir les en-têtes ou les pieds de page du fichier.

1. Construisez Workbook pour ouvrir le fichier.
2. Obtient la feuille de calcul dans laquelle vous souhaitez obtenir les en-têtes ou les pieds de page.
3. Obtient l'en-tête ou le pied de page avec un identifiant de section spécifique.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Analyser les en-têtes et pieds de page dans la liste de commandes**
Le texte d'en-tête ou de pied de page peut contenir des commandes spéciales, par exemple un espace réservé pour le numéro de page, la date actuelle ou les attributs de formatage du texte.

Les commandes spéciales sont représentées par une seule lettre précédée d'une esperluette ("&").

Les chaînes d'en-tête et de pied de page sont construites à l'aide de la grammaire ABNF. Ce n'est pas facile à comprendre sans spectateur.

 Aspose.Cells pour .Net fournit[**Feuille de calcul.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)méthode pour analyser les en-têtes et les pieds de page en tant que liste de commandes.

Les codes suivants expliquent comment analyser l'en-tête ou le pied de page en tant que liste de commandes et traiter les commandes :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
