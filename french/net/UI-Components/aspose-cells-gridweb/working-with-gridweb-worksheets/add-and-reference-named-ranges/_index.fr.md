---
title: Ajouter et référencer des plages nommées
type: docs
weight: 120
url: /fr/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: Cet article présente comment travailler avec les plages nommées dans GridWeb. 
---

{{% alert color="primary" %}} 

Normalement, les libellés de colonnes et de lignes sont utilisés pour faire référence de manière unique aux cellules. Mais vous pouvez créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot **Nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Par exemple, utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, comme Ventes!C20:C30. Les étiquettes peuvent être utilisées dans des formules qui font référence à des données dans la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. Les **plages nommées** sont l'une des fonctionnalités les plus puissantes de Microsoft Excel. Les utilisateurs peuvent attribuer un nom à une plage et utiliser ce nom dans des formules. Aspose.Cells.GridWeb prend en charge cette fonctionnalité.

{{% /alert %}} 
## **Ajout/Référence de plages nommées dans des formules**
Le contrôle GridWeb fournit deux classes (GridName et GridNameCollection) pour travailler avec les plages nommées. Le fragment de code suivant vous aidera à comprendre comment créer la plage nommée et y accéder dans les formules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
