---
title: Ajouter ou insérer une colonne dans la feuille de calcul
type: docs
weight: 10
url: /fr/net/adding-or-inserting-a-column-into-worksheet/
---
{{% alert color="primary" %}} 

Dans cette rubrique, nous décrirons la fonctionnalité de base d'ajout et d'insertion de colonnes dans les feuilles de calcul lors de l'exécution à l'aide du API de Aspose.Cells.GridDesktop. La différence fondamentale entre l'addition et l'insertion est qu'en outre, la colonne est ajoutée à la fin de la collection de colonnes de la feuille de calcul où, comme dans l'insertion, la colonne peut être ajoutée à n'importe quelle position spécifiée dans la feuille de calcul.

{{% /alert %}} 
## **Ajouter une colonne à la feuille de calcul**
Pour ajouter une nouvelle colonne à la feuille de calcul, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Colonne** au**Feuille de travail**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Insertion d'une colonne dans la feuille de calcul**
Pour insérer une nouvelle colonne dans la feuille de calcul à une position spécifiée, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Insérer**Colonne** dans**Feuille de travail** (à une position précise en précisant l'index de la colonne où l'insérer)

{{< highlight "java" >}}

 // Accessing first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet to the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
