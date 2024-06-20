---
title: Ajouter une validation de fonction côté serveur personnalisée
type: docs
weight: 110
url: /fr/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, validation côté serveur
description: Cet article présente comment travailler avec la validation côté serveur dans GridWeb.
---

## **Scénarios d'utilisation possibles**
Parfois, vous pourriez avoir besoin de mettre en œuvre une validation des données côté serveur. Aspose.Cells.GridWeb vous permet d'ajouter une validation des données côté serveur personnalisée. Vous devez spécifier la plage de cellules ou la zone. Vous pouvez également définir des fonctions de validation côté client pour des rappels avec une validation côté serveur personnalisée.
## **Ajouter une validation de fonction côté serveur personnalisée**
Vous devez définir la classe de validation côté serveur qui implémente l'interface GridCustomServerValidation via l'attribut GridValidation.ServerValidation. Vous devez également définir la fonction de validation côté client (elle doit être écrite en JavaScript côté client), cette fonction est obligatoire pour valider les données côté client lors d'un rappel. Vous pouvez définir la chaîne de message d'erreur via les propriétés GridValidation.ErrorMessage et le titre via GridValidation.ErrorTitle selon vos besoins. Veuillez consulter une série de captures d'écran qui montrent comment cela fonctionne (étape par étape) dans un scénario donné après l'exécution du code d'exemple ci-dessous. Dans l'exemple, vous ne pouvez pas mettre à jour les données dans les cellules B2:C3. Lorsque vous essayez de modifier ces cellules dans la feuille, vous verrez des messages d'erreur et la valeur précédente sera restaurée. Vous pouvez ouvrir la fenêtre de la console (dans votre navigateur) pour afficher les infos/détails des cellules pour certains événements. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
