---
title: Ajouter une validation de fonction personnalisée côté serveur
type: docs
weight: 110
url: /fr/net/add-custom-server-side-function-validation/
---
## **Scénarios d'utilisation possibles**
Parfois, vous devrez peut-être implémenter la validation des données côté serveur. Aspose.Cells.GridWeb vous permet d'ajouter une validation personnalisée des données côté serveur. Vous devez spécifier la plage de cellules ou la zone. Vous pouvez également définir des fonctions de validation côté client pour les rappels avec une validation côté serveur personnalisée.
## **Ajouter une validation de fonction personnalisée côté serveur**
 Vous devez définir la classe de validation du serveur qui implémente le**GridCustomServerValidationGridCustomServerValidation** via**GridValidation.ServerValidation** attribut. Vous devez également définir la fonction de validation côté client (elle doit être écrite en JavaScript côté client), cette fonction est obligatoire pour valider les données côté client lors du rappel. Vous pouvez définir la chaîne de message d'erreur via**GridValidation.ErrorMessageGridValidation.ErrorMessage** et le titre via**GridValidation.ErrorTitleGridValidation.ErrorTitle**propriétés pour vos besoins. Veuillez voir une série de captures d'écran qui montrent comment cela fonctionne (étape par étape) dans un scénario donné après avoir exécuté l'exemple de code ci-dessous. Dans l'exemple, vous ne pouvez pas mettre à jour les données dans les cellules B2 : C3. Lorsque vous essayez de modifier ces cellules dans la feuille, des messages d'erreur s'affichent et la valeur précédente est restaurée. Vous pouvez ouvrir la fenêtre de la console (dans votre navigateur) pour imprimer les informations/détails de la cellule pour certains événements.

![tâche : image_autre_texte](add-custom-server-side-function-validation_1.png)

![tâche : image_autre_texte](add-custom-server-side-function-validation_2.png)

![tâche : image_autre_texte](add-custom-server-side-function-validation_3.png)

![tâche : image_autre_texte](add-custom-server-side-function-validation_4.png)

![tâche : image_autre_texte](add-custom-server-side-function-validation_5.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
