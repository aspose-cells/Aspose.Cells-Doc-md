---
title: Ajouter des validations de cellules
type: docs
weight: 70
url: /fr/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb, GridValidation, validation de liste, validation d expression personnalisée
description: Cet article présente comment ajouter une validation de liste, une validation de liste déroulante et une validation d expression personnalisée dans GridWeb.
---

{{% alert color="primary" %}} 

Une des fonctionnalités avancées d'Aspose.Cells.GridWeb est d'ajouter des règles de validation d'entrée pour les cellules. Les développeurs peuvent créer différents types de règles de validation pour les cellules afin de contrôler et valider les valeurs d'entrée. Ce sujet aborde les types de validation pris en charge et comment les créer.

{{% /alert %}} 
## **Types de validations**
Trois types de validations peuvent être appliqués à l'aide d'Aspose.Cells.GridWeb :

- Validation de liste.
- Validation de liste déroulante.
- Validation d'expression personnalisée.

Chacun est discuté en détail ci-dessous.
### **Validation de liste**
La validation de liste permet aux utilisateurs de fournir une entrée de cellule soit en tapant, soit en sélectionnant une valeur dans un menu. Pour créer une validation de liste pour une cellule :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule pour ajouter la validation.
1. Créez la validation pour la cellule et spécifiez le type de validation comme List.
1. Ajoutez des valeurs pour la validation de la liste.

Le code exemple ajoute une validation de liste à C1. Lorsqu'un utilisateur clique sur la cellule, une liste apparaît.

**Résultat : sélection d'une valeur dans la liste** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Validation de liste déroulante**
La validation de liste déroulante permet aux utilisateurs de fournir une entrée pour les cellules en sélectionnant une valeur dans une liste prédéfinie. Pour créer une validation de liste déroulante :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule pour créer la validation.
1. Créez une validation pour la cellule et spécifiez le type comme DropDownList.
1. Ajoutez des valeurs pour la validation.

L'exemple de code ajoute une validation de liste déroulante à C1. Lorsqu'un utilisateur clique sur la cellule, une liste déroulante apparaît et les utilisateurs peuvent sélectionner une valeur.

**Sélectionner une valeur dans une liste déroulante** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Validation d'expression personnalisée**
La validation d'expression personnalisée permet aux développeurs d'écrire leurs propres expressions régulières personnalisées pour valider les valeurs d'entrée. Pour créer une validation d'expression personnalisée :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Accéder à une feuille de calcul.
1. Accédez à la cellule pour créer une validation.
1. Créez une validation pour la cellule et spécifiez le type comme CustomExpression.
1. Définissez l'expression régulière de la validation.

Le code exemple ajoute une validation d'expression personnalisée à C1. Les utilisateurs ne peuvent ajouter qu'une date dans la cellule selon le format spécifié par l'expression régulière.

**Ajout d'une valeur de date à C1 selon une expression régulière** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Forcer la validation**
En utilisant Aspose.Cells.GridWeb, les utilisateurs peuvent envoyer des données d'entrée à un serveur. Même s'il existe des règles de validation pour différentes cellules, si la propriété ForceValidation du contrôle GridWeb n'est pas définie sur true, les données d'entrée incorrectes seront tout de même soumises au serveur et aucune validation ne sera forcée. La propriété ForceValidation de GridWeb est toujours définie sur true par défaut.

Lorsque la propriété ForceValidation est true, le contrôle ne soumet pas les données au serveur web tant que les valeurs d'entrée de toutes les cellules ne sont pas valides. Par exemple, si quelqu'un entre une valeur d'entrée incorrecte dans une cellule, ou ne saisit pas de valeur, la validation côté client est activée et les utilisateurs ne peuvent pas envoyer de données même s'ils cliquent sur **Soumettre**.

**Valeur d'entrée incorrecte surlignée par GridWeb** 

![todo:image_alt_text](add-cell-validations_4.png)
