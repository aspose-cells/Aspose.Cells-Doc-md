---
title: Charger ou importer un fichier CSV avec des formules en utilisant C++
linktitle: Charger ou importer un fichier CSV avec des formules
type: docs
weight: 350
url: /fr/go-cpp/load-or-import-csv-file-with-formulas/
description: Charger ou importer un fichier CSV contenant des formules en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}} 

 Les fichiers CSV contiennent principalement des données textuelles et n'incluent généralement pas de formules. Cependant, il existe des cas où des fichiers CSV peuvent contenir des formules. Ces fichiers CSV doivent être chargés en définissant la propriété [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) sur **true**. Une fois cette propriété définie sur **true**, Aspose.Cells ne considérera pas les formules comme du simple texte. Elles seront traitées comme des formules, et le moteur de calcul de formules Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 

Le code suivant illustre comment charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À des fins d'illustration, nous utilisons le [fichier CSV simple](5115034.csv) contenant ces données. Comme vous le voyez, il contient une formule.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Le code charge d'abord le fichier CSV, puis l'importe à nouveau à la cellule D4. Enfin, il enregistre l'objet classeur au format XLSX. Le [fichier XLSX de sortie](5115052.xlsx) ressemble à ceci. Comme vous le voyez, la cellule C3 et F4 contiennent des formules et leur résultat est 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
