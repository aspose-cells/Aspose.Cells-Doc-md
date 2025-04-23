---
title: Changements dans l API publique dans Aspose.Cells 8.3.2
type: docs
weight: 130
url: /fr/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.3.1 à la 8.3.2 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-3-2/) et [classes supprimées etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-3-2/), mais aussi une description de toutes les modifications du comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Mécanisme pour définir la position absolue de PivotItem**
Afin de fournir la fonctionnalité [Positionnement Absolu de PivotItem](/cells/fr/java/specifying-the-absolute-position-of-the-pivot-item/), le Aspose.Cells for Java 8.3.2 a exposé une série de propriétés et une méthode comme indiqué ci-dessous.

- PivotItem.setPosition peut être utilisé pour définir l'index de position dans tous les PivotItems indépendamment du nœud parent.
- PivotItem.setPositionInSameParentNode peut être utilisé pour définir l'index de position dans les PivotItems sous le même nœud parent.
- La méthode PivotItem.move(int count, bool isSameParent) peut être utilisée pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du compteur, où le compteur est le nombre de positions à déplacer pour le PivotItem vers le haut ou vers le bas. Si la valeur du compteur est inférieure à zéro, l'élément sera déplacé vers le haut, tandis que si la valeur du compteur est supérieure à zéro, le PivotItem se déplacera vers le bas. Le paramètre de type booléen isSameParent spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.

{{% alert color="primary" %}} 

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.refreshData et PivotTable.calculateData avant d'utiliser les propriétés PivotItem.setPosition, PivotItem.setPositionInSameParentNode et la méthode PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Classe SignatureLine ajoutée**
Aspose.Cells 8.3.2 fournit la prise en charge de la Ligne de Signature pour imiter la fonctionnalité équivalente à MS Excel. Cette version a exposé la classe SignatureLine et la propriété Picture.SignatureLine à cette fin.

Le code d'exemple suivant ajoute une ligne de signature à l'aide de la propriété Picture.SignatureLine au classeur.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Méthode Chart.hasAxis ajoutée**
Avec la version 8.3.2, l'API Aspose.Cells a fourni la méthode Chart.hasAxis(AxisType axisType, bool isPrimary) pour déterminer si le graphique possède un axe particulier ou non.

Le code d'exemple suivant montre l'utilisation de la méthode Chart.hasAxis pour déterminer si le graphique d'exemple possède des axes Principal, Secondaire et de Valeur.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Méthode WorkbookSettings.checkWriteProtectedPassword ajoutée**
La méthode WorkbookSettings.checkWriteProtectedPassword permet aux développeurs de vérifier si un mot de passe donné pour modifier la feuille de calcul est correct ou non.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Méthodes de surcharge WorkbookRender.toPrinter & SheetRender.toPrinter ajoutées**
Aspose.Cells 8.3.2 a fourni les méthodes WorkbookRender.toPrinter (string printerName, int printPageIndex, int printPageCount) et SheetRender.toPrinter (string printerName, int printPageIndex, int printPageCount) pour imprimer la plage de pages du classeur et de la feuille de calcul respectivement.

