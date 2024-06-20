---
title: Définir le mode de calcul de formule du classeur
description: Cet article présente comment définir le mode de calcul de formule d un classeur dans Microsoft Excel avec la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour définir le mode de calcul de formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, classeur, mode de calcul de formule, réglages
type: docs
weight: 110
url: /fr/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel vous permet de définir le mode de calcul de formule, c'est-à-dire la manière dont les formules sont calculées. Il existe trois valeurs possibles

- Automatique - recalculer chaque fois qu'une modification est apportée, et à chaque ouverture d'un classeur.
- Automatique sauf pour les tables de données - recalculer chaque fois qu'une modification est apportée, mais en excluant les tables de données.
- Manuel - recalculer seulement lorsque l'utilisateur le demande explicitement en appuyant sur F9 ou CTRL+ALT+F9, ou lorsque le classeur est enregistré.

{{% /alert %}}

Pour définir le mode de calcul des formules dans Microsoft Excel :

1. Sélectionnez **Formules** puis **Options de calcul**.
1. Sélectionnez l'une des options.

Aspose.Cells vous permet également de définir le **Mode de calcul de formule** en utilisant [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) propriété de mode. Vous pouvez lui assigner la [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) énumération qui a l'une des valeurs suivantes:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
