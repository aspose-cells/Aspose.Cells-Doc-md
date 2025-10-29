---
title: Charger ou importer un fichier CSV avec des formules
type: docs
weight: 350
url: /fr/python-net/load-or-import-csv-file-with-formulas/
description: Charger ou importer un fichier CSV avec des formules en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Charger ou importer un fichier CSV avec des formules en Python, Convertir un CSV avec des formules en Excel en Python via NET, Convertir un CSV avec des formules en xlsx en Python, Charger un CSV avec des formules dans un fichier Excel.
---

{{% alert color="primary" %}} 

Le fichier CSV contient principalement des données textuelles et ne contient pas de formules. Cependant, il arrive parfois que les fichiers CSV contiennent également des formules. De tels fichiers CSV doivent être chargés en définissant la [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) comme **true**. Une fois que cette propriété sera définie sur **true**, Aspose.Cells ne traitera pas les formules comme du simple texte. Elles seront traitées comme des formules et le moteur de calcul de formules Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

Le code suivant illustre comment vous pouvez charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À des fins d'illustration, nous utilisons le [fichier CSV simple](5115034.csv) qui contient ces données. Comme vous pouvez le constater, il contient une formule.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Le code charge d'abord le fichier CSV, puis l'importe à nouveau dans la cellule D4. Enfin, il enregistre l'objet classeur au format XSLX. Le [fichier XLSX de sortie](5115052.xlsx) ressemble à ceci. Comme vous pouvez le constater, la cellule C3 et F4 contiennent une formule et son résultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
