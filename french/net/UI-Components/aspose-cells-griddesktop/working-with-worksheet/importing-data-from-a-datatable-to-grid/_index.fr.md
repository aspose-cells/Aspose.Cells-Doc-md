---
title: Importer des données à partir d un DataTable dans une grille
type: docs
weight: 50
url: /fr/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,importer,données,datatable
description: Cet article présente comment importer des données dans GridDesktop.
---

{{% alert color="primary" %}} 

Depuis la sortie du .NET Framework, Microsoft a fourni un excellent moyen de stocker des données en mode hors ligne sous forme d'objet DataTable. Comprendre les besoins des développeurs, Aspose.Cells.GridDesktop prend également en charge l'importation de données à partir d'un tableau de données. Ce sujet discute de la manière de le faire.

{{% /alert %}} 
## **Exemple**
Pour importer le contenu d'un tableau de données à l'aide du contrôle Aspose.Cells.GridDesktop :

1. Ajouter le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Créer un objet DataTable contenant les données à importer.
1. Obtenez la référence d'une feuille de calcul souhaitée.
1. Importer le contenu du tableau de données dans la feuille de travail.
1. Définir les en-têtes de colonne de la feuille de travail selon les noms de colonne du tableau de données.
1. Définir la largeur des colonnes, si nécessaire.
1. Afficher la feuille de travail.

Dans l'exemple ci-dessous, nous avons créé un objet DataTable et l'avons rempli avec des données extraites d'une table de base de données nommée Produits. Enfin, nous avons importé les données de cet objet DataTable dans une feuille de travail souhaitée à l'aide de Aspose.Cells.GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
