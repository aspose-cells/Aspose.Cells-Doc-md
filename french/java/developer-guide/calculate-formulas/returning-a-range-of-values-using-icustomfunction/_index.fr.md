---
title: Renvoyer une plage de valeurs à l'aide de ICustomFunction
type: docs
weight: 270
url: /fr/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 La[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) est obsolète depuis la sortie de Aspose.Cells for Java 20.8. Veuillez utiliser le[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) classer. L'utilisation de la[**RésuméCalculMoteur**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) classe est décrite dans l'article suivant.

[Retour d'une plage de valeurs à l'aide de AbstractCalculationEngine](/cells/fr/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells fournit[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)interface utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Surtout lorsque vous implémentez le[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) méthode d'interface, vous devez renvoyer une seule valeur de cellule. Mais parfois, vous devez renvoyer une plage de valeurs. Cet article explique comment renvoyer la plage de valeurs de[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Renvoyer une plage de valeurs à l'aide de ICustomFunction**

 Le code suivant implémente[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) et renvoie la plage de valeurs via sa méthode. S'il vous plaît, vérifiez le[fichier excel de sortie](5472922.xlsx) et[pdf](5472925.pdf) généré avec le code pour votre référence.

Créer une classe avec une fonction*CalculateCustomFunction*. Cette classe implémente[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
