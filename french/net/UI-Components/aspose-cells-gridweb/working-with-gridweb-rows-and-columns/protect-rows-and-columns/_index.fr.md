---
title: Protéger les lignes et les colonnes
type: docs
weight: 60
url: /fr/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

Cette rubrique présente quelques techniques de protection des cellules dans les lignes et les colonnes contre tout type d'action effectuée par les utilisateurs finaux. Les développeurs peuvent implémenter cette protection à l'aide de deux techniques : en rendant les cellules des lignes et des colonnes en lecture seule, ou en limitant les options du menu contextuel de Aspose.Cells.GridWeb. Ces deux techniques sont décrites ci-dessous à l'aide d'exemples.

{{% /alert %}} 
## **Protéger Cells dans les lignes et les colonnes**
### **Rendre les lignes et les colonnes en lecture seule**
Une façon de protéger les lignes et les colonnes d'une feuille de calcul consiste à rendre les cellules en lecture seule. Ensuite, ils ne peuvent pas être supprimés par les utilisateurs finaux.

Pour rendre les lignes et les colonnes en lecture seule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accédez à GridWorksheet dans la collection.
1. Définissez les cellules souhaitées dans les lignes ou les colonnes en lecture seule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Restreindre les options du menu contextuel**
Aspose.Cells.GridWeb fournit un menu contextuel que les utilisateurs finaux peuvent utiliser pour effectuer des opérations sur le contrôle. Le menu propose de nombreuses options pour manipuler les cellules, les lignes et les colonnes.

**Options contextuelles complètes** 

![tâche : image_autre_texte](protect-rows-and-columns_1.png)

Il est possible de restreindre tout type d'opérations côté client sur les lignes et les colonnes en limitant les options disponibles dans le menu contextuel. Cela peut être fait en définissant les propriétés EnableClientColumnOperations et EnableClientRowOperations du contrôle GridWeb sur false. Il est également possible d'empêcher les utilisateurs de geler des lignes et des colonnes en définissant la propriété EnableClientFreeze du contrôle GridWeb sur false.

**Menu contextuel après avoir restreint les options de ligne et de colonne** 

![tâche : image_autre_texte](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
