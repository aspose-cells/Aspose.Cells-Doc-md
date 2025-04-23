---
title: Modifications de l API publique dans Aspose.Cells 8.5.0
type: docs
weight: 160
url: /fr/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.4.2 à la version 8.5.0 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-5-0/), mais aussi une description de tous les changements de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Changé les paramètres de la méthode ICustomFunction.CalculateCustomFunction**
Si un paramètre pour la fonction personnalisée est une référence de cellule, dans les anciennes versions des API Aspose.Cells, la référence de cellule était convertie en une valeur de cellule unique ou un tableau d'objets de toutes les valeurs des cellules dans la zone référencée. Cependant, pour de nombreuses fonctions et utilisateurs, le tableau de valeurs de cellules pour toutes les cellules dans la zone référencée n'est pas nécessaire, ils ont juste besoin d'une seule cellule correspondant à la position de la formule, ou juste de la référence elle-même au lieu de la valeur de cellule ou du tableau de valeurs. Pour certaines situations, récupérer toutes les valeurs de cellules a même augmenté le risque d'erreur de référence circulaire.

Pour répondre à ce type de besoins, Aspose.Cells for .NET 8.5.0 a modifié la valeur du paramètre en "paramsList" pour la zone référencée. Depuis la version 8.5.0, l'API place simplement l'objet ReferredArea dans "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement ReferredArea. Si vous avez besoin d'obtenir une seule valeur de cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.GetValue(rowOffset, int colOffset). Si vous avez besoin d'un tableau de valeurs de cellule pour toute la zone, vous pouvez utiliser la méthode ReferredArea.GetValues.

Maintenant, comme Aspose.Cells for .NET 8.5.0 donne ReferredArea dans "paramsList", la ReferredAreaCollection dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, elle ne pouvait pas toujours donner une correspondance un à un avec les paramètres de la fonction personnalisée), donc cette version l'a également supprimée de "contextObjects" maintenant.

Ce changement nécessite des modifications du code de l'implémentation pour ICustomFunction un peu lorsque vous avez besoin de la valeur/des valeurs du paramètre de référence.

**Ancienne implémentation**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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


### **Classe CalculationOptions ajoutée**
Aspose.Cells for .NET 8.5.0 a exposé la classe CalculationOptions pour ajouter plus de flexibilité et d'extensibilité au moteur de calcul de formule. La nouvelle classe ajoutée a les propriétés suivantes.

1. CalculationOptions.CalcStackSize : Spécifie la taille de la pile pour calculer les cellules de manière récursive. -1 spécifie que le calcul utilisera WorkbookSettings.CalcStackSize du classeur correspondant.
1. CalculationOptions.CustomFunction : Étend le moteur de calcul des formules avec une formule personnalisée.
1. CalculationOptions.IgnoreError : Valeur de type booléen indique si les erreurs doivent être masquées lors du calcul des formules, où les erreurs peuvent être dues à la fonction non supportée, au lien externe ou plus encore.
1. CalculationOptions.PrecisionStrategy : Valeur de type CalculationPrecisionStrategy qui spécifie la stratégie de traitement de la précision du calcul.
### **Énumération CalculationPrecisionStrategy ajoutée**
Aspose.Cells for .NET 8.5.0 a exposé l'énumération CalculationPrecisionStrategy pour ajouter plus de flexibilité au moteur de calcul de formule pour obtenir les résultats souhaités. Cette énumération stratégise la gestion de la précision du calcul. En raison du problème de précision de l'arithmétique en virgule flottante IEEE 754, certaines formules en apparence simples peuvent ne pas être calculées pour donner les résultats escomptés, c'est pourquoi la dernière version de l'API a exposé les champs suivants pour obtenir les résultats souhaités selon la sélection.

1. CalculationPrecisionStrategy.Decimal: Utilise un entier là où c'est possible et est le plus inefficace d'un point de vue des performances.
1. CalculationPrecisionStrategy.Round: Arrondit les résultats du calcul en fonction du chiffre significatif.
1. CalculationPrecisionStrategy.None: Aucune stratégie n'est appliquée donc lors du calcul, le moteur utilise la valeur réelle en double comme opérande et retourne le résultat directement. Cette option est la plus efficace et est applicable pour la plupart des cas.
### **Méthodes ajoutées pour utiliser CalculationOptions**
Avec la sortie de la version 8.5.0, l'API Aspose.Cells a ajouté des versions surchargées de la méthode CalculateFormula comme indiqué ci-dessous.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Champ d'énumération PasteType.RowHeights ajouté**
Les API Aspose.Cells ont fourni le champ d'énumération PasteType.RowHeights dans le but de copier les hauteurs de ligne lors de la copie des plages. En définissant la propriété PasteOptions.PasteType sur PasteType.RowHeights, les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées vers la plage de destination.

**C#**

{{< highlight csharp >}}

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


### **Propriété SheetRender.PageScale ajoutée**
Lorsque vous définissez la mise en page de l'échelle en utilisant l'option **Ajuster à n page(s) de largeur sur m de hauteur**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Il est possible d'atteindre le même résultat en utilisant la propriété SheetRender.PageScale exposée par Aspose.Cells for .NET 8.5.0. Cette propriété renvoie une valeur de type double qui peut être convertie en pourcentage. Par exemple, si elle renvoie 0.507968245, cela signifie que le facteur d'échelle est de 51%.

**C#**

{{< highlight csharp >}}

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


### **Champ d'énumération CellValueFormatStrategy ajouté**
Aspose.Cells for .NET 8.5.0 a ajouté une nouvelle énumération CellValueFormatStrategy pour gérer les situations où les valeurs de cellules doivent être extraites avec ou sans formatage appliqué. L'énumération CellValueFormatStrategy a les champs suivants.

1. CellValueFormatStrategy.CellStyle : Uniquement formaté avec le format original de la cellule.
1. CellValueFormatStrategy.DisplayStyle : Formaté avec le style affiché de la cellule.
1. CellValueFormatStrategy.None : Non formaté.
### **Méthode Cell.GetStingValue ajoutée**
Pour utiliser l'énumération CellValueFormatStrategy, la version 8.5.0 a exposé la méthode Cell.GetStingValue qui peut accepter un paramètre de type CellValueFormatStrategy et retourne la valeur en fonction de l'option spécifiée.

Le snippet de code suivant montre comment utiliser la méthode nouvellement exposée Cells.GetStingValue.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.5.0 a exposé la propriété ExportTableOptions.FormatStrategy pour les utilisateurs qui souhaitent exporter les données vers DataTable avec ou sans mise en forme. Cette propriété utilise l'énumération CellValueFormatStrategy et exporte les données selon l'option spécifiée.

Le code suivant explique l'utilisation de la propriété ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
