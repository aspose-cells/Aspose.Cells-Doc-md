---
title: Comment imprimer Excel en pages adaptées en largeur et en hauteur
type: docs
weight: 200
url: /fr/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Cet article vous montre un code expliquant comment définir FitToPagesWide et FitToPagesTall avec la bibliothèque Aspose.Cells.
keywords: C# Comment définir FitToPagesWide et FitToPagesTall, Comment ajouter FitToPagesWide et FitToPagesTall en C#, Comment définir FitToPagesWide et FitToPagesTall dans Excel, Comment effacer FitToPagesWide et FitToPagesTall dans Excel, Comment imprimer Excel comme pages ajustées en largeur et en hauteur, Comment imprimer la feuille de calcul en une seule page, Comment imprimer toutes les colonnes d une feuille de calcul sur une seule page.
---

## **Introduction**

Les réglages FitToPagesWide et FitToPagesTall sont utilisés dans les applications de tableur (comme Microsoft Excel) pour contrôler la mise à l'échelle d'une feuille lors de l'impression. Ces réglages aident à s'assurer que votre sortie imprimée rentre dans un nombre spécifié de pages, horizontalement et verticalement. Voici une explication de chaque réglage :

1. FitToPagesWide : Ce réglage spécifie le nombre de pages en largeur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesWide à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule largeur de page, peu importe la largeur de la feuille.
1. FitToPagesTall : Ce réglage spécifie le nombre de pages en hauteur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesTall à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule hauteur de page, indépendamment du nombre de lignes.

## **Pourquoi utiliser FitToPagesWide et FitToPagesTall**
Voici quelques raisons de définir FitToPagesWide et FitToPagesTall :
1. Contrôle de la mise en page imprimée : En spécifiant le nombre de pages en largeur et en hauteur, vous pouvez vous assurer que votre document imprimé est facile à lire et bien organisé, sans que des colonnes ou lignes soient mal réparties sur plusieurs pages.
1. Cohérence : Si vous imprimez plusieurs feuilles ou rapports, l'utilisation de ces réglages aide à maintenir un format cohérent, facilitant la comparaison et l'analyse des documents imprimés.
1. Présentation professionnelle : La mise à l'échelle et l'ajustement du contenu dans un nombre spécifié de pages peuvent donner une présentation plus professionnelle et soignée de vos données.

## **Comment imprimer un fichier en pages adaptées en largeur et en hauteur dans Excel**

Pour définir les paramètres FitToPagesWide et FitToPagesTall dans Microsoft Excel, suivez ces étapes :

1. Ouvrez votre classeur Excel et allez à la feuille que vous souhaitez imprimer.
1. Allez à l'onglet Mise en page dans le ruban.
1. Dans le groupe Mise en page, cliquez sur la petite flèche en bas à droite pour ouvrir la boîte de dialogue Mise en page.
1. Dans la boîte de dialogue Mise en page, allez à l'onglet Page.
1. Sous Échelle, sélectionnez l'option "Adapter à" puis indiquez le nombre de pages en largeur et en hauteur que vous souhaitez : Entrez le nombre de pages en largeur dans la première case (Adapter à x pages de large). Entrez le nombre de pages en hauteur dans la seconde case (Adapter à y pages de haut).
<br>
<img src="2.png" width=60% />

1. Cliquez sur OK pour appliquer les paramètres.


## **Comment imprimer Excel en pages adaptées en largeur et en hauteur en utilisant Aspose.Cells**

Pour définir FitToPagesWide et FitToPagesTall dans une feuille de calcul spécifique : d'abord, charger le [fichier exemple](input.xlsx), puis modifier les propriétés [**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/) et [**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) pour la feuille souhaitée. Voici un exemple en C# :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

Le résultat en sortie :
<br>
<img src="1.png" width=60% />


## **Comment imprimer une feuille de calcul en une seule page en utilisant Aspose.Cells**

Pour imprimer la feuille de calcul en une seule page : d'abord, charger le [fichier exemple](sample.xlsx), puis définir la propriété [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/). Voici un exemple en C# :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

Le résultat en sortie :
<br>
<img src="3.png" width=60% />


## **Comment imprimer toutes les colonnes d'une feuille de calcul en une seule page en utilisant Aspose.Cells**

Pour imprimer toutes les colonnes de la feuille de calcul sur une seule page : d'abord, charger le [fichier exemple](sample.xlsx), puis définir la propriété [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/). Voici un exemple en C# :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

Le résultat en sortie :
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
