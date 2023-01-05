---
title: Utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents
type: docs
weight: 630
url: /fr/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Cet article présente un exemple qui illustre l'utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents.

{{% /alert %}} 
## **Utilisation de marqueurs d'image lors du regroupement de données dans des marqueurs intelligents**
L'exemple de code suivant crée un classeur, puis ajoute les balises de marqueur intelligent suivantes dans les cellules D2, E2 et F2 respectivement.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Ensuite, il remplit la source de données avec des données et appelle le[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) pour traiter les marqueurs intelligents. Le code utilise ces images, c'est-à-dire[lune.png](5472549.png) et[lune2.png](5472548.png) mais vous pouvez utiliser n'importe quelle image. La capture d'écran suivante montre la sortie de cet exemple de code. Comme vous pouvez le voir, les données des colonnes E et F sont regroupées par rapport aux données de la colonne D.

![tâche : image_autre_texte](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
