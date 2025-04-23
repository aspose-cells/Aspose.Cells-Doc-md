---
title: Changements dans l API publique dans Aspose.Cells 8.3.2
type: docs
weight: 120
url: /fr/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.3.1 à la 8.3.2 qui pourraient intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-3-2/) et [classes supprimées etc.](/cells/fr/net/public-api-changes-in-aspose-cells-8-3-2/), mais aussi une description de tout changement dans le comportement en coulisses d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme pour définir la position absolue de PivotItem**
Afin de fournir la fonctionnalité [Positionnement absolu de PivotItem](/cells/fr/net/specifying-the-absolute-position-of-the-pivot-item/), le Aspose.Cells for .NET 8.3.2 a exposé une série de propriétés et de méthodes d'aide comme indiqué ci-dessous.

- La propriété PivotItem.Position peut être utilisée pour spécifier l'index de position dans tous les PivotItems quel que soit le nœud parent.
- La propriété PivotItem.PositionInSameParentNode peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- La méthode PivotItem.Move(int count, bool isSameParent) peut être utilisée pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur count, où count est le nombre de positions pour déplacer le PivotItem vers le haut ou vers le bas. Si la valeur count est inférieure à zéro, l'élément sera déplacé vers le haut, tandis que si la valeur count est supérieure à zéro, le PivotItem se déplacera vers le bas, le paramètre isSameParent de type booléen spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.

{{% alert color="primary" %}} 

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.RefreshData et PivotTable.CalculateData avant d'utiliser les propriétés PivotItem.Position, PivotItem.PositionInSameParentNode et la méthode PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Classe SignatureLine ajoutée**
Aspose.Cells for .NET 8.3.2 fournit le support pour la ligne de signature pour imiter la fonctionnalité équivalente de MS Excel. Cette version de Aspose.Cells for .NET a exposé la classe SignatureLine et la propriété Picture.SignatureLine à cette fin.

Le code d'exemple suivant ajoute une ligne de signature à l'aide de la propriété Picture.SignatureLine au classeur.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Méthode Chart.HasAxis ajoutée**
Avec la sortie de la v8.3.2, l'API Aspose.Cells a fourni la méthode Chart.HasAxis(AxisType axisType, bool isPrimary) pour déterminer si le graphique a un axe particulier ou non.

Le code d'exemple suivant démontre l'utilisation de la méthode Chart.HasAxis pour déterminer si le graphique d'exemple a des axes Primary, Secondaire et de valeur.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Méthode WorkbookSettings.CheckWriteProtectedPassword ajoutée**
La méthode WorkbookSettings.CheckWriteProtectedPassword permet aux développeurs de vérifier si un mot de passe donné pour modifier la feuille de calcul est correct ou non.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Méthodes de surcharge WorkbookRender.ToPrinter & SheetRender.ToPrinter ajoutées**
Aspose.Cells for .NET 8.3.2 a fourni les méthodes WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) et SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) pour imprimer la plage de pages du classeur et de la feuille de calcul respectivement.

Le code d'exemple suivant illustre l'utilisation desdites méthodes pour imprimer les pages 2-5 du classeur et de la feuille de calcul.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Méthode Worksheet.RefreshPivotTables ajoutée**
La nouvelle méthode ajoutée Worksheet.RefreshPivotTables permet de rafraîchir tous les tableaux croisés dynamiques dans une feuille de calcul donnée en un seul appel.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Méthode Workbook.GetNamedStyle ajoutée**
L'API Aspose.Cells for .NET a exposé la méthode Workbook.GetNamedStyle qui accepte la chaîne en tant que paramètre et récupère l'objet Style en fonction du paramètre passé.
### **Méthode Cells.ImportTwoDimensionArray ajoutée**
L'API Aspose.Cells for .NET a rendu possible l'importation de tableaux bidimensionnels dans les cellules de feuilles de calcul en exposant la méthode Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Ladite méthode importe un tableau de données bidimensionnel dans une feuille de calcul avec des options plus flexibles définies dans TxtLoadOptions.
### **Propriétés OnePagePerSheet, PageIndex et PageCount ajoutées**
Aspose.Cells for .NET 8.3.2 a exposé les propriétés OnePagePerSheet, PageIndex et PageCount pour la classe XpsSaveOptions. L'utilisateur peut adapter l'ensemble du contenu d'une feuille de calcul sur une seule page de XPS en utilisant la propriété OnePagePerSheet et/ou récupérer le nombre de pages à imprimer en utilisant la propriété PageCount. La propriété PageIndex obtient/définit l'index 0-based de la première page à enregistrer.
### **Propriétés NumberDecimalSeparator & NumberGroupSeparator ajoutées**
Aspose.Cells for .NET 8.3.2 a introduit les propriétés NumberDecimalSeparator et NumberGroupSeparator qui peuvent obtenir/définir les séparateurs personnalisés utilisés pour le formatage et l'analyse des valeurs numériques dans les feuilles de calcul.

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Le code suivant spécifie les séparateurs de décimales et de groupe personnalisés respectivement comme point et espace.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Propriété PdfSaveOptions.IsFontSubstitutionCharGranularity ajoutée**
Aspose.Cells for .NET 8.3.2 a exposé la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity afin de surmonter le problème où certains caractères Unicode ne peuvent pas être affichés à l'aide d'une famille de polices spécifique. Lorsque la propriété PdfSaveOptions.IsFontSubstitutionCharGranularity est définie sur true, seule la police du caractère spécifique qui ne peut pas être affiché sera changée en une police affichable et le reste du mot ou de la phrase devrait rester dans la police d'origine.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **APIs supprimées**
### **Méthodes obsolètes supprimées**
Les méthodes suivantes ont été supprimées de l'API publique.

