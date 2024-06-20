---
title: Retourner une plage de valeurs en utilisant ICustomFunction
description: Cet article décrit comment utiliser la bibliothèque Aspose.Cells pour retourner une plage de valeurs avec ICustomFunction dans Microsoft Excel. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour obtenir une plage de valeurs et retourner le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, ICustomFunction, retourne une série de valeurs
type: docs
weight: 50
url: /fr/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Le [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) est obsolète depuis la version Aspose.Cells for Java 20.8. Veuillez utiliser la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). L'utilisation de la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) est décrite dans l'article suivant.

[Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells fournit l'interface [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) qui est utilisée pour implémenter des fonctions personnalisées ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

La plupart du temps, lorsque vous implémentez la méthode de l'interface [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), vous devez renvoyer une seule valeur de cellule. Mais parfois, vous devez renvoyer une plage de valeurs. Cet article expliquera comment renvoyer la plage de valeurs depuis [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

Le code suivant implémente [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) et renvoie la plage de valeurs via sa méthode.

Créez une classe avec une fonction *CalculateCustomFunction*. Cette classe implémente [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Maintenant utilisez la fonction ci-dessus dans votre programme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
