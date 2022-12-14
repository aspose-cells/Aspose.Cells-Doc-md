---
title: Définition du mode de calcul de la formule du classeur
type: docs
weight: 130
url: /fr/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel vous permet de définir le mode de calcul de la formule, c'est-à-dire la manière dont les formules sont calculées. Il y a trois valeurs possibles :

- Automatique - recalcule chaque fois que quelque chose est modifié et chaque fois qu'un classeur est ouvert.
- Automatique sauf pour les tableaux de données - recalcule chaque fois que quelque chose est modifié, mais en omettant les tableaux de données.
- Manuel - recalcule uniquement lorsque l'utilisateur le demande explicitement en appuyant sur F9 ou CTRL+ALT+F9, ou lorsque le classeur est enregistré.

{{% /alert %}}

Pour définir le mode de calcul de la formule dans Microsoft Excel :

1.  Sélectionner**Formules** et alors**Options de calcul**.
1. Sélectionnez l'une des options.

 Aspose.Cells vous permet également de régler le**Mode de calcul de formule** en utilisant le[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) propriété. Vous pouvez lui attribuer le[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)énumération qui prend l'une des valeurs suivantes :

- [**CalcModeType.AUTOMATIQUE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

 L'exemple de code suivant crée d'abord un classeur, puis définit le mode de calcul de la formule sur**Manuel** et enregistre le classeur en tant que fichier Excel de sortie sur le disque.

**Le fichier de sortie. Notez le mode de calcul de la formule.**

![tâche : image_autre_texte](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
