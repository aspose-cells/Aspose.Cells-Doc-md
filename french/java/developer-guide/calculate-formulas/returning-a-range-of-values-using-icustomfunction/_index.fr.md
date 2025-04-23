---
title: Retourner une plage de valeurs en utilisant ICustomFunction
type: docs
weight: 270
url: /fr/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Le [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) est obsolète depuis la version Aspose.Cells for Java 20.8. Veuillez utiliser la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). L'utilisation de la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) est décrite dans l'article suivant.

[Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells fournit l'interface [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) qui est utilisée pour implémenter des fonctions personnalisées ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

La plupart du temps, lorsque vous implémentez la méthode de l'interface [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), vous devez renvoyer une seule valeur de cellule. Mais parfois, vous devez renvoyer une plage de valeurs. Cet article expliquera comment renvoyer la plage de valeurs depuis [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Retourner une plage de valeurs en utilisant ICustomFunction**

Le code suivant implémente [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) et renvoie la plage de valeurs via sa méthode. Veuillez vérifier le [fichier Excel de sortie](5472922.xlsx) et le [pdf](5472925.pdf) généré avec le code pour votre référence.

Créez une classe avec une fonction *CalculateCustomFunction*. Cette classe implémente [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}
