---
title: Utiliser les plages nommées
type: docs
weight: 110
url: /fr/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop,plages nommées,noms
description: Cet article présente les plages nommées dans GridDesktop.
---

{{% alert color="primary" %}} 

Normalement, vous utilisez les libellés des colonnes et des lignes sur une feuille de calcul pour faire référence aux cellules dans ces colonnes et lignes. Mais vous pouvez créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot **Nom** peut désigner une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Par exemple, Utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, telles que Ventes!C20:C30 pour représenter une cellule, une plage de cellules, une formule ou une valeur constante. Les libellés peuvent être utilisés dans des formules qui font référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. Les **Plages nommées** font partie des fonctionnalités les plus puissantes de Microsoft. Les utilisateurs peuvent attribuer un nom à une plage nommée afin que cette plage de cellules puisse être référencée par son nom dans les formules. **Aspose.Cells.GridDesktop** prend en charge cette fonctionnalité.

{{% /alert %}} 
## **Ajout/Référence de plages nommées dans des formules**
Le contrôle GridDesktop prend en charge l'importation/exportation des plages nommées dans les fichiers Excel, il fournit deux classes (**Nom** et **CollectionNom**) pour travailler avec les plages nommées.

Le code suivant vous aidera à comprendre comment les utiliser.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
