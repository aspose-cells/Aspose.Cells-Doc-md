---
title: Ajustement automatique des lignes pour Cells fusionné
type: docs
weight: 120
url: /fr/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel propose une fonctionnalité qui vous permet de dimensionner automatiquement la hauteur d'une cellule en fonction de son contenu. Cette fonctionnalité est appelée ajustement automatique des lignes. Microsoft Excel ne définit pas nativement l’opération d’ajustement automatique sur les cellules fusionnées. Parfois, cette fonctionnalité devient vitale pour un utilisateur qui a réellement besoin d'implémenter également l'ajustement automatique des lignes sur les cellules fusionnées.

{{% /alert %}}

##  **Comment utiliser AutoFitMergedCellsType pour l'ajustement automatique des lignes**
 Aspose.Cells prend en charge cette fonctionnalité via le[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Grâce à ce API, il est possible d'ajuster automatiquement les lignes d'une feuille de calcul comprenant des cellules fusionnées. Voici une liste de tous les types possibles de cellules fusionnées à ajustement automatique :

- Aucun
- Première ligne
- Dernière ligne
- Chaque ligne

##  **Ajustement automatique des lignes pour Cells fusionné**

Veuillez consulter le code suivant, il crée un objet classeur et ajoute plusieurs feuilles de calcul. Utilisez différentes méthodes pour les opérations d’ajustement automatique dans chaque feuille de calcul. La capture d'écran montre les résultats après l'exécution de l'exemple de code.

<br>
<img src="result.png" width=80% />

##  **C# Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
