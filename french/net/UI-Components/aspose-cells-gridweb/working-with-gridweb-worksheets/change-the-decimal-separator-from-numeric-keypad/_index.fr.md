---
title: Changer le séparateur décimal du pavé numérique
type: docs
weight: 150
url: /fr/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Scénarios d'utilisation possibles**
Par défaut, Aspose.Cells.GridWeb affiche les données numériques en fonction des paramètres régionaux/régionaux de la machine. Vous pouvez modifier le séparateur décimal du pavé numérique par programmation à l'aide de Aspose.Cells.GridWeb API. Ainsi, lorsqu'un fichier est importé dans la matrice GridWeb ou que vous saisissez des données numériques (à partir du pavé numérique) dans une nouvelle cellule de feuille de calcul, il devrait avoir la décimale souhaitée séparateur réglé visuellement.
## **Changer le séparateur décimal du pavé numérique**
En utilisant le**GridWorksheetCollection.NumberDecimalSeparator** vous pouvez modifier le séparateur décimal du pavé numérique par programmation. S'il vous plaît voir les captures d'écran qui montrent comment cela fonctionne

![tâche : image_autre_texte](change-the-decimal-separator-from-numeric-keypad_1.png)

![tâche : image_autre_texte](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Veuillez noter que le changement de séparateur décimal est uniquement destiné à l'expérience visuelle des utilisateurs dans GridWeb. Lorsque vous modifiez et enregistrez votre classeur, il stocke toujours les valeurs numériques (dans la feuille de calcul) selon votre séparateur décimal local/régional.

{{% /alert %}}
