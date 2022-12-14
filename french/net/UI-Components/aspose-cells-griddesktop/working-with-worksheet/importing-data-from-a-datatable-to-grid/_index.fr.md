---
title: Importation de données d'un DataTable vers Grid
type: docs
weight: 50
url: /fr/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

Depuis la sortie du framework .NET, Microsoft a fourni un excellent moyen de stocker des données en mode hors ligne sous la forme d'un objet DataTable. Comprenant les besoins des développeurs, Aspose.Cells.GridDesktop prend également en charge l'importation de données à partir d'une table de données. Cette rubrique explique comment procéder.

{{% /alert %}} 
## **Exemple**
Pour importer le contenu d'une table de données à l'aide du contrôle Aspose.Cells.GridDesktop :

1. Ajoutez le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Créez un objet DataTable qui contient les données à importer.
1. Obtenir la référence d'une feuille de calcul souhaitée.
1. Importez le contenu de la table de données dans la feuille de calcul.
1. Définissez les en-têtes de colonne de la feuille de calcul en fonction des noms de colonne de la table de données.
1. Définissez la largeur des colonnes, si vous le souhaitez/
1. Affichez la feuille de calcul.

Dans l'exemple ci-dessous, nous avons créé un objet DataTable et l'avons rempli avec des données extraites d'une table de base de données nommée Products. Enfin, nous avons importé des données de cet objet DataTable dans une feuille de calcul souhaitée à l'aide de Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
