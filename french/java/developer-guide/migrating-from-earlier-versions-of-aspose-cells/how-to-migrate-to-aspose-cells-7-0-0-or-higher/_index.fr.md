---
title: Comment migrer vers Aspose.Cells 7.0.0 ou une version supérieure
type: docs
weight: 10
url: /fr/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

Dans cet article, nous avons partagé les changements notables dans l'API qui ont été effectués dans les versions Aspose.Cells for Java 7.0.0 et ultérieures par rapport aux versions précédentes de Aspose.Cells for Java. Cet article aidera les utilisateurs à migrer rapidement de l'ancienne API à la nouvelle API en comprenant les modifications apportées et en les mettant en œuvre dans leurs applications.

{{% /alert %}}

## **Changements notables pour les utilisateurs existants**

Depuis la sortie de Aspose.Cells for Java v7.0.0, nous avons apporté des modifications majeures à l'API et avons ajouté toutes les fonctionnalités présentes dans Aspose.Cells for .NET à ce jour. Ainsi, tant Aspose.Cells for Java que .NET seront désormais comparables en termes de fonctionnalités et même en termes de noms de méthodes et de propriétés.

Tout comme l'approche précédente, vous pouvez simplement importer une seule instruction d'importation dans votre application pour récupérer toutes les classes, interfaces, etc.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Nous avons renommé certaines API pour nettoyer la structure de l'API afin de l'aligner sur Aspose.Cells for .NET. Nous avons maintenant ajouté certaines classes de collection et les avons remplacées par des classes de collection existantes. Par exemple, la classe Worksheets a été remplacée par **WorksheetCollection**. De même, la classe Shapes a été remplacée par **ShapeCollection**. Cependant, la fonctionnalité des classes n'a pas été affectée, mais plutôt améliorée.

Si vous souhaitez migrer vers la nouvelle API, vous devrez peut-être effectuer les modifications suivantes dans votre application pour que tout fonctionne de votre côté. La liste suivante contient les modifications apportées aux classes et à leurs méthodes respectives.

## **Résumé des modifications apportées à l'API**

1) Les collections dans v2.5.4 ou antérieures dont les noms se terminent par 's' sont renommées. Dans v7.0.0 ou version ultérieure, les collections sont nommées :
par exemple, Shapes (Ancien) -> ShapeCollection (Nouveau), Worksheets (Ancien) -> WorksheetCollection (Nouveau), ...,etc.

2) L'obtention d'un élément de la collection est modifiée. Par exemple, dans v2.5.4 ou antérieur, nous avions l'habitude de le faire avec getXXX(int), dans v7.0.0 ou version ultérieure, nous le faisons maintenant avec get(int) :
par exemple, Worksheets.getSheet(int) (Ancien) -> WorksheetCollection.get(int) (Nouveau), ...etc.

3) L'obtention de la taille (nombre d'éléments) d'une collection est modifiée. Dans v2.5.4 ou antérieure, nous avions l'habitude de le faire avec size(), dans v7.0.0 ou version ultérieure, nous le faisons maintenant avec getCount() :
Worksheets.size() (Ancien) -> WorksheetCollection.getCount() (Nouveau), ...,etc.

4) Les méthodes getter des propriétés booléennes dont les noms commencent par 'is' dans v2.5.4 ou antérieure sont changées. Dans v7.0.0, elles commencent par "get" :
par exemple, PageSetup.isBlackAndWhite() (Ancien) -> PageSetup.getBlackAndWhite() (Nouveau), ...,etc.
{{< app/cells/assistant language="java" >}}
