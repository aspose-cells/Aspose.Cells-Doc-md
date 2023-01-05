---
title: Utilisation des validations dans les feuilles de calcul
type: docs
weight: 70
url: /fr/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop prend également en charge l'ajout de validations (ou de règles de validation) aux cellules d'une feuille de calcul. En appliquant des règles de validation aux cellules, les développeurs peuvent empêcher les utilisateurs de saisir des données dans Grid dans un format spécifique. Différents modes de validations sont pris en charge par Aspose.Cells.GridDesktop. Dans cette rubrique, nous discuterons non seulement de ces modes de validation, mais expliquerons également la manipulation de ces validations.

{{% /alert %}} 
## **Modes de validation**
Il existe trois modes de validation pris en charge par Aspose.Cells.GridDesktop comme suit :

- Est requis Mode de validation
- Mode de validation des expressions régulières
- Mode de validation personnalisé
### **Est requis Mode de validation**
 Dans ce mode de validation, les utilisateurs sont limités à saisir des valeurs dans des cellules spécifiées. Une fois que**Est une validation requise** est appliqué sur une cellule de feuille de calcul, il devient indispensable pour un utilisateur d'entrer une valeur dans cette cellule.
### **Mode de validation des expressions régulières**
 Dans ce mode, des restrictions sont appliquées aux cellules de la feuille de calcul pour que les utilisateurs soumettent des données dans des cellules dans un format spécifique. Le modèle de format de données est fourni sous la forme d'un**Expression régulière**.
### **Mode de validation personnalisé**
 Utiliser**Validation personnalisée** , Il est indispensable que les développeurs implémentent l'interface Aspose.Cells.GridDesktop.ICustomValidation. L'interface fournit une**Valider** méthode. Cette méthode renvoie vrai si les données sont valides sinon renvoie faux.
## **Utilisation des validations dans Aspose.Cells.GridDesktop**
### **Ajouter une validation**
Pour ajouter tout type de validation à une cellule de feuille de calcul, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajoutez une validation souhaitée à la**Validations** collecte de la**Feuille de travail** pour préciser quelle validation serait appliquée sur quelle cellule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 Dans la figure ci-dessus, nous avons également mentionné les règles de validation devant les cellules où ces règles de validation sont appliquées. Si une valeur non valide (qui n'est pas valide selon la règle de validation définie pour cette cellule) est saisie, un**Messagerie** apparaîtrait pour informer l'utilisateur de l'entrée invalide.

{{% /alert %}} 
### **Implémentation de ICustomValidation**
 Dans l'extrait de code ci-dessus, nous avons ajouté une validation personnalisée dans**A8**cell mais nous n'avons pas encore implémenté cette validation personnalisée. Comme nous l'avons expliqué au début de ce sujet, pour appliquer la validation personnalisée, nous devons implémenter**ICustomValidation** interface. Essayons donc de créer une classe à implémenter**ICustomValidation** interface.

Dans l'extrait de code ci-dessous, nous avons implémenté une validation personnalisée pour effectuer les vérifications suivantes :

- Vérifiez si l'adresse de la cellule est exacte dans laquelle la validation est ajoutée
- Vérifiez si le type de données de la valeur de la cellule est double
- Vérifiez si la valeur de la cellule est supérieure à 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accéder à la validation**
Une fois qu'une validation est ajoutée à une cellule de feuille de calcul spécifique, les développeurs peuvent demander aux développeurs d'accéder et de modifier les attributs d'une validation spécifique au moment de l'exécution. Ainsi, Aspose.Cells.GridDesktop a simplifié la tâche des développeurs.

Pour accéder à une validation spécifique, veuillez suivre les étapes ci-dessous :

-  Accéder à un**Feuille de travail**
-  Accéder à un**Validation**dans la feuille de calcul en précisant le nom de la cellule sur laquelle la validation a été appliquée
-  Éditer**Validation** attributs, si désiré



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validations** collection a deux indexeurs. Un indexeur (qui est utilisé dans l'exemple ci-dessous) permet d'accéder à un**Validation** objet en prenant un nom de cellule comme index tandis que l'autre indexeur prend deux paramètres (c'est-à-dire les numéros de ligne et de colonne) pour effectuer la même tâche.

{{% /alert %}} 
### **Suppression de la validation**
Pour supprimer une validation spécifique de la feuille de calcul, veuillez suivre les étapes ci-dessous :

-  Accéder à un**Feuille de travail**
-  Supprimer un élément spécifique**Validation** du**Feuille de travail** en précisant le nom de la cellule sur laquelle la validation a été appliquée



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
