---
title: Définition du mode de calcul de la formule du classeur
type: docs
weight: 110
url: /fr/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel vous permet de définir le mode de calcul de la formule, c'est-à-dire la manière dont les formules sont calculées. Il y a trois valeurs possibles :

- Automatique - recalcule chaque fois que quelque chose est modifié et chaque fois qu'un classeur est ouvert.
- Automatique sauf pour les tableaux de données - recalcule chaque fois que quelque chose est modifié, mais en omettant les tableaux de données.
- Manuel - recalcule uniquement lorsque l'utilisateur le demande explicitement en appuyant sur F9 ou CTRL+ALT+F9, ou lorsque le classeur est enregistré.

{{% /alert %}}

Pour définir le mode de calcul de la formule dans Microsoft Excel :

1.  Sélectionner**Formules** et puis**Options de calcul**.
1. Sélectionnez l'une des options.

 Aspose.Cells vous permet également de régler le**Mode de calcul de formule** en utilisant[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) propriété de mode. Vous pouvez lui attribuer le[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)énumération qui prend l'une des valeurs suivantes :

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
