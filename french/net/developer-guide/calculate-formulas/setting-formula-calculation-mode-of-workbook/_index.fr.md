---
title: Définition du mode de calcul de formule du classeur
description: Cet article explique comment définir le mode de calcul de formule d'un classeur dans Excel Microsoft avec la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour définir le mode de calcul de la formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /fr/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel vous permet de définir le mode de calcul des formules, c'est-à-dire la manière dont les formules sont calculées. Il y a trois valeurs possibles :

- Automatique : recalculez chaque fois que quelque chose est modifié et chaque fois qu'un classeur est ouvert.
- Automatique sauf pour les tableaux de données - recalculez chaque fois que quelque chose est modifié, mais en laissant de côté les tableaux de données.
- Manuel : recalculez uniquement lorsque l'utilisateur le demande explicitement en appuyant sur F9 ou CTRL+ALT+F9, ou lorsque le classeur est enregistré.

{{% /alert %}}

Pour définir le mode de calcul de la formule dans Excel Microsoft :

1.  Sélectionner**Formules** puis *Options de calcul**.
1. Sélectionnez l'une des options.

 Aspose.Cells vous permet également de définir le**Mode de calcul de formule** en utilisant[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) propriété de mode. Vous pouvez lui attribuer le[**TypeModeCalc**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)énumération qui a l’une des valeurs suivantes :

- CalcModeType.Automatique
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manuel

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
