---
title: Modifications de l API publique dans Aspose.Cells 8.5.0
type: docs
weight: 170
url: /fr/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.4.2 à la version 8.5.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [les classes ajoutées etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-5-0/), mais aussi une description des éventuels changements de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Changé les paramètres de la méthode ICustomFunction.CalculateCustomFunction**
Si un paramètre pour la fonction personnalisée est une référence de cellule, dans les anciennes versions des API Aspose.Cells, la référence de cellule était convertie en une valeur de cellule unique ou un tableau d'objets de toutes les valeurs des cellules dans la zone référencée. Cependant, pour de nombreuses fonctions et utilisateurs, le tableau de valeurs de cellules pour toutes les cellules dans la zone référencée n'est pas nécessaire, ils ont juste besoin d'une seule cellule correspondant à la position de la formule, ou juste de la référence elle-même au lieu de la valeur de cellule ou du tableau de valeurs. Pour certaines situations, récupérer toutes les valeurs de cellules a même augmenté le risque d'erreur de référence circulaire.

Pour répondre à ce type de besoin, le Aspose.Cells for Java 8.5.0 a changé la valeur du paramètre en "paramsList" pour la zone référencée. Depuis la version 8.5.0, l'API place simplement l'objet ReferredArea dans le "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement ReferredArea. Si vous avez besoin d'obtenir une seule valeur de cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.getValue(rowOffset, int colOffset). Si vous avez besoin du tableau de valeurs de cellules pour toute la zone, vous pouvez utiliser la méthode ReferredArea.getValues.

Maintenant, étant donné que le Aspose.Cells for Java 8.5.0 donne ReferredArea dans "paramsList", la ReferredAreaCollection dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, elle ne pouvait pas donner une correspondance un-à-un avec les paramètres de la fonction personnalisée), cette version l'a donc également supprimée de "contextObjects" maintenant.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Le Aspose.Cells for Java 8.5.0 a exposé la classe CalculationOptions pour ajouter plus de flexibilité et d'extensibilité au moteur de calcul des formules. La classe nouvellement ajoutée a les propriétés suivantes. 

1. CalculationOptions.CalcStackSize : Spécifie la taille de la pile pour calculer les cellules de manière récursive. -1 spécifie que le calcul utilisera WorkbookSettings.CalcStackSize du classeur correspondant.
1. CalculationOptions.CustomFunction : Étend le moteur de calcul des formules avec une formule personnalisée.
1. CalculationOptions.IgnoreError : Valeur de type booléen indique si les erreurs doivent être masquées lors du calcul des formules, où les erreurs peuvent être dues à la fonction non supportée, au lien externe ou plus encore.
1. CalculationOptions.PrecisionStrategy : Valeur de type CalculationPrecisionStrategy qui spécifie la stratégie de traitement de la précision du calcul.
### **Énumération CalculationPrecisionStrategy ajoutée**
Le Aspose.Cells for Java 8.5.0 a exposé l'énumération CalculationPrecisionStrategy pour ajouter plus de flexibilité au moteur de calcul des formules pour obtenir les résultats souhaités. Cette énumération permet de définir la précision du calcul. En raison du problème de précision de l'arithmétique en virgule flottante IEEE 754, certaines formules en apparence simples peuvent ne pas être calculées pour donner les résultats attendus, par conséquent, la dernière version de l'API a exposé les champs suivants pour obtenir les résultats souhaités selon la sélection.

1. CalculationPrecisionStrategy.DECIMAL : Utilise les décimales comme opérande lorsque c'est possible, et est le plus inefficace du point de vue des performances.
1. CalculationPrecisionStrategy.ROUND: Arrondit les résultats du calcul selon le nombre de chiffres significatifs.
1. CalculationPrecisionStrategy.NONE : Aucune stratégie n'est appliquée donc pendant le calcul, le moteur utilise la valeur double d'origine comme opérande et retourne directement le résultat. Cette option est la plus efficace et est applicable pour la plupart des cas.
### **Méthodes ajoutées pour utiliser CalculationOptions**
Avec la version 8.5.0, l'API Aspose.Cells a ajouté des versions de surcharge de la méthode calculateFormula comme indiqué ci-dessous.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Champ d'énumération PasteType.ROW_HEIGHTS ajouté**
Les APIs Aspose.Cells ont fourni le champ d'énumération PasteType.ROW_HEIGHTS dans le but de copier les hauteurs de ligne lors de la copie des plages. En définissant la propriété PasteOptions.PasteType sur ((PasteType.ROW_HEIGHTS)), les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Propriété SheetRender.PageScale ajoutée**
Lorsque vous définissez l'échelle de la mise en page à l'aide de l'option **Ajuster à n page(s) de large sur m de haut**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Il est possible d'atteindre le même résultat en utilisant la propriété SheetRender.PageScale exposée par Aspose.Cells for Java 8.5.0. Cette propriéte retourne une valeur double qui peut être convertie en pourcentage. Par exemple, si elle retourne 0,507968245, cela signifie que le facteur d'échelle est de 51%.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Champ d'énumération CellValueFormatStrategy ajouté**
Aspose.Cells for Java 8.5.0 a ajouté un nouvelle énumération CellValueFormatStrategy pour gérer les situations où les valeurs des cellules doivent être extraites avec ou sans format appliqué. L'énumération CellValueFormatStrategy comprend les champs suivants. 

1. CellValueFormatStrategy.CELL_STYLE: Uniquement formaté avec le format d'origine de la cellule.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formaté avec le style d'affichage de la cellule.
1. CellValueFormatStrategy.NONE: Non formaté.
### **Méthode Cell.getStringValue ajoutée**
Afin d'utiliser l'énumération CellValueFormatStrategy, v8.5.0 a exposé la méthode Cell.getStringValue qui peut accepter un paramètre de type CellValueFormatStrategy et renvoie la valeur en fonction de l'option spécifiée.

Le code suivant montre comment utiliser la méthode Cells.getStringValue nouvellement exposée.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
