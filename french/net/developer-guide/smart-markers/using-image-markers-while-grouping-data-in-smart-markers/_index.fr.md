---
title: Utilisation des marqueurs d image lors du regroupement de données dans les Smart Markers
type: docs
weight: 30
url: /fr/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Utilisation des marqueurs d'image lors du regroupement des données dans des marqueurs intelligents**
L'exemple suivant crée un classeur puis ajoute les balises de marqueurs intelligents suivantes dans les cellules D2, E2 et F2 respectivement.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Ensuite, il remplit la source de données avec des données et appelle la méthode [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) pour traiter les balises de marqueurs intelligents. Le code utilise ces images c'est-à-dire [moon.png](5115492.png) et [moon2.png](5115491.png) mais vous pouvez utiliser n'importe quelle image.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
