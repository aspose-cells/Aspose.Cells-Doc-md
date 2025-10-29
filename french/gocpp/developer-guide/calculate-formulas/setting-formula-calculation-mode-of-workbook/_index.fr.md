---
title: Définir le mode de calcul des formules du classeur avec Golang via C++
linktitle: Définir le mode de calcul de formule du classeur
description: Cet article explique comment définir le mode de calcul des formules d’un classeur dans Microsoft Excel en utilisant la bibliothèque Aspose.Cells avec C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour définir le mode de calcul des formules et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, classeur, mode de calcul des formules, paramètres, C++
type: docs
weight: 110
url: /fr/go-cpp/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells vous permet également de définir le **Mode de calcul de formule** en utilisant [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/) propriété de mode. Vous pouvez lui assigner la [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) énumération qui a l'une des valeurs suivantes:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}
