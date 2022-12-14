---
title: Utilisation de plages nommées
type: docs
weight: 110
url: /fr/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalement, vous utilisez les étiquettes des colonnes et des lignes d'une feuille de calcul pour faire référence aux cellules de ces colonnes et lignes. Mais vous pouvez créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot**Nom**peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Par exemple, utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, telles que Ventes!C20:C30 pour représenter une cellule, une plage de cellules, une formule ou une valeur constante. Les étiquettes peuvent être utilisées dans des formules faisant référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom.**Plages nommées** sont parmi les fonctionnalités les plus puissantes de Microsoft. Les utilisateurs peuvent attribuer un nom à une plage nommée afin que cette plage de cellules puisse être référencée avec son nom dans les formules.**Aspose.Cells.GridDesktop** prend en charge cette fonctionnalité.

{{% /alert %}} 
## **Ajout/référencement de plages nommées dans les formules**
Le contrôle GridDesktop prend en charge l'importation/exportation de plages nommées dans les fichiers Excel, il fournit deux classes (**Nom** et**NameCollection**) pour travailler avec des plages nommées.

L'extrait de code suivant vous aidera à les utiliser.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
