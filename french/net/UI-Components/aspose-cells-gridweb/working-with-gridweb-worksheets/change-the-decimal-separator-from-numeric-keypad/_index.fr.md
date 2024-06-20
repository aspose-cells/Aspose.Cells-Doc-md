---
title: Changer le séparateur décimal à partir du pavé numérique
type: docs
weight: 150
url: /fr/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb, décimal, séparateur décimal
description: Cet article présente comment changer le séparateur décimal dans GridWeb.
---

## **Scénarios d'utilisation possibles**
Par défaut, Aspose.Cells.GridWeb affiche les données numériques en fonction des paramètres régionaux sur la machine. Vous pouvez changer le séparateur décimal à partir du pavé numérique de manière programmée en utilisant l'API Aspose.Cells.GridWeb. Ainsi, lorsque vous importez un fichier dans la matrice GridWeb ou que vous saisissez des données numériques (à partir du pavé numérique) dans une nouvelle cellule de feuille de calcul, elles devraient avoir votre séparateur décimal souhaité défini visuellement. 
## **Changer le séparateur décimal à partir du pavé numérique**
En utilisant la propriété **GridWorksheetCollection.NumberDecimalSeparator**, vous pouvez changer le séparateur décimal à partir du pavé numérique de manière programmée. Veuillez consulter les captures d'écran qui montrent comment cela fonctionne.

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Veuillez noter que le changement du séparateur décimal est uniquement destiné à l'expérience visuelle des utilisateurs dans GridWeb. Lorsque vous modifiez et enregistrez votre classeur, il conservera toujours les valeurs numériques (dans la feuille de calcul) selon votre séparateur décimal local/régional.

{{% /alert %}}
