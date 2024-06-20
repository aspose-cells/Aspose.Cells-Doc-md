---
title: Modifier un style existant
type: docs
weight: 50
url: /fr/java/modify-an-existing-style/
description: Apprenez comment changer les styles dans Excel avec Microsoft Excel et avec l API Aspose.Cells for Java.
keywords: modifier un style existant excel, modifier un style existant excel java, modifier un style existant excel, modifier un style existant excel java, changer un style existant dans excel, changer un style existant dans excel java, comment changer de style dans excel, comment changer de style dans excel avec java, comment changer de style dans excel avec java, comment changer de style dans excel en utilisant java, changer un style existant dans excel java, changer un style existant dans excel
---

{{% alert color="primary" %}}

Pour appliquer les mêmes options de formatage aux cellules, créez un nouvel objet de style de formatage. Un objet de style de formatage est une combinaison de caractéristiques de formatage, telles que la police, la taille de la police, l'indentation, le nombre, le bord, les motifs, etc., nommées et stockées comme un ensemble. Lorsqu'appliqué, tout le formatage de ce style est appliqué.

Vous pouvez également utiliser un style existant, le sauvegarder avec le classeur et l'utiliser pour formater des informations avec les mêmes attributs.

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

Aspose.Cells fournit la méthode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) pour mettre à jour un style existant.

Pour changer un style nommé, qu'il soit créé dynamiquement avec Aspose.Cells ou prédéfini, appelez la méthode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) pour refléter les modifications apportées au style appliqué à une cellule ou une plage.

La méthode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) se comporte comme le bouton **OK** dans la boîte de dialogue Style : après avoir apporté des modifications à un style existant, appelez pour appliquer le changement. Si vous avez déjà appliqué un style à une plage de cellules, modifiez les attributs du style et appelez la méthode, la mise en forme de ces cellules est automatiquement mise à jour

### **Créer et modifier un style**

Cet exemple crée un objet de style, l'applique à une plage de cellules et modifie l'objet de style. Les modifications sont automatiquement appliquées à la cellule et à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modification d'un style existant**

Cet exemple utilise un fichier Excel de modèle simple dans lequel un style appelé Pourcentage a déjà été appliqué à une plage. L'exemple :

1. obtient le style,
1. crée un objet de style et
1. modifie le format du style.

Les modifications sont automatiquement appliquées à la plage à laquelle le style a été appliqué.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
