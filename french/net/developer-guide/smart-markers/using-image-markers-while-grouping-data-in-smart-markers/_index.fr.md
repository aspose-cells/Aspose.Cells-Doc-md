---
title: Utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents
type: docs
weight: 30
url: /fr/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents**
L'exemple suivant crée un classeur, puis ajoute les balises de marqueur intelligent suivantes dans les cellules D2, E2 et F2 respectivement.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Ensuite, il remplit la source de données avec des données et appelle le[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) méthode pour traiter les marqueurs intelligents. Le code utilise ces images, c'est-à-dire[lune.png](5115492.png) et[lune2.png](5115491.png) mais vous pouvez utiliser n'importe quelle image.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
