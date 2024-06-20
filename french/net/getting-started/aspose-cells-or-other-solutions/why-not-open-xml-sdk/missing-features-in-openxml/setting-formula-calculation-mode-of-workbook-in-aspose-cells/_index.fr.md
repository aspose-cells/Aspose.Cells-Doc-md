---
title: Définir le mode de calcul de formule du classeur dans Aspose.Cells
type: docs
weight: 100
url: /fr/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

Aspose.Cells vous permet également de définir le **Mode de Calcul des Formules** en utilisant la propriété du mode FormulaSettings.CalculationMode. Vous pouvez lui attribuer l'énumération CalcModeType qui a l'une des valeurs suivantes :

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Le code d'exemple suivant crée d'abord un classeur, puis définit le mode de calcul des formules sur **Manuel** et enregistre le classeur en tant que fichier Excel de sortie sur le disque.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Télécharger un exemple en cours d'exécution**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
