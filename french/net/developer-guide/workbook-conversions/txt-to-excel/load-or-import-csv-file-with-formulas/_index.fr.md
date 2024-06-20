---
title: Charger ou importer un fichier CSV avec des formules
type: docs
weight: 350
url: /fr/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Les fichiers CSV contiennent principalement des données textuelles et ne contiennent pas de formules. Cependant, il arrive parfois que des fichiers CSV contiennent également des formules. Ces fichiers CSV doivent être chargés en définissant la propriété **[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula)** sur **true**. Une fois cette propriété définie sur **true**, Aspose.Cells ne traitera pas la formule comme un simple texte. Elles seront traitées comme une formule et le moteur de calcul de formules d'Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

Le code suivant illustre comment vous pouvez charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À des fins d'illustration, nous utilisons le [fichier CSV simple](5115034.csv) qui contient ces données. Comme vous pouvez le constater, il contient une formule.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Le code charge d'abord le fichier CSV, puis l'importe à nouveau dans la cellule D4. Enfin, il enregistre l'objet classeur au format XSLX. Le [fichier XLSX de sortie](5115052.xlsx) ressemble à ceci. Comme vous pouvez le constater, la cellule C3 et F4 contiennent une formule et son résultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

