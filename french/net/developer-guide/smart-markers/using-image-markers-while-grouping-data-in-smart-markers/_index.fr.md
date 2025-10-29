---
title: Comment utiliser les marqueurs d images dans Smart Markers
type: docs
weight: 30
url: /fr/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Scénarios d'utilisation possibles**
Les marqueurs d'images sont des espaces réservés spécialisés dans les systèmes de gabarits (comme FoxPro, Handlebars ou frameworks UI modernes) qui injectent dynamiquement des images ou des éléments visuels dans les modèles. Parfois, vous devez insérer des images en utilisant des smart markers. Aspose.Cells permet d'ajouter des images aux smart markers.

## **Paramètres d'image dans Smart Markers**
Paramètres de marqueurs intelligents pour gérer les images.

- **Image:Ajusteràlacellule** - Ajuster automatiquement l'image à la hauteur de la ligne et à la largeur de la colonne de la cellule.
- **Image:EchelleN** - Adapter la hauteur et la largeur à N pour cent.
- **Image:Largeur:NpoetHauteur:Npoet** - Rendre l'image haute de N pouces et large de N pouces. Vous pouvez également spécifier les positions Gauche et Haut (en points).

## **Comment utiliser les marqueurs d'image dans Smart Markers**
Veuillez voir le code d'exemple suivant qui montre comment insérer des images en utilisant des marqueurs intelligents.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Comment utiliser les marqueurs d'image lors du regroupement de données dans Smart Markers**
L'exemple suivant crée un classeur puis ajoute les balises de marqueurs intelligents suivantes dans les cellules D2, E2 et F2 respectivement.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Ensuite, il remplit la source de données avec des données et appelle la méthode [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) pour traiter les balises de marqueurs intelligents. Le code utilise ces images c'est-à-dire [moon.png](5115492.png) et [moon2.png](5115491.png) mais vous pouvez utiliser n'importe quelle image.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
