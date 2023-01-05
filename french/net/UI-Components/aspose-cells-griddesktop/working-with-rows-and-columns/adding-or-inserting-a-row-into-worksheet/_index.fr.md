---
title: Ajouter ou insérer une ligne dans la feuille de calcul
type: docs
weight: 30
url: /fr/net/adding-or-inserting-a-row-into-worksheet/
---
{{% alert color="primary" %}} 

Semblable à l'une de nos rubriques précédentes, cette rubrique décrit la fonctionnalité d'ajout et d'insertion de lignes dans les feuilles de calcul lors de l'exécution à l'aide du API de Aspose.Cells.GridDesktop. La différence fondamentale entre l'ajout et l'insertion est qu'en outre, une ligne est ajoutée à la fin de la collection de lignes de la feuille de calcul où, comme dans l'insertion, une ligne peut être ajoutée à n'importe quelle position spécifiée dans la feuille de calcul.

{{% /alert %}} 
## **Ajouter une ligne à la feuille de calcul**
Pour ajouter une nouvelle ligne à la feuille de calcul, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Ligne** au**Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}
## **Insertion d'une ligne dans la feuille de calcul**
Pour insérer une nouvelle ligne dans la feuille de calcul à une position spécifiée, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Insérer**Ligne** dans**Feuille de travail**(à une position précise en précisant l'index de la ligne où l'insérer)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.

sheet.Cells.InsertRow(0);

{{< /highlight >}}
