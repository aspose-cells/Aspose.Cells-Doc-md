---
title: Calculer le facteur d échelle de la mise en page
type: docs
weight: 260
url: /fr/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

Lorsque vous définissez l'échelle de mise en page à l'aide de l'option **Ajuster à n page(s) de large sur m de hauteur**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale). Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, si elle renvoie 0,5079621076, cela signifie que le facteur d'échelle est de 51%.

{{% /alert %}} 
## **Calculer le facteur d'échelle de la mise en page**
Le code d'exemple suivant illustre comment calculer le facteur d'échelle de mise en page à l'aide de la propriété [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
