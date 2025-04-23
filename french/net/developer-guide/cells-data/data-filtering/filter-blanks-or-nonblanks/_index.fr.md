---
title: Comment filtrer les cellules vides ou non vides
type: docs
weight: 85
url: /fr/net/how-to-filter-blanks-and-non-blanks/
description: Apprenez à filtrer les cellules vides et non vides en utilisant l API Aspose.Cells for .NET.
keywords: Filtrer les cellules vides, Filtrer les cellules non vides, Filtrer les cellules vides dans la feuille de calcul, Filtrer les cellules non vides dans la feuille de calcul, Filtrer les cellules vides dans Excel, Filtrer les cellules non vides dans Excel, Filtrer les cellules vides et non vides dans Excel
---

## **Scénarios d'utilisation possibles**
Filtrer les données dans Excel est un outil précieux qui améliore l'analyse, l'exploration et la présentation des données en permettant aux utilisateurs de se concentrer sur des sous-ensembles spécifiques de données en fonction de leurs critères, rendant ainsi le processus global de manipulation et d'interprétation des données plus efficace et plus efficace.

## **Comment filtrer les cellules vides ou non vides dans Excel**
Dans Excel, vous pouvez facilement filtrer les cellules vides ou non vides en utilisant les options de filtrage. Voici comment vous pouvez le faire :

### **Comment filtrer les cellules vides dans Excel**
1. Sélectionnez la plage : Cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage où vous souhaitez filtrer les cellules vides.
1. Ouvrez le menu Filtre : Allez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : Cliquez sur le bouton "Filtrer". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les cellules vides : Cliquez sur la flèche de filtrage dans la colonne que vous souhaitez filtrer les cellules vides. Désélectionnez toutes les options sauf « Vides » et cliquez sur OK. Cela affichera uniquement les cellules vides de cette colonne.
<br>
<image src="2.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="3.png" width="70%" />

### **Comment filtrer les cellules non vides dans Excel**
1. Sélectionnez la plage : Cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage où vous souhaitez filtrer les cellules non vides.
1. Ouvrez le menu Filtre : Allez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : Cliquez sur le bouton "Filtrer". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les cellules non vides : Cliquez sur la flèche de filtre dans la colonne que vous souhaitez filtrer pour les cellules non vides. Désélectionnez toutes les options sauf "Non vides" ou "Personnalisé" et définissez les conditions en conséquence. Cliquez sur OK. Cela affichera uniquement les cellules qui ne sont pas vides dans cette colonne.
<br>
<image src="4.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="5.png" width="70%" />

## **Comment filtrer les cellules vides à l'aide d'Aspose.Cells**
Si une colonne contient du texte de telle sorte que quelques cellules sont vides, et qu'un filtre est nécessaire pour sélectionner uniquement les lignes où des cellules vides sont présentes, les fonctions [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) et [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) peuvent être utilisées comme démontré ci-dessous. 

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](sample.xlsx) contenant certaines données fictives. Le code d'exemple utilise trois méthodes pour filtrer les cellules vides. Ensuite, il enregistre le classeur sous forme de [fichier Excel de sortie](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **Comment filtrer les cellules non vides à l'aide d'Aspose.Cells**

Veuillez consulter le code d'exemple suivant qui charge le [fichier Excel d'exemple](sample.xlsx) contenant certaines données fictives. Après avoir chargé le fichier, appelez la fonction [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) pour filtrer les données non vides, puis enregistrez le classeur sous forme de [fichier Excel de sortie](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

{{< app/cells/assistant language="csharp" >}}
