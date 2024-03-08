---
title: Comment filtrer les blancs ou les non-vides
type: docs
weight: 85
url: /fr/net/how-to-filter-blanks-and-non-blanks/
description: Apprenez à filtrer les blancs et les non-vides en utilisant le Aspose.Cells for .NET API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Scénarios d'utilisation possibles**
Le filtrage des données dans Excel est un outil précieux qui améliore l'analyse, l'exploration et la présentation des données en permettant aux utilisateurs de se concentrer sur des sous-ensembles spécifiques de données en fonction de leurs critères, rendant ainsi le processus global de manipulation et d'interprétation des données plus efficace et efficient.

##  **Comment filtrer les blancs ou les non-vides dans Excel**
Dans Excel, vous pouvez facilement filtrer les blancs ou les non-vides à l'aide des options de filtrage. Voici comment procéder :

###  **Comment filtrer les blancs dans Excel**
1. Sélectionnez la plage : cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage dans laquelle vous souhaitez filtrer les blancs.
1. Ouvrez le menu Filtre : accédez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : cliquez sur le bouton "Filtre". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les blancs : cliquez sur la flèche de filtre dans la colonne dans laquelle vous souhaitez filtrer les blancs. Désélectionnez toutes les options sauf « Vides » et cliquez sur OK. Cela affichera uniquement les cellules vides de cette colonne.
<br>
<image src="2.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="3.png" width="70%" />

###  **Comment filtrer les non-vides dans Excel**
1. Sélectionnez la plage : cliquez sur la lettre de l'en-tête de colonne pour sélectionner la colonne entière ou sélectionnez la plage dans laquelle vous souhaitez filtrer les non-vides.
1. Ouvrez le menu Filtre : accédez à l'onglet "Données" dans le ruban.
<br>
<image src="1.png" width="70%" />
1. Options de filtre : cliquez sur le bouton "Filtre". Cela ajoutera des flèches de filtre à la plage sélectionnée.
1. Filtrer les non-vides : cliquez sur la flèche de filtre dans la colonne dans laquelle vous souhaitez filtrer les non-vides. Désélectionnez toutes les options sauf « Non-vides » ou « Personnalisé » et définissez les conditions en conséquence. Cliquez sur OK. Cela affichera uniquement les cellules qui ne sont pas vides dans cette colonne.
<br>
<image src="4.png" width="70%" />
1. Le résultat est le suivant :
<br>
<image src="5.png" width="70%" />

##  **Comment filtrer les blancs à l'aide du Aspose.Cells**
 Si une colonne contient du texte de telle sorte que peu de cellules sont vides et qu'un filtre est requis pour sélectionner les lignes uniquement où des cellules vides sont présentes,[AutoFilter.MatchBlanks (int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) et[AutoFilter.AddFilter (int fieldIndex, critères de chaîne)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) les fonctions peuvent être utilisées comme démontré ci-dessous.

 Veuillez consulter l'exemple de code suivant qui charge le[exemple de fichier Excel](sample.xlsx) qui contient des données factices. L'exemple de code utilise trois méthodes pour filtrer les blancs. Il enregistre ensuite le classeur sous[sortie du fichier Excel](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Comment filtrer les non-vides à l'aide de Aspose.Cells**

 Veuillez consulter l'exemple de code suivant qui charge le[exemple de fichier Excel](sample.xlsx)qui contient des données factices. Après avoir chargé le fichier, appelez le[AutoFilter.MatchNonBlanks (int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) fonction pour filtrer les données non vides, et enfin enregistrer le classeur sous[sortie du fichier Excel](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

