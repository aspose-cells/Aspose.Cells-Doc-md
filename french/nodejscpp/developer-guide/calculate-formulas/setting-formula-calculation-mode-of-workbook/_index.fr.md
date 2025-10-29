---  
title: Définir le mode de calcul des formules du classeur avec Node.js via C++  
linktitle: Définir le mode de calcul de formule du classeur  
description: Cet article présente comment définir le mode de calcul des formules d un classeur dans Microsoft Excel avec Aspose.Cells for Node.js via C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour définir le mode de calcul des formules et obtenir le résultat. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.  
keywords: Aspose.Cells, Excel, classeur, mode de calcul des formules, paramètres, Node.js via C++  
type: docs  
weight: 110  
url: /fr/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
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

Aspose.Cells for Node.js via C++ permet également de définir le **Mode de calcul des formules** en utilisant la propriété mode [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--). Vous pouvez lui attribuer l'énumération [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) qui possède l'une des valeurs suivantes :  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
