---
title: Définition du mode de calcul de formule du classeur dans Aspose.Cells
type: docs
weight: 100
url: /fr/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

 Aspose.Cells vous permet également de régler le**Mode de calcul de formule** en utilisant la propriété de mode FormulaSettings.CalculationMode. Vous pouvez lui affecter l'énumération CalcModeType qui a l'une des valeurs suivantes :

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

 L'exemple de code suivant crée d'abord un classeur, puis définit le mode de calcul de la formule sur**Manuel** et enregistre le classeur en tant que fichier Excel de sortie sur le disque.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Télécharger l'exemple d'exécution**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
