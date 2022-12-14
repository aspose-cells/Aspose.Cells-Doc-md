---
title: Modifier un style existant
type: docs
weight: 50
url: /fr/java/modify-an-existing-style/
description: Apprenez à changer les styles dans Excel avec Microsoft Excel et avec Aspose.Cells for Java API.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Pour appliquer les mêmes options de mise en forme aux cellules, créez un nouvel objet de style de mise en forme. Un objet de style de mise en forme est une combinaison de caractéristiques de mise en forme, telles que la police, la taille de la police, l'indentation, le nombre, la bordure, les motifs, etc., nommées et stockées sous forme d'ensemble. Lorsqu'il est appliqué, toutes les mises en forme de ce style sont appliquées.

Vous pouvez également utiliser un style existant, l'enregistrer avec le classeur et l'utiliser pour mettre en forme des informations avec les mêmes attributs.

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

 Aspose.Cells fournit le[**Style.mise à jour**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) méthode de mise à jour d'un style existant.

 Pour modifier un style nommé, qu'il soit créé dynamiquement à l'aide de Aspose.Cells ou prédéfini, appelez le[**Style.mise à jour**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) pour refléter tout changement de style appliqué à une cellule ou à une plage.

 La[**Style.mise à jour**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) se comporte comme la méthode**D'ACCORD** bouton dans la boîte de dialogue Style : après avoir apporté des modifications à un style existant, appelez pour implémenter la modification. Si vous avez déjà appliqué un style à une plage de cellules, modifiez les attributs de style et appelez la méthode, la mise en forme de ces cellules est automatiquement mise à jour

### **Création et modification d'un style**

Cet exemple crée un objet de style, l'applique à une plage de cellules et modifie l'objet de style. Les modifications sont automatiquement appliquées à la cellule et à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modification d'un style existant**

Cet exemple utilise un fichier Excel de modèle simple dans lequel un style appelé Pourcentage a déjà été appliqué à une plage. L'exemple:

1. obtient le style,
1. crée un objet de style et
1. modifie la mise en forme du style.

Les modifications sont automatiquement appliquées à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
