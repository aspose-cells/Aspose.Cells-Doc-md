---
title: Comment migrer vers Aspose.Cells 7.0.0 ou supérieur
type: docs
weight: 10
url: /fr/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

Dans cet article, nous avons partagé les changements notables dans le API qui ont été effectués dans Aspose.Cells for Java 7.0.0 et les versions ultérieures par rapport aux versions précédentes de Aspose.Cells for Java. Cet article aidera les utilisateurs à migrer rapidement de l'ancien API vers le nouveau API en comprenant les modifications apportées et en les réalisant dans leurs applications.

{{% /alert %}}

## **Changements notables pour les utilisateurs existants**

Depuis la sortie de Aspose.Cells for Java v7.0.0, nous avons apporté des modifications majeures au API et avons ajouté toutes les fonctionnalités présentes dans Aspose.Cells for .NET à ce jour. Ainsi, Aspose.Cells for Java et .NET seront désormais comparables en termes de fonctionnalités et même en termes de noms de méthodes et de propriétés.

Semblable à l'ancienne approche, vous pouvez simplement importer une seule instruction d'importation dans votre application pour récupérer toutes les classes, interfaces, etc.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Nous avons renommé certains ensembles API pour nettoyer la structure API afin qu'elle corresponde à Aspose.Cells for .NET. Nous avons maintenant ajouté des classes de collection et les avons remplacées par des classes de collection existantes. Comme la classe Worksheets a été remplacée par**WorksheetCollection** . De même, la classe Shapes a été remplacée par**ShapeCollection**. Cependant, la fonctionnalité des classes n'a pas été affectée plutôt améliorée.

Si vous souhaitez migrer vers le nouveau API, vous devrez peut-être effectuer les modifications suivantes dans votre application pour que les choses fonctionnent de votre côté. La liste suivante contient les modifications apportées aux classes ainsi que leurs méthodes respectives.

## **Résumé des changements dans le API**

1) Collections en v2.5.4 ou antérieures dont les noms se terminant par 's' sont renommés. Dans la version 7.0.0 ou ultérieure, les collections sont nommées :
par exemple, Formes (Ancien) -> ShapeCollection (Nouveau), Worksheets (Ancien) -> WorksheetCollection (Nouveau), ..., etc.

2) L'obtention d'un élément de la collection est modifiée. Par exemple, dans la version 2.5.4 ou antérieure, nous avions l'habitude de le faire sous la forme getXXX(int), dans la version 7.0.0 ou supérieure, nous le faisons maintenant sous la forme get(int) :
par exemple, Worksheets.getSheet(int) (Ancien) -> WorksheetCollection.get(int) (Nouveau), ... etc.

3) L'obtention de la taille (nombre d'éléments) d'une collection est modifiée. Dans la v2.5.4 ou antérieure, nous avions l'habitude de le faire avec size(), dans la v7.0.0 ou supérieure, maintenant nous le faisons avec getCount() :
Worksheets.size() (Ancien) -> WorksheetCollection.getCount() (Nouveau), ..., etc.

4) Les méthodes getter des propriétés booléennes dans la version 2.5.4 ou antérieure dont les noms commençant par "is" sont modifiés. Dans la v7.0.0, ceux-ci sont démarrés par "get":
par exemple, PageSetup.isBlackAndWhite() (Ancien) -> PageSetup.getBlackAndWhite() (Nouveau), ..., etc.
