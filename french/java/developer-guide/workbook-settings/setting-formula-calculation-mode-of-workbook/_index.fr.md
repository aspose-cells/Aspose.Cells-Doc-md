---
title: Définir le mode de calcul de formule du classeur
type: docs
weight: 130
url: /fr/java/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells vous permet également de définir le **Mode de calcul des formules** en utilisant la propriété [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode). Vous pouvez lui attribuer l'énumération [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) qui a l'une des valeurs suivantes :

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC-EXCEPT-TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Le code d'exemple suivant crée d'abord un classeur, puis définit le mode de calcul des formules sur **Manuel** et enregistre le classeur en tant que fichier Excel de sortie sur le disque.

**Le fichier de sortie. Remarquez le mode de calcul des formules.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
{{< app/cells/assistant language="java" >}}
