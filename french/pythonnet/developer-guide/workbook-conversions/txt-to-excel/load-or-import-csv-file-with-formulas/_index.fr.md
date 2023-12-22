---
title: Charger ou importer le fichier CSV avec des formules
type: docs
weight: 350
url: /fr/python-net/load-or-import-csv-file-with-formulas/
description: Chargez ou importez le fichier CSV avec des formules en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 Le fichier CSV contient principalement des données textuelles et ne contient aucune formule. Cependant, il arrive parfois que les fichiers CSV contiennent également des formules. Ces fichiers CSV doivent être chargés en définissant le[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) comme *vrai**. Une fois que cette propriété sera définie sur *true**, Aspose.Cells ne traitera pas la formule comme un simple texte. Ils seront traités comme des formules et le moteur de calcul de formule Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

 Le code suivant illustre comment charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n’importe quel fichier CSV. À des fins d'illustration, nous utilisons le[fichier csv simple](5115034.csv)qui contient ces données. Comme vous le voyez, il contient une formule.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Le code charge d'abord le fichier CSV, puis l'importe à nouveau dans la cellule D4. Enfin, il enregistre l'objet classeur au format XSLX. Le[sortie du fichier XLSX](5115052.xlsx) ressemble à ça. Comme vous le voyez, les cellules C3 et F4 contiennent la formule et son résultat 800.

|![tâche : image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

