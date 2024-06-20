---
title: Ajout ou insertion d une ligne dans la feuille de calcul
type: docs
weight: 30
url: /fr/net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/
keywords: GridDesktop,insert,add,row,insert row,add row
description: Cet article présente comment ajouter ou insérer une ligne dans GridDesktop.
---

{{% alert color="primary" %}} 

Similaire à l'un de nos sujets précédents, ce sujet décrit la fonctionnalité d'ajout et d'insertion de lignes dans les feuilles de calcul au moment de l'exécution à l'aide de l'API de Aspose.Cells.GridDesktop. La différence fondamentale entre l'ajout et l'insertion est que dans l'ajout, une ligne est ajoutée à la fin de la collection des lignes de la feuille de calcul, tandis que dans l'insertion, une ligne peut être ajoutée à n'importe quelle position spécifiée dans la feuille de calcul.

{{% /alert %}} 
## **Ajout d'une ligne à la feuille de calcul**
Pour ajouter une nouvelle ligne à la feuille de calcul, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajouter une **Ligne** à la **Feuille de calcul**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Insérer une ligne dans la Feuille de calcul**
Pour insérer une nouvelle ligne dans la feuille de calcul à un emplacement spécifié, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Insérer une **Ligne** dans la **Feuille de calcul** (à une position spécifique en spécifiant l'index de la ligne où l'insérer)

{{< highlight java >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
