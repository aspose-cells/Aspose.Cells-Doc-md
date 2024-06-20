---
title: Utilisation des marqueurs d image lors du regroupement de données dans les Smart Markers
type: docs
weight: 630
url: /fr/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Cet article présente un exemple qui illustre l'utilisation des marqueurs d'image lors du regroupement de données dans les smart markers.

{{% /alert %}} 
## **Utilisation des marqueurs d'image lors du regroupement des données dans des marqueurs intelligents**
Le code d'exemple suivant crée un classeur, puis ajoute les balises de smart marker suivantes dans les cellules D2, E2 et F2 respectivement.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Il remplit ensuite la source de données avec des données et appelle la méthode [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) pour traiter les balises smart marker. Le code utilise ces images à savoir [moon.png](5472549.png) et [moon2.png](5472548.png) mais vous pouvez utiliser n'importe quelle image. La capture d'écran suivante montre la sortie de ce code d'exemple. Comme vous pouvez le constater, les données des colonnes E et F sont regroupées par rapport aux données de la colonne D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
