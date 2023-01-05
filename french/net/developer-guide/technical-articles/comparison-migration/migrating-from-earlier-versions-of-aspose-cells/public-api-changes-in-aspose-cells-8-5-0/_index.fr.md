---
title: Public API Changements dans Aspose.Cells 8.5.0
type: docs
weight: 160
url: /fr/net/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.4.2 à 8.5.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-5-0/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Modification des paramètres ICustomFunction.CalculateCustomFunction**
Si un paramètre de la fonction personnalisée est la référence de cellule, dans l'ancienne version Aspose.Cells, les API sont utilisées pour convertir la référence de cellule en une valeur de cellule ou en un tableau d'objets de toutes les valeurs de cellule dans la zone référencée. Cependant, pour de nombreuses fonctions et utilisateurs, le tableau de valeurs de cellule pour toutes les cellules de la zone référencée n'est pas requis, ils n'ont besoin que d'une seule cellule correspondant à la position de la formule, ou ont simplement besoin de la référence elle-même au lieu de la valeur de cellule ou du tableau de valeurs. . Dans certaines situations, la récupération de toutes les valeurs de cellule a même augmenté le risque d'erreur de référence circulaire.

Pour prendre en charge ce type d'exigence, Aspose.Cells for .NET 8.5.0 a remplacé la valeur du paramètre par "paramsList" pour la zone référencée. Depuis la v8.5.0, le API place simplement l'objet ReferredArea dans la "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement la ReferredArea. Si vous avez besoin d'obtenir une seule valeur de cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.GetValue(rowOffset, int colOffset). Si vous avez besoin d'un tableau de valeurs de cellule pour toute la zone, vous pouvez utiliser la méthode ReferredArea.GetValues.

Maintenant que Aspose.Cells for .NET 8.5.0 donne le ReferredArea dans "paramsList", le ReferredAreaCollection dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, il ne pouvait pas toujours donner une carte un à un aux paramètres de la fonction personnalisée), donc cette version l'a également supprimé de "contextObjects" maintenant.

Cette modification nécessite un peu de modifications du code de l'implémentation de ICustomFunction lorsque vous avez besoin de la valeur/des valeurs du paramètre de référence.

**Ancienne implémentation**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Nouvelle implémentation**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Options de calcul de classe ajoutées**
Aspose.Cells for .NET 8.5.0 a exposé la classe CalculationOptions pour ajouter plus de flexibilité et d'extensibilité au moteur de calcul de formule. La classe nouvellement ajoutée a les propriétés suivantes.

1. CalculationOptions.CalcStackSize : spécifié la taille de la pile pour le calcul récursif des cellules. -1 spécifie que le calcul utilisera le WorkbookSettings.CalcStackSize du classeur correspondant.
1. CalculationOptions.CustomFunction : étend le moteur de calcul de formule avec une formule personnalisée.
1. CalculationOptions.IgnoreError : la valeur de type booléen indique si les erreurs doivent être masquées lors du calcul des formules, où les erreurs peuvent être dues à la fonction non prise en charge, au lien externe ou plus.
1. CalculationOptions.PrecisionStrategy : valeur de type CalculationPrecisionStrategy qui spécifie la stratégie de traitement de la précision du calcul.
### **Enumeration CalculationPrecisionStrategy Ajouté**
Aspose.Cells for .NET 8.5.0 a exposé l'énumération CalculationPrecisionStrategy pour ajouter plus de flexibilité au moteur de calcul de formule pour obtenir les résultats souhaités. Cette énumération stratégie la gestion de la précision des calculs. En raison du problème de précision de l'arithmétique à virgule flottante IEEE 754, certaines formules apparemment simples peuvent ne pas être calculées pour donner les résultats attendus. Par conséquent, la dernière version API a exposé les champs suivants pour obtenir les résultats souhaités en fonction de la sélection.

1. CalculationPrecisionStrategy.Decimal : utilise la décimale comme opérande dans la mesure du possible, et est le plus inefficace du point de vue des performances.
1. CalculationPrecisionStrategy.Round : arrondit les résultats du calcul en fonction du chiffre significatif.
1. CalculationPrecisionStrategy.None : aucune stratégie n'est appliquée. Par conséquent, lors du calcul, le moteur utilise la valeur double d'origine comme opérande et renvoie directement le résultat. Cette option est la plus efficace et s'applique à la plupart des cas.
### **Méthodes ajoutées pour utiliser CalculationOptions**
Avec la version v8.5.0, le Aspose.Cells API a ajouté des versions de surcharge de la méthode CalculateFormula comme indiqué ci-dessous.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula (options CalculOptions, booléen récursif)
- Cell.Calculer(OptionsCalcul)
### **Champ d'énumération PasteType.RowHeights ajouté**
Aspose.Cells Les API ont fourni le champ d'énumération PasteType.RowHeights dans le but de copier les hauteurs de ligne tout en copiant les plages. Lors de la définition de la propriété PasteOptions.PasteType sur ((PasteType.RowHeights}}, les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Feuille de propriétésRender.PageScale ajoutée**
Lorsque vous définissez la mise à l'échelle de la mise en page à l'aide de**Ajuster à n page(s) de large par m de haut** option, Microsoft Excel calcule le facteur de mise à l'échelle de la mise en page. La même chose peut être obtenue en utilisant la propriété SheetRender.PageScale exposée par Aspose.Cells for .NET 8.5.0. Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, s'il renvoie 0,507968245, cela signifie que le facteur d'échelle est de 51 %.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Énumération CellValueFormatStrategy ajoutée**
Aspose.Cells for .NET 8.5.0 a ajouté une nouvelle énumération CellValueFormatStrategy pour gérer les situations où les valeurs de cellule doivent être extraites avec ou sans mise en forme appliquée. L'énumération CellValueFormatStrategy a les champs suivants.

1. CellValueFormatStrategy.CellStyle : formaté uniquement avec le format d'origine de la cellule.
1. CellValueFormatStrategy.DisplayStyle : mis en forme avec le style d'affichage de la cellule.
1. CellValueFormatStrategy.None : non formaté.
### **Méthode Cell.GetStingValue ajoutée**
Afin d'utiliser l'énumération CellValueFormatStrategy, la v8.5.0 a exposé la méthode Cell.GetStingValue qui peut accepter un paramètre de type CellValueFormatStrategy et renvoie la valeur dépend de l'option spécifiée.

L'extrait de code suivant montre comment utiliser la méthode Cells.GetStingValue nouvellement exposée.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Propriété ExportTableOptions.FormatStrategy ajoutée**
Aspose.Cells for .NET 8.5.0 a exposé la propriété ExportTableOptions.FormatStrategy pour les utilisateurs qui souhaitent exporter les données vers DataTable avec ou sans formatage. Cette propriété utilise l'énumération CellValueFormatStrategy et exporte les données selon l'option spécifiée.

Le code suivant explique l'utilisation de la propriété ExportTableOptions.FormatStrategy.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
