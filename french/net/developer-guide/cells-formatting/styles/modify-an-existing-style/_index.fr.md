---
title: Modifier un style existant
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuilles de calcul qui permet aux utilisateurs de modifier les styles de cellules existants. Cet article présentera comment modifier un style de cellule existant avec la bibliothèque Aspose.Cells afin que les utilisateurs puissent changer l apparence des cellules selon leurs besoins.
keywords: Modifier les styles existants, personnaliser l apparence de votre application, guides, tutoriels, documentation d aide, documentation de développement, références API, code d exemple, téléchargements, support.
type: docs
weight: 90
url: /fr/net/modify-an-existing-style/
---

{{% alert color="primary" %}}

Pour appliquer les mêmes options de formatage aux cellules, créez un nouvel objet de style de formatage. Un objet de style de formatage est une combinaison de caractéristiques de formatage, telles que la police, la taille de police, l'indentation, le nombre, la bordure, les motifs, etc., nommés et stockés en tant qu'ensemble. Lorsqu'ils sont appliqués, tous les formatages de ce style sont appliqués.

Vous pouvez également utiliser un style existant, l'enregistrer avec le classeur et l'utiliser pour formater des informations avec les mêmes attributs.

Lorsque les cellules ne sont pas explicitement formatées, le style **Normal** (le style par défaut du classeur) est appliqué. Microsoft Excel prédéfinit plusieurs styles en plus du style Normal, y compris Virgule, Monétaire et Pourcentage.

Aspose.Cells permet de modifier n'importe lequel de ces styles ou tout autre style que vous définissez avec les attributs souhaités.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour mettre à jour un style dans Microsoft Excel 97-2003 :

1. Sur le menu **Format**, cliquez sur **Style**.
1. Sélectionnez le style que vous souhaitez modifier dans la liste **Nom du style**.
1. Cliquez sur **Modifier**.
1. Sélectionnez les options de style que vous souhaitez en utilisant les onglets dans la boîte de dialogue Format de cellule.
1. Cliquez sur **OK**.
1. Sous **Le style inclut**, spécifiez les fonctionnalités de style que vous souhaitez.
1. Cliquez sur **OK** pour enregistrer le style et l'appliquer à la plage sélectionnée.

## **Utilisation d'Aspose.Cells**

Les exemples suivants illustrent comment utiliser la méthode [**Style.Update**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update).

### **Créer et modifier un style**

Cet exemple crée un objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style), l'applique à une plage de cellules et modifie l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Les modifications sont automatiquement appliquées à la cellule et à la plage sur laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modification d'un style existant**

Cet exemple utilise un fichier Excel de modèle simple dans lequel un style appelé Pourcentage a déjà été appliqué à une plage. L'exemple :

1. obtient le style,
1. crée un objet de style et
1. modifie le format du style.

Les modifications sont automatiquement appliquées à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