Le code d'exemple suivant illustre l'utilisation desdites méthodes pour imprimer les pages 2-5 du classeur et de la feuille de calcul.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Méthode Worksheet.refreshPivotTables ajoutée**
La méthode nouvellement ajoutée Worksheet.refreshPivotTables permet de rafraîchir tous les tableaux croisés dynamiques dans une feuille de calcul donnée en un seul appel.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Méthode Workbook.getNamedStyle ajoutée**
Aspose.Cells 8.3.2 a exposé la méthode Workbook.getNamedStyle qui accepte la chaîne en paramètre et récupère l'objet Style en fonction du paramètre passé.
### **Méthode Cells.importTwoDimensionArray ajoutée**
L'API Aspose.Cells a rendu possible l'importation de tableaux bidimensionnels dans des cellules de feuille de calcul en exposant la méthode Cells.importTwoDimensionArray (objet[,], objet[,], int, int, TxtLoadOptions). Ladite méthode importe un tableau de données bidimensionnel dans une feuille de calcul avec des options plus flexibles définies dans TxtLoadOptions.
### **Propriétés OnePagePerSheet, PageIndex et PageCount ajoutées**
Aspose.Cells for Java 8.3.2 a exposé les propriétés OnePagePerSheet, PageIndex & PageCount pour la classe XpsSaveOptions. L'utilisateur peut ajuster tout le contenu d'une feuille de calcul sur une seule page de XPS en utilisant la propriété OnePagePerSheet et/ou récupérer le nombre de pages à imprimer en utilisant la propriété PageCount. La propriété PageIndex obtient/définit l'index à base 0 de la première page à enregistrer.
### **Propriétés NumberDecimalSeparator & NumberGroupSeparator ajoutées**
Aspose.Cells for Java 8.3.2 a introduit les propriétés NumberDecimalSeparator & NumberGroupSeparator qui peuvent obtenir/définir les séparateurs personnalisés utilisés pour formater et parser les valeurs numériques dans les feuilles de calcul.

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Le code suivant spécifie les séparateurs décimaux et de groupe personnalisés en tant que point et espace respectivement.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Propriété PdfSaveOptions.setFontSubstitutionCharGranularity ajoutée**
Aspose.Cells for Java 8.3.2 a exposé la propriété PdfSaveOptions.setFontSubstitutionCharGranularity afin de résoudre le problème où certains caractères Unicode ne peuvent pas être affichés à l'aide d'une police de caractères spécifique. Lorsque la propriété PdfSaveOptions.setFontSubstitutionCharGranularity est définie sur true, seule la police du caractère spécifique qui ne peut pas être affiché sera modifiée en une police affichable et le reste du mot ou de la phrase devrait rester dans la police d'origine.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **APIs supprimées**
### **Méthodes obsolètes supprimées**
Les méthodes suivantes ont été supprimées de l'API publique.

- Méthodes Workbook.open et Workbook.save.
- Méthode Workbook.setOleSize.
- Méthode Workbook.loadData.
- Méthodes WorkbookDesigner.open et WorkbookDesigner.save.
- Méthode WorksheetCollection.deleteName.
### **Propriétés obsolètes supprimées**
Les propriétés suivantes ont été supprimées de l'API publique.

- Propriété Workbook.isProtected.
- Propriété Workbook.Language.
- Propriété Workbook.Region.
- Propriété WorkbookSettings.ReCalcOnOpen.
- Propriété WorkbookSettings.Language.
- Propriété WorkbookSettings.Encoding.
- Propriété WorkbookSettings.ConvertNumericData.
- Propriété WorksheetCollection.HidePivotFieldList.
- Propriété WorksheetCollection.EnableHTTPCompression.
- Propriété WorksheetCollection.isMinimized.
- Propriété WorksheetCollection.isHidden.
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
### **Propriété Workbook.saveOptions obsolète**
Un objet SaveOptions doit être passé à la méthode Workbook.Save après avoir défini les propriétés appropriées de SaveOptions. 
### **Propriété Workbook.Styles & Classe StyleCollection obsolète**
Il est conseillé d'utiliser la méthode Workbook.createStyle pour créer et manipuler un style pour une instance Workbook au lieu de créer un Style avec la méthode StyleCollection.add. De plus, la méthode Workbook.getNamedStyle(string) peut être utilisée pour obtenir un style nommé au lieu de StyleCollection.get(string).
### **Méthode PivotItem.move(int count) obsolète**
Avec la sortie de Aspose.Cells 8.3.2, l'API a introduit une autre surcharge de la méthode PivotItem.move qui accepte le paramètre entier pour le décompte et un paramètre booléen pour déplacer un PivotItem dans le nœud parent. 
{{< app/cells/assistant language="java" >}}