- Méthodes Workbook.Open & Workbook.Save.
- Méthode Workbook.SetOleSize.
- Méthode Workbook.LoadData.
- Méthodes WorkbookDesigner.Open et WorkbookDesigner.Save.
- Méthode WorksheetCollection.DeleteName.
### **Propriétés obsolètes supprimées**
Les propriétés suivantes ont été supprimées de l'API publique.

- Propriété Workbook.IsProtected.
- Propriété Workbook.Language.
- Propriété Workbook.Region.
- Propriété WorkbookSettings.ReCalcOnOpen.
- Propriété WorkbookSettings.Language.
- Propriété WorkbookSettings.Encoding.
- Propriété WorkbookSettings.ConvertNumericData.
- Propriété WorksheetCollection.HidePivotFieldList.
- Propriété WorksheetCollection.EnableHTTPCompression.
- Propriété WorksheetCollection.IsMinimized.
- Propriété WorksheetCollection.IsHidden.
- Propriété WorksheetCollection.SheetTabBarWidth.
- Propriété WorksheetCollection.WindowLeft.
- Propriété WorksheetCollection.WindowLeftInch.
- Propriété WorksheetCollection.WindowLeftCM.
- Propriété WorksheetCollection.WindowTop.
- Propriété WorksheetCollection.WindowTopInch.
- Propriété WorksheetCollection.WindowTopCM.
- Propriété WorksheetCollection.WindowWidth.
- Propriété WorksheetCollection.WindowWidthInch.
- Propriété WorksheetCollection.WindowWidthCM.
- Propriété WorksheetCollection.WindowHeight.
- Propriété WorksheetCollection.WindowHeightInch.
- Propriété WorksheetCollection.WindowHeightCM.
- Propriété Worksheet.HPageBreaks.
- Propriété Worksheet.VPageBreaks.
- Propriété HtmlSaveOptions.DisplayHTMLCrossString.
- Propriété HtmlSaveOptions.ExportChartImageFormat.
- Propriété SaveOptions.ExpCellNameToXLSX.
- Propriété SaveOptions.DefaultFont.
- Propriété SaveOptions.Compliance.
- propriété SaveOptions.PdfBookmark.
- propriété SaveOptions.PdfImageCompression.
- propriété TxtSaveOptions.AlwaysQuoted.
## **API obsolètes**
### **Propriété obsolète Workbook.SaveOptions**
Un objet SaveOptions doit être passé à la méthode Workbook.Save après avoir défini les propriétés appropriées de SaveOptions.
### **Propriété Workbook.Styles obsolète & Classe StyleCollection**
Il est conseillé d'utiliser la méthode Workbook.CreateStyle pour créer et manipuler le style pour l'instance Workbook au lieu de créer un Style avec la méthode StyleCollection.Add. De plus, la méthode Workbook.GetNamedStyle(string) peut être utilisée pour obtenir un style nommé au lieu de StyleCollection[string].
### **Méthode PivotItem.Move(int count) obsolète**
Avec la version 8.3.2 d'Aspose.Cells, l'API a introduit une surcharge de la méthode PivotItem.Move qui accepte le paramètre entier pour le décompte et le paramètre booléen pour déplacer un PivotItem dans le nœud parent.
{{< app/cells/assistant language="csharp" >}}
