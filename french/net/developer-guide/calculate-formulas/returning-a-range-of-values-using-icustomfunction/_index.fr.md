---
title: Renvoyer une plage de valeurs à l'aide de ICustomFunction
description: Cet article décrit comment utiliser la bibliothèque Aspose.Cells pour renvoyer une plage de valeurs avec ICustomFunction dans Excel Microsoft. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour obtenir une plage de valeurs et renvoyer le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /fr/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Le[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) est obsolète depuis la sortie de Aspose.Cells for Java 20.8. Veuillez utiliser le[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe. L'utilisation du[**RésuméCalculMoteur**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) la classe est décrite dans l’article suivant.

[Renvoi d'une plage de valeurs à l'aide de AbstractCalculationEngine](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells fournit[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)interface utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées qui ne sont pas prises en charge par Microsoft Excel en tant que fonctions intégrées.

 Surtout lorsque vous mettez en œuvre le[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) méthode d'interface, vous devez renvoyer une valeur de cellule unique. Mais parfois, vous devez renvoyer une plage de valeurs. Cet article explique comment renvoyer la plage de valeurs de[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Le code suivant implémente[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)et renvoie la plage de valeurs via sa méthode.

Créez une classe avec une fonction *CalculateCustomFunction*. Cette classe implémente[**ICustomFonction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Utilisez maintenant la fonction ci-dessus dans votre programme

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
