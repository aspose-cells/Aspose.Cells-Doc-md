---
title: Comment gérer les dates et les heures
type: docs
weight: 600
url: /fr/net/how-to-manage-dates-and-times/
description: Découvrez comment gérer les dates et les heures via le Aspose.Cells for .NET API.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Comment stocker les dates et les heures dans Excel**
Les dates et les heures sont stockées dans les cellules sous forme de nombres. Ainsi, les valeurs des cellules contenant des dates et des heures sont de type numérique. Un nombre qui spécifie une date et une heure est constitué des composants date (partie entière) et heure (partie fractionnaire). La propriété Cell.DoubleValue renvoie ce numéro.

##  **Comment afficher les dates et les heures dans Aspose.Cells**
Pour afficher un nombre sous forme de date et d'heure, appliquez le format de date et d'heure requis à une cellule via le[Style.Numéro](https://reference.aspose.com/cells/net/aspose.cells/style/number/) ou[Style.Personnalisé]() propriété. La propriété CellValue.DateTimeValue renvoie l'objet DateTime, qui spécifie la date et l'heure représentées par le nombre contenu dans une cellule.
<br>
<image src="1.png" width="70%" />

##  **Comment changer deux systèmes de date dans Aspose.Cells**
MS-Excel stocke les dates sous forme de nombres appelés valeurs de série. Une valeur de série est un nombre entier correspondant au nombre de jours écoulés depuis le premier jour dans le système de date. Excel prend en charge les systèmes de date suivants pour les valeurs de série :

1. Le système de date 1900. La première date est le 1er janvier 1900 et sa valeur sérielle est 1. La dernière date est le 31 décembre 9999 et sa valeur sérielle est 2 958 465. Ce système de date est utilisé par défaut dans le classeur.
1.  Le système de date de 1904. La première date est le 1er janvier 1904 et sa valeur sérielle est 0. La dernière date est le 31 décembre 9999 et sa valeur sérielle est 2 957 003. Pour utiliser ce système de date dans le classeur, définissez le[Classeur.Paramètres.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) propriété à vrai.


Cet exemple montre que les valeurs de série stockées à la même date dans différents systèmes de date sont différentes.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Résultat de sortie :
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Comment définir la valeur DateTime dans Aspose.Cells**
Cet exemple définit une valeur DateTime dans les cellules A1 et A2, définit le format personnalisé de A1 et le format numérique de A2, puis génère les types de valeur.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Résultat de sortie :
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Comment obtenir la valeur DateTime dans Aspose.Cells**
Cet exemple définit une valeur DateTime dans les cellules A1 et A2, définit le format personnalisé de A1 et le format numérique de A2, vérifie les types de valeur de deux cellules, puis génère la valeur DateTime et la chaîne formatée.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Résultat de sortie :
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
