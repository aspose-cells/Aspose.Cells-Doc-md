---
title: Charger ou importer le fichier CSV avec des formules
type: docs
weight: 350
url: /fr/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 Le fichier CSV contient principalement des données textuelles et ne contient aucune formule. Cependant, il arrive parfois que les fichiers CSV contiennent également des formules. Ces fichiers CSV doivent être chargés en définissant le[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) comme**vrai** . Une fois cette propriété définie**vrai**, Aspose.Cells ne traitera pas la formule comme du texte simple. Ils seront traités comme des formules et le moteur de calcul de formule Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

 Le code suivant illustre comment vous pouvez charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. A des fins d'illustration, nous utilisons le[fichier csv simple](5115034.csv) qui contient ces données. Comme vous le voyez, il contient une formule.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Le code charge d'abord le fichier CSV, puis l'importe à nouveau dans la cellule D4. Enfin, il enregistre l'objet classeur au format XSLX. Le[fichier de sortie XLSX](5115052.xlsx) ressemble à ça. Comme vous le voyez, les cellules C3 et F4 contiennent la formule et son résultat 800.

|![tâche : image_autre_texte](load-or-import-csv-file-with-formulas_1.png)|
|:- |

