---
title: Ajouter Cell validations
type: docs
weight: 70
url: /fr/net/add-cell-validations/
---
{{% alert color="primary" %}} 

L'une des fonctionnalités avancées de Aspose.Cells.GridWeb consiste à ajouter des règles de validation d'entrée pour les cellules. Les développeurs peuvent créer différents types de règles de validation pour les cellules afin de contrôler et de valider les valeurs d'entrée. Cette rubrique décrit les types de validation pris en charge et comment les créer.

{{% /alert %}} 
## **Types de validation**
Trois types de validations peuvent être appliquées à l'aide de Aspose.Cells.GridWeb :

- Validation de la liste.
- Validation de la liste déroulante.
- Validation des expressions personnalisées.

Chacun est discuté en détail ci-dessous.
### **Validation de liste**
La validation de liste permet aux utilisateurs de fournir une entrée de cellule en tapant ou en sélectionnant une valeur dans un menu. Pour créer une validation de liste pour une cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule à laquelle ajouter la validation.
1. Créez la validation pour la cellule et spécifiez le type de validation en tant que Liste.
1. Ajoutez des valeurs pour la validation de la liste.

L'exemple de code ajoute une validation de liste à C1. Lorsqu'un utilisateur clique sur la cellule, une liste s'affiche.

**Sortie : sélection d'une valeur dans la liste** 

![tâche : image_autre_texte](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Validation de la liste déroulante**
La validation de la liste déroulante permet aux utilisateurs de fournir une entrée pour les cellules en sélectionnant une valeur dans une liste prédéfinie. Pour créer une validation de liste déroulante :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule pour laquelle créer la validation.
1. Créez une validation pour la cellule et spécifiez le type comme DropDownList.
1. Ajoutez des valeurs pour la validation.

L'exemple de code ajoute une validation de liste déroulante à C1. Lorsqu'un utilisateur clique sur la cellule, une liste déroulante apparaît et les utilisateurs peuvent y sélectionner une valeur.

**Sélection d'une valeur dans une liste déroulante** 

![tâche : image_autre_texte](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Validation des expressions personnalisées**
La validation des expressions personnalisées permet aux développeurs d'écrire leurs propres expressions régulières personnalisées pour valider les valeurs d'entrée. Pour créer une validation d'expression personnalisée :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule pour laquelle créer une validation.
1. Créez une validation pour la cellule et spécifiez le type comme CustomExpression.
1. Définissez l'expression régulière de la validation.

L'exemple de code ajoute une validation d'expression personnalisée à C1. Les utilisateurs peuvent uniquement ajouter une date dans la cellule selon le format spécifié par l'expression régulière.

**Ajouter une valeur de date à C1 selon une expression régulière** 

![tâche : image_autre_texte](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forcer la validation**
En utilisant Aspose.Cells.GridWeb, les utilisateurs peuvent publier des données d'entrée sur un serveur. Même s'il existe des règles de validation pour différentes cellules mais que la propriété ForceValidation du contrôle GridWeb n'est pas définie sur true, les données d'entrée erronées seront également soumises au serveur et aucune validation n'est forcée. La propriété ForceValidation de GridWeb est toujours définie sur true par défaut.

 Lorsque la propriété ForceValidation a la valeur true, le contrôle ne publie pas de données sur le serveur Web tant que les valeurs d'entrée de toutes les cellules ne sont pas valides. Par exemple, si quelqu'un entre une valeur d'entrée non valide dans une cellule ou n'entre pas de valeur, la validation côté client est activée et les utilisateurs ne peuvent pas publier de données même s'ils cliquent sur**Nous faire parvenir**.

**Mauvaise valeur d'entrée mise en évidence par GridWeb** 

![tâche : image_autre_texte](add-cell-validations_4.png)
