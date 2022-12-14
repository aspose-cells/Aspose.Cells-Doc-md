---
title: Öffentlich API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 370
url: /de/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.12.0 zu 17.1.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Excel 2016-Diagramme**
Aspose.Cells APIs haben die Unterstützung für einige Excel 2016-Diagramme hinzugefügt, indem sie die ChartType-Enumeration erweitert haben. Die folgenden neuen Felder wurden mit der Veröffentlichung von Aspose.Cells 17.1.0 hinzugefügt.

- ChartType.BoxWhisker: Die Reihe ist als Box und Whisker angelegt.
- ChartType.Funnel: Die Reihe ist als Trichter angelegt.
- ChartType.ParetoLine: Die Reihe wird als Pareto-Linien angelegt.
- ChartType.Sunburst: Die Reihe wird als Sunburst angelegt.
- ChartType.Treemap: Die Serie wird als Treemap angelegt.
- ChartType.Waterfall: Die Reihe wird als Wasserfall angelegt.
- ChartType.Histogram: Die Reihe wird als Histogramm angelegt.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Diagrammtypen in Excel 2016 lesen](/cells/de/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Setter für LoadFilter.LoadDataFilterOptions-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat Setter für die Eigenschaft LoadFilter.LoadDataFilterOptions hinzugefügt, um die Instanzvariable m_LoadDataFilterOptions zu ersetzen. Benutzer können die LoadDataFilterOptions-Eigenschaft in ihrer eigenen Implementierung der LoadFilter-Klasse ändern, um das Verhalten beim Laden von Vorlagendateien zu ändern.

Hier ist ein einfaches Anwendungsszenario.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Benutzerdefinierte Vorlagenfilterung](/cells/de/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **CellsHelper.SignificantDigits-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die SignificantDigits-Eigenschaft der CellsHelper-Klasse verfügbar gemacht, die es ermöglicht, die Anzahl signifikanter Stellen für numerische Werte in einer Tabelle abzurufen oder festzulegen. Der Standardwert der Eigenschaft CellsHelper.SignificantDigits ist 17, wobei er nur anwendbar ist, wenn das Ergebnis im XLSX-Dateiformat gespeichert werden muss.

Hier ist ein einfaches Szenario, um die Verwendung der Eigenschaft CellsHelper.SignificantDigits zu demonstrieren.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Einstellen der Anzahl signifikanter Stellen](/cells/de/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **GlowEffect.Color-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die Eigenschaft GlowEffect.Color hinzugefügt, die verwendet werden kann, um die Farbe des Glüheffekts abzurufen.

Das folgende Snippet verwendet die GlowEffect.Color-Eigenschaft.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Lesen der Leuchtfarbe der Form](/cells/de/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **PageSetup.PaperWidth- und PaperHeight-Eigenschaften hinzugefügt**
Aspose.Cells 17.1.0 hat die PaperWidth- und PaperHeight-Eigenschaften für die PageSetup-Klasse verfügbar gemacht. Die Eigenschaften PageSetup.PaperWidth und PageSetup.PaperHeight sind vom Typ Double und repräsentieren die Papierbreite und -höhe in der Einheit Zoll, wobei die Seitenausrichtung berücksichtigt wird.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Abrufen der Papiergröße des Arbeitsblatts](/cells/de/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **WorkbookSettings.CheckCustomNumberFormat-Eigenschaft hinzugefügt**
Aspose.Cells 17.1.0 hat die CheckCustomNumberFormat-Eigenschaft zur WorkbookSettings-Klasse hinzugefügt. Das CheckCustomNumberFormat ist nützlich, um zu überprüfen, ob die Style.Custom-Eigenschaft richtig festgelegt wurde oder nicht. Falls die Style.Custom-Eigenschaft falsch eingestellt wurde, das heißt; Der Wert entspricht keinem gültigen Muster, dann lösen die Aspose.Cells-APIs CellsException mit der entsprechenden Meldung aus.

{{% alert color="primary" %}} 

 Überprüfen Sie den ausführlichen Artikel auf[Überprüfen des benutzerdefinierten Formats](/cells/de/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **DisplayUnitType.Prozentfeld hinzugefügt**
Aspose.Cells 17.1.0 hat auch das Prozentfeld für die DisplayUnitType-Enumeration verfügbar gemacht. Das Feld DisplayUnitType.Percentage gibt an, dass die Werte im Diagramm durch 0,01 dividiert werden sollen.
## **Entfernte APIs**
### **Instanzvariable m_LoadDataFilterOptions entfernt**
In dieser Version wurde die Instanzvariable m_LoadDataFilterOptions entfernt. Es wird empfohlen, stattdessen die Eigenschaft LoadFilter.LoadDataFilterOptions zu verwenden.
