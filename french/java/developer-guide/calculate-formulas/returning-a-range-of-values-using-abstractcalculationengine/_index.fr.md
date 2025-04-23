---
title: Renvoyer une plage de valeurs en utilisant AbstractCalculationEngine
type: docs
weight: 275
url: /fr/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées non prises en charge par Microsoft Excel en tant que fonctions intégrées.

Cet article expliquera comment renvoyer la plage de valeurs de [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

Le code suivant démontre l'utilisation de [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) et retourne la plage de valeurs via sa méthode.

Créez une classe avec une fonction *CalculateCustomFunction*. Cette classe étend [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
{{< app/cells/assistant language="java" >}}
