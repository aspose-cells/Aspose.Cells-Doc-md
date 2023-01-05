---
title: Utilisation des validations dans les colonnes
type: docs
weight: 80
url: /fr/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 Dans l'un de nos sujets précédents, nous avons discuté des validations, mais c'était dans le contexte de[Validations dans les feuilles de travail](/cells/fr/net/working-with-validations-in-worksheets/) (pour avoir des informations générales sur la validation et les modes de validation, les développeurs peuvent se référer à cette rubrique). Dans cette rubrique, nous expliquerons les validations par rapport aux colonnes. Grâce à cette fonctionnalité, il est possible pour les développeurs d'appliquer une règle de validation sur n'importe quelle colonne de la feuille de calcul. Discutons-en en détail.

{{% /alert %}} 
## **Ajout d'une validation de colonne**
Pour ajouter tout type de validation à une colonne, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
- **Ajouter** un désir**Validation** à n'importe quelle colonne

**IMPORTANT:**Pour plus d'informations sur les types de validation (ou les modes de validation comme**Est une validation requise**, **Validation des expressions régulières** et**Validation personnalisée** ) et la mise en œuvre**Validation personnalisée** , prière de se référer à[Utilisation des validations dans les feuilles de calcul.](/cells/fr/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Accéder à la validation des colonnes**
Pour accéder à une validation de colonne spécifique, veuillez suivre les étapes ci-dessous :

-  Accéder à un**Feuille de travail**
-  Accéder à une colonne spécifique**Validation** dans le**Feuille de travail**
-  Éditer**Validation** attributs, si désiré



{{< highlight "csharp" >}}

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
Pour supprimer une validation de colonne spécifique de la feuille de calcul, veuillez suivre les étapes ci-dessous :

-  Accéder à un**Feuille de travail**
-  Supprimer une colonne spécifique**Validation** du**Feuille de travail**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
