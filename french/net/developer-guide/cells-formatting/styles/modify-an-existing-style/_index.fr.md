---
title: Modifier un style existant
type: docs
weight: 90
url: /fr/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Pour appliquer les mêmes options de mise en forme aux cellules, créez un nouvel objet de style de mise en forme. Un objet de style de formatage est une combinaison de caractéristiques de formatage, telles que la police, la taille de la police, l'indentation, le nombre, la bordure, les motifs, etc., nommées et stockées sous forme d'ensemble. Lorsqu'il est appliqué, toutes les mises en forme de ce style sont appliquées.

Vous pouvez également utiliser un style existant, l'enregistrer avec le classeur et l'utiliser pour formater les informations avec les mêmes attributs.

 Lorsque les cellules ne sont pas explicitement formatées, le**Normal** style (le style par défaut du classeur) est appliqué. Microsoft Excel prédéfinit plusieurs styles en plus du style Normal, notamment Virgule, Devise et Pourcentage.

Aspose.Cells permet de modifier n'importe lequel de ces styles ou tout autre style que vous définissez avec les attributs souhaités.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour mettre à jour un style dans Microsoft Excel 97-2003 :

1.  Sur le**Format** menu, cliquez sur**Style**.
1.  Sélectionnez le style que vous souhaitez modifier dans le**Nom du style** liste.
1.  Cliquez sur**Modifier**.
1. Sélectionnez les options de style souhaitées à l'aide des onglets de la boîte de dialogue Format Cells.
1.  Cliquez sur**D'ACCORD**.
1.  En dessous de**Le style comprend**, spécifiez les fonctionnalités de style souhaitées.
1.  Cliquez sur**D'ACCORD** pour enregistrer le style et l'appliquer à la plage sélectionnée.

## **En utilisant Aspose.Cells**

 Les exemples suivants montrent comment utiliser[**Style.Mettre à jour**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)méthode.

### **Création et modification d'un style**

 Cet exemple crée un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet, l'applique à une plage de cellules et modifie[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet. Les modifications sont automatiquement appliquées à la cellule et à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modification d'un style existant**

Cet exemple utilise un fichier Excel de modèle simple dans lequel un style appelé Pourcentage a déjà été appliqué à une plage. L'exemple:

1. obtient le style,
1. crée un objet de style et
1. modifie la mise en forme du style.

Les modifications sont automatiquement appliquées à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
