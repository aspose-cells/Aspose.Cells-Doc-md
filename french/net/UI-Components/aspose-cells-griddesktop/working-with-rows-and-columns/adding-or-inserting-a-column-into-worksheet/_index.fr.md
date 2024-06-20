---
title: Ajout ou insertion d une colonne dans la feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,insertion,ajout,colonne,insérer colonne,insérer ligne
description: Cet article présente comment insérer ou ajouter une colonne dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans ce sujet, nous décrirons la fonctionnalité de base pour ajouter et insérer des colonnes dans les feuilles de calcul au moment de l'exécution à l'aide de l'API de Aspose.Cells.GridDesktop. La différence fondamentale entre l'ajout et l'insertion est que dans l'ajout, une colonne est ajoutée à la fin de la collection des colonnes de la feuille de calcul, tandis que dans l'insertion, une colonne peut être ajoutée à n'importe quelle position spécifiée dans la feuille de calcul.

{{% /alert %}} 
## **Ajout d'une colonne à la feuille de calcul**
Pour ajouter une nouvelle colonne à la feuille de calcul, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajouter une **Colonne** à la **Feuille de calcul**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Insertion d'une colonne dans la feuille de calcul**
Pour insérer une nouvelle colonne dans la feuille de calcul à une position spécifiée, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Insérer une **Colonne** dans la **Feuille de calcul** (à une position spécifique en spécifiant l'indice de la colonne où l'insérer)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
