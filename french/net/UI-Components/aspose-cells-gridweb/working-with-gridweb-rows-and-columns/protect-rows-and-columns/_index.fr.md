---
title: Protéger les lignes et les colonnes
type: docs
weight: 60
url: /fr/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,protéger
description: Cet article présente comment protéger les lignes et les colonnes dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet discute de quelques techniques pour protéger les cellules dans les lignes et les colonnes contre toute action des utilisateurs finaux. Les développeurs peuvent mettre en œuvre cette protection en utilisant deux techniques : en rendant les cellules dans les lignes et les colonnes en lecture seule, ou en restreignant les options du menu contextuel d'Aspose.Cells.GridWeb. Les deux techniques sont discutées ci-dessous à l'aide d'exemples.

{{% /alert %}} 
## **Protéger les cellules dans les lignes et les colonnes**
### **Rendre les lignes et les colonnes en lecture seule**
Une façon de protéger les lignes et les colonnes dans une feuille de calcul est de rendre les cellules en lecture seule. Ainsi, elles ne peuvent pas être supprimées par les utilisateurs finaux.

Pour rendre les lignes et les colonnes en lecture seule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accédez à GridWorksheet dans la collection.
1. Définissez vos cellules désirées dans les lignes ou les colonnes en lecture seule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Restreindre les options du menu contextuel**
Aspose.Cells.GridWeb fournit un menu contextuel que les utilisateurs finaux peuvent utiliser pour effectuer des opérations sur le contrôle. Le menu propose de nombreuses options de manipulation des cellules, des lignes et des colonnes.

**Options contextuelles complètes** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Il est possible de restreindre tout type d'opérations côté client sur les lignes et les colonnes en limitant les options disponibles dans le menu contextuel. Cela peut être fait en définissant les propriétés EnableClientColumnOperations et EnableClientRowOperations du contrôle GridWeb à false. Il est également possible de restreindre les utilisateurs à geler les lignes et les colonnes en définissant la propriété EnableClientFreeze du contrôle GridWeb à false.

**Menu contextuel après avoir restreint les options de ligne et de colonne** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
