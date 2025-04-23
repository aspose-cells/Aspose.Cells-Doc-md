---
title: Öffentliche API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 370
url: /de/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 16.12.0 auf 17.1.0, die für Modulentwickler/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Excel 2016 Diagramme**
Aspose.Cells APIs haben die Unterstützung für einige Excel 2016 Diagramme hinzugefügt, indem sie die ChartType-Enumeration verbessert haben. Mit der Veröffentlichung von Aspose.Cells 17.1.0 wurden folgende neue Felder hinzugefügt.

- ChartType.BoxWhisker: Die Serie ist als Box und Whisker angeordnet.
- ChartType.Funnel: Die Serie ist als Trichter angeordnet.
- ChartType.ParetoLine: Die Serie ist als Pareto-Linien angeordnet.
- ChartType.Sunburst: Die Serie ist als Sunburst angeordnet.
- ChartType.Treemap: Die Serie ist als TreeMap angeordnet.
- ChartType.Waterfall: Die Serie ist als Wasserfall angeordnet.
- ChartType.Histogram: Die Serie ist als Histogramm angeordnet.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Lesen von Excel 2016 Diagrammtypen](/cells/de/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Hinzugefügter Setter für LoadFilter.LoadDataFilterOptions Eigenschaft**
Aspose.Cells 17.1.0 hat einen Setter für die LoadFilter.LoadDataFilterOptions-Eigenschaft hinzugefügt, um die Instanzvariable m_LoadDataFilterOptions zu ersetzen. Benutzer können die LoadDataFilterOptions-Eigenschaft in ihrer eigenen Implementierung der LoadFilter-Klasse ändern, um das Ladeverhalten von Vorlagendateien zu ändern.

Hier ist ein einfaches Anwendungsbeispiel.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Benutzerdefinierter Vorlagenfilterung](/cells/de/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte CellsHelper.SignificantDigits Eigenschaft**
Aspose.Cells 17.1.0 hat die SignificantDigits-Eigenschaft aus der CellsHelper-Klasse freigelegt, die es erlaubt, die Anzahl der signifikanten Stellen für numerische Werte in einer Tabellenkalkulation zu erhalten oder festzulegen. Der Standardwert der CellsHelper.SignificantDigits-Eigenschaft beträgt 17 und ist nur anwendbar, wenn das Ergebnis im XLSX-Dateiformat gespeichert werden soll.

Hier ist ein einfaches Szenario zur Demonstration der Verwendung der CellsHelper.SignificantDigits-Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zur [Festlegung der Anzahl von signifikanten Stellen](/cells/de/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Hinzugefügtes GlowEffect.Color-Eigenschaft**
Aspose.Cells 17.1.0 hat die GlowEffect.Color-Eigenschaft hinzugefügt, die zur Abrufung der Farbe des Leuchteffekts verwendet werden kann.

Der folgende Ausschnitt verwendet die GlowEffect.Color-Eigenschaft.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Lesen der Glanzfarbe der Form](/cells/de/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte PaperWidth- & PaperHeight-Eigenschaften für PageSetup**
Aspose.Cells 17.1.0 hat die PaperWidth- und PaperHeight-Eigenschaften für die PageSetup-Klasse freigegeben. Die PaperWidth- und PaperHeight-Eigenschaften von PageSetup sind vom Typ double und repräsentieren die Papierbreite und -höhe in Zoll, unter Berücksichtigung der Seitenorientierung.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zu [Abrufen der Papiergröße des Arbeitsblatts](/cells/de/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Hinzugefügtes CheckCustomNumberFormat-Eigenschaft für WorkbookSettings**
Aspose.Cells 17.1.0 hat die CheckCustomNumberFormat-Eigenschaft für die WorkbookSettings-Klasse hinzugefügt. Die CheckCustomNumberFormat ist nützlich, um zu überprüfen, ob die Style.Custom-Eigenschaft ordnungsgemäß festgelegt wurde oder nicht. Falls die Style.Custom-Eigenschaft auf unkorrekte Weise festgelegt wurde, d.h. der Wert nicht dem gültigen Muster entspricht, werden die Aspose.Cells-APIs eine CellsException mit entsprechender Meldung auslösen.

{{% alert color="primary" %}} 

Überprüfen Sie den ausführlichen Artikel zur [Überprüfung des benutzerdefinierten Formats](/cells/de/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügtes DisplayUnitType.Percentage Feld**
Aspose.Cells 17.1.0 hat auch das Percentage Feld der DisplayUnitType Enumeration freigegeben. Das DisplayUnitType.Percentage Feld gibt an, dass die Werte im Diagramm durch 0,01 geteilt werden sollen.
## **Entfernte APIs**
### **Instanzvariable m_LoadDataFilterOptions wurde entfernt**
In diesem Release wurde die Instanzvariable m_LoadDataFilterOptions entfernt. Es wird empfohlen, stattdessen die LoadFilter.LoadDataFilterOptions-Eigenschaft zu verwenden.
{{< app/cells/assistant language="csharp" >}}
