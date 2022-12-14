---
title: Calculer le facteur d'échelle de mise en page
type: docs
weight: 260
url: /fr/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

Lorsque vous définissez la mise à l'échelle de la mise en page à l'aide de**Ajuster à n page(s) de large par m de haut** option, Microsoft Excel calcule le facteur de mise à l'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) propriété. Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, s'il renvoie 0,5079621076, cela signifie que le facteur d'échelle est de 51 %.

{{% /alert %}} 
## **Calculer le facteur d'échelle de mise en page**
 L'exemple de code suivant illustre comment calculer le facteur d'échelle de mise en page à l'aide de[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Sortie console**
Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
