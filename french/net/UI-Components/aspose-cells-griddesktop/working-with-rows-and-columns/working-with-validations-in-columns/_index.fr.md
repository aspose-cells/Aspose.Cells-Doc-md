---
title: Travailler avec des validations dans les colonnes
type: docs
weight: 80
url: /fr/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop,validation,validations
description: Cet article présente comment utiliser les validations dans les colonnes dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans l'un de nos sujets précédents, nous avons discuté des validations mais c'était dans le contexte des [Validations dans les feuilles de calcul](/cells/fr/net/working-with-validations-in-worksheets/) (pour avoir des informations générales sur la validation et les modes de validation, les développeurs peuvent se référer à ce sujet). Dans ce sujet, nous expliquerons les validations par rapport aux colonnes. En utilisant cette fonctionnalité, il est possible pour les développeurs d'appliquer une règle de validation sur n'importe quelle colonne de la feuille de calcul. Discutons-en en détail.

{{% /alert %}} 
## **Ajout de validation de colonne**
Pour ajouter n'importe quel type de validation à une colonne, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- **Ajoutez** une **Validation** souhaitée à n'importe quelle colonne

**IMPORTANT :** Pour plus d'informations sur les types de validation (ou modes de validation comme **Validation requise**, **Validation par expressions régulières** et **Validation personnalisée**) et la mise en oeuvre de la **Validation personnalisée**, veuillez vous référer à [Travailler avec les validations dans les feuilles de calcul.](/cells/fr/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accéder à la validation de colonne**
Pour accéder à une validation de colonne spécifique, veuillez suivre les étapes ci-dessous :

- Accéder à une **Feuille de calcul** souhaitée
- Accéder à une validation de colonne spécifique dans la **Feuille de calcul**
- Modifier les attributs de la **Validation**, si désiré



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Suppression de la validation de colonne**
Pour supprimer une validation de colonne spécifique de la feuille de calcul, veuillez suivre les étapes ci-dessous :

- Accéder à une **Feuille de calcul** souhaitée
- Supprimer une validation de colonne spécifique de la **Feuille de calcul**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
