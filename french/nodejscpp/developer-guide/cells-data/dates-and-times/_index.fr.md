---  
title: Comment gérer les dates et heures
type: docs  
weight: 600  
url: /fr/nodejs-cpp/how-to-manage-dates-and-times/  
description: Apprenez comment gérer les dates et heures via l’API Aspose.Cells for Node.js via C++.  
keywords: Comment gérer les dates et heures, le système de date 1900, le système de date 1904, définir les dates et heures, obtenir les dates et heures, gérer les dates et heures, stocker les dates et heures dans Excel, afficher les dates et heures dans les cellules.  
---  

## **Comment stocker les dates et heures dans Excel**  
Les dates et heures sont stockées dans les cellules sous forme de nombres. Ainsi, les valeurs des cellules contenant des dates et heures sont de type numérique. Un nombre qui spécifie une date et une heure se compose des composants date (partie entière) et heure (partie fractionnaire). La propriété Cell.DoubleValue renvoie ce nombre.  

## **Comment afficher les dates et heures dans Aspose.Cells**  
Pour afficher un nombre sous forme de date et heure, appliquez le format de date et heure requis à une cellule via la propriété [Style.getNumber()](https://reference.aspose.com/cells/nodejs-cpp/style/#getNumber--) ou [Style.Custom]() . La propriété CellValue.DateTimeValue renvoie l’objet DateTime, qui indique la date et l’heure représentées par le nombre contenu dans une cellule.  
<br>  
<image src="1.png" width="70%" />  

## **Comment passer de deux systèmes de dates dans Aspose.Cells**  
MS-Excel stocke les dates sous forme de nombres appelés valeurs sérielles. Une valeur sérielle est un entier qui représente le nombre de jours écoulés depuis le premier jour du système de date. Excel prend en charge les systèmes de date suivants pour les valeurs sérielles:  

1. Le système de date 1900. La première date est le 1er janvier 1900, et sa valeur sérielle est 1. La dernière date est le 31 décembre 9999, et sa valeur sérielle est 2 958 465. Ce système de date est utilisé par défaut dans le classeur.  
1. Le système de date 1904. La première date est le 1er janvier 1904, et sa valeur série est 0. La dernière date est le 31 décembre 9999, et sa valeur série est 2 957 003. Pour utiliser ce système de date dans le classeur, définissez la propriété [WorkbookSettings.getDate1904()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getDate1904--) sur true.  

Cet exemple montre que les valeurs sérielles stockées à la même date dans différents systèmes de dates sont différentes.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SwitchTwoDateSystems.js" >}}


Résultat de la sortie :  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **Comment définir la valeur DateTime dans Aspose.Cells**  
Cet exemple définit une valeur DateTime dans la cellule A1 et A2, définit un format personnalisé pour A1 et un format numérique pour A2, puis affiche les types de valeurs.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SetDateTimeValue.js" >}}


Résultat de la sortie :  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **Comment obtenir la valeur DateTime dans Aspose.Cells**  
Cet exemple définit une valeur DateTime dans la cellule A1 et A2, définit un format personnalisé pour A1 et un format numérique pour A2, vérifie les types de valeurs de deux cellules, puis affiche la valeur DateTime et la chaîne formatée.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-GetDateTimeValue.js" >}}


Résultat de la sortie :  
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

