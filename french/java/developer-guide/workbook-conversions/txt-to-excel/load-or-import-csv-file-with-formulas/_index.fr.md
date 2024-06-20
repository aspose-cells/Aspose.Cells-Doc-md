---
title: Charger ou importer un fichier CSV avec des formules
type: docs
weight: 500
url: /fr/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Le fichier CSV contient principalement des données textuelles et ne contient pas de formules. Cependant, il arrive parfois que les fichiers CSV contiennent également des formules. Ces fichiers CSV doivent être chargés en définissant le [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) à **true**. Une fois que cette propriété est définie sur **true**, Aspose.Cells ne traitera pas la formule comme un simple texte. Elles seront traitées comme des formules et le moteur de calcul de formules Aspose.Cells les traitera comme d'habitude.

{{% /alert %}} 
## **Charger ou importer un fichier CSV avec des formules**
Le code suivant illustre comment vous pouvez charger et importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À des fins d'illustration, nous utilisons le [fichier CSV simple](5472505.csv) qui contient ces données. Comme vous le voyez, il contient une formule.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Le code charge d'abord le fichier CSV, puis l'importe à nouveau dans la cellule D4. Enfin, il enregistre l'objet classeur au format XSLX. Le [fichier XLSX de sortie](5472503.xlsx) ressemble à ceci. Comme vous le voyez, la cellule C3 et F4 contiennent la formule et son résultat 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
