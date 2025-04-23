---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
description: Cet article décrit comment étendre le moteur de calcul par défaut en implémentant un moteur de calcul personnalisé à l aide de la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour implémenter un moteur de calcul personnalisé et obtenir les résultats. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, Moteur de calcul personnalisé, étend le moteur de calcul par défaut
type: docs
weight: 80
url: /fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul qui peut calculer presque toutes les formules Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) qui possède une méthode [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la fonction **TODAY** et ajoutons un jour à la date système. Ainsi, si la date actuelle est le 27/07/2023, le moteur personnalisé calculera AUJOURDHUI() comme le 28/07/2023.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Résultat**

Veuillez vérifier la sortie de la console du code d'échantillon ci-dessus, la valeur (date/heure) de A1 avec le moteur personnalisé devrait être un jour plus tard que le résultat sans le moteur personnalisé.

### **Article connexe**

{{% alert color="primary" %}}

[Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
