---
title: Travailler avec des validations dans les feuilles de calcul
type: docs
weight: 70
url: /fr/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop, validations, validation
description: Cet article présente comment travailler avec la validation dans GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop prend également en charge l'ajout de validations (ou règles de validation) aux cellules d'une feuille de calcul. En appliquant des règles de validation aux cellules, les développeurs peuvent limiter les utilisateurs à saisir des données dans la grille dans un format spécifique. Différents modes de validation sont pris en charge par Aspose.Cells.GridDesktop. Dans ce sujet, nous ne discuterons pas seulement de ces modes de validation, mais nous expliquerons également la manipulation de ces validations.

{{% /alert %}} 
## **Modes de validation**
Il existe trois modes de validation pris en charge par Aspose.Cells.GridDesktop comme suit :

- Mode de Validation Requis
- Mode de Validation Expressions Régulières
- Mode de Validation Personnalisé
### **Mode de Validation Requis**
Dans ce mode de validation, les utilisateurs sont limités à entrer des valeurs dans des cellules spécifiées. Une fois que la **Validation Requise** est appliquée sur une cellule de la feuille de calcul, il devient obligatoire pour l'utilisateur d'entrer une valeur dans cette cellule.
### **Mode de Validation des Expressions Régulières**
Dans ce mode, des restrictions sont appliquées sur les cellules de la feuille de calcul pour que les utilisateurs soumettent des données dans un format spécifique. Le format des données est fourni sous forme d'une **Expression Régulière**.
### **Mode de Validation Personnalisée**
Pour utiliser la **Validation Personnalisée**, il est obligatoire pour les développeurs de mettre en œuvre l'interface Aspose.Cells.GridDesktop.ICustomValidation. L'interface fournit une méthode **Valider**. Cette méthode renvoie vrai si les données sont valides, sinon elle renvoie faux.
## **Travailler avec les Validations dans Aspose.Cells.GridDesktop**
### **Ajouter une Validation**
Pour ajouter n'importe quel type de validation à une cellule de la feuille de calcul, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajouter une validation souhaitée à la collection **Validations** de la **Feuille de calcul** pour spécifier quelle validation doit être appliquée sur quelle cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

Sur la figure ci-dessus, nous avons également mentionné les règles de validation devant les cellules auxquelles ces règles de validation sont appliquées. Si une valeur invalide (qui n'est pas valide selon la règle de validation définie pour cette cellule) est entrée, une **MessageBox** apparaîtrait pour informer l'utilisateur de l'entrée invalide.

{{% /alert %}} 
### **Implémentation de ICustomValidation**
Dans l'extrait de code ci-dessus, nous avons ajouté une validation personnalisée dans la cellule **A8** mais nous n'avons pas encore implémenté cette validation personnalisée. Comme nous l'avons expliqué au début de ce sujet, pour appliquer une validation personnalisée, nous devons mettre en œuvre l'interface **ICustomValidation**. Alors, essayons de créer une classe pour implémenter l'interface **ICustomValidation**.

Dans l'extrait de code ci-dessous, nous avons mis en œuvre une validation personnalisée pour effectuer les vérifications suivantes:

- Vérifier si l'adresse de la cellule est exacte dans laquelle la validation est ajoutée
- Vérifier si le type de données de la valeur de la cellule est double
- Vérifier si la valeur de la cellule est supérieure à 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accès à la Validation**
Une fois qu'une validation est ajoutée à une cellule spécifique de la feuille de calcul, il peut être nécessaire pour les développeurs d'accéder et de modifier les attributs d'une validation spécifique à l'exécution. Ainsi, Aspose.Cells.GridDesktop a rendu simple pour les développeurs d'accomplir cette tâche.

Pour accéder à une validation spécifique, veuillez suivre les étapes ci-dessous :

- Accéder à une **Feuille de calcul** souhaitée
- Accéder à une **Validation** spécifique dans la feuille de calcul en spécifiant le nom de la cellule sur laquelle la validation a été appliquée
- Modifier les attributs de la **Validation**, si désiré



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**La collection de validations** a deux indexeurs. Un indexeur (utilisé dans l'exemple ci-dessous) permet d'accéder à un objet de **validation** en prenant un nom de cellule comme index, tandis que l'autre indexeur prend deux paramètres (les numéros de ligne et de colonne) pour accomplir la même tâche.

{{% /alert %}} 
### **Supprimer la validation**
Pour supprimer une validation spécifique de la feuille de calcul, veuillez suivre les étapes ci-dessous :

- Accéder à une **Feuille de calcul** souhaitée
- Supprimer une **validation** spécifique de la **feuille de calcul** en spécifiant le nom de la cellule sur laquelle la validation a été appliquée



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
