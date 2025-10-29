---
title: Retourner une plage de valeurs en utilisant AbstractCalculationEngine avec Golang via C++
linktitle: Renvoyer une plage de valeurs en utilisant AbstractCalculationEngine
description: Cet article présente un moteur de calcul abstrait qui retourne une plage de valeurs dans Microsoft Excel en utilisant la bibliothèque Aspose.Cells avec Golang via C++. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour obtenir une plage de valeurs et retourner le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, un moteur de calcul abstrait qui renvoie une série de valeurs
type: docs
weight: 55
url: /fr/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées non prises en charge par Microsoft Excel en tant que fonctions intégrées.

Cet article expliquera comment renvoyer la plage de valeurs de [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{% /alert %}}

Le code suivant démontre l'utilisation de la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) et retourne la plage de valeurs via sa méthode.

Créer une classe avec une fonction `CalculateCustomFunction`. Cette classe implémente [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
Utilisez maintenant la fonction ci-dessus dans votre programme.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
