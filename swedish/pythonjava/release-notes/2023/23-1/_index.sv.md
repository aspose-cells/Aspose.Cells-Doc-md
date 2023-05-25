---
title: Aspose.Cells for Python via Java 23.1 Release Notes
type: docs
weight: 12
url: /sv/python-java/aspose-cells-for-python-via-java-23-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Python via Java 23.1](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-23.1/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSJAVA-44172|Stöd avbrott vid beräkning av formler för en cell|
|CELLSJAVA-45029|Stöd arkzoom, frys rutor vid export och import av html|
|CELLSJAVA-45034|Hur man kodar/använder filterflaggaalternativet för rad 1|
|CELLSJAVA-45003|XLS till HTML: Rektangelformen är förvrängd|
|CELLSJAVA-45004|XLS till HTML: Bild klippt och flyttad ur sin plats|
|CELLSJAVA-44364|Skillnad i värden mellan en Excel-fil och den konverterade PDF (via Aspose.Cells) filen|
|CELLSJAVA-45026|Dubbla citattecken " från XLSX-filen visas inte i konverterad PDF-fil|
|CELLSJAVA-45035|DATEDIF-funktionen fungerar inte korrekt med skottår|
|CELLSJAVA-45008|Diagramförklaringsobjekt avskurna i utdatabilden|
|CELLSJAVA-45036|Regression: Diagrammets storlek har ändrats felaktigt|
|CELLSJAVA-45017|kan inte byta kalkylblad i java-demoprojektet för filen med lösenord|
|CELLSJAVA-44942|Färger förlorade vid export av ett diagram till EMF|
|CELLSJAVA-45005|Typsnitt med teckensnittets fullständiga namn väljs inte vid konvertering till pdf|
|CELLSJAVA-45033|Kalkylblad till Emf-bild är inte direkt efter inställning av upplösningsalternativ|
|CELLSJAVA-44971|Bilder kan inte visas när html-ström laddas|
|CELLSJAVA-45020|HTML till EXCEL: Stilar ändrade|
|CELLSJAVA-45021|"com.aspose.cells.CellsException: Ogiltig arkreferens för det definierade namnet" när en Excel-fil renderas till PDF|
|CELLSJAVA-45025|ArrayIndexOutOfBoundsException på arbetsbok spara|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till klassen PivotGlobalizationSettings.**

Klassen hanterar alla globaliseringsinställningar om pivottabeller.

###  **Tar bort metoden GlobalizationSettings.GetOtherName().**

Denna metod har inte hänvisats längre, den har ingen effekt även om användaren implementerar den i GlobalizationSettings. Så vi tar bort det nu. Användaren bör använda metoden ChartGlobalizationSettings.GetOtherName() istället.

###  **Tar bort metoderna GlobalizationSettings.GetColumnLablesName()/GetRowLablesName().**

Använd PivotGlobalizationSettings.GetTextOfColumnLabels()/GetTextOfRowLabels().

###  **Föråldrar alla metoder om pivottabeller i GlobalizationSettings.**

Använd motsvarande metoder i PivotGlobalizationSettings.

###  **Lägger till metoden SetStyle() för klassen Row och Column.**

Stöder för att ställa in anpassad stil för hela raden/kolumnen. För att ställa in anpassad stil är skillnaden mellan SetStyle() och ApplyStyle() att SetStyle() inte ändrar stilinställningarna för befintliga celler.

###  **Lägger till HasCustomStyle-egenskapen för Cell, rad- och kolumnklasser.**

Indikerar om cellen, raden eller kolumnen har ställts in med anpassade stilinställningar (till skillnad från den standard som den ärver).

###  **Lägger till egenskapen JsonSaveOptions.AlwaysExportAsJsonObject.**

Anger om Excel-filer alltid exporteras som Json-objekt även om det bara finns ett kalkylblad.

###  **Lägger till klassen RevisionHeader och egenskapen RevisionLog.MetadataTable.**

Stöder att hämta och ställa in egenskaper för revisionslogg.

###  **Lägger till metoden Style.GetTwoColorGradientSetting() och föråldrar metoden Style.GetTwoColorGradient().**

Använd metoden Style.GetTwoColorGradientSetting() istället.

###  **Föråldrat JsonUtility.ExportRangeToJson(Range,ExportRangeToJsonOptions) och lägger till JsonUtility.ExportRangeToJson(Range, JsonSaveOptions)**

Använd metoden ExportRangeToJson(Range, JsonSaveOptions) istället.

###  **Lägger till egenskapen Charts.Axis.CustomUnit.**

Anger ett anpassat värde för visningsenheten.

###  **Föråldrade egenskapen Charts.Axis.CustUnit.**

Använd Charts.Axis.CustomUnit istället.

###  **Lägger till egenskapen Charts.Chart.PlotVisibleCellsOnly.**

Anger om endast synliga celler plottas.

###  **Föråldrade egenskapen Charts.Chart.PlotVisibleCells.**

Använd Charts.Chart.PlotVisibleCellsOnly istället.

###  **Tar bort egenskapen ShapeFormat.FillFormat.**

Använd egenskapen ShapeFormat.Fill istället.

###  **Tar bort egenskapen ShapeFormat.Outline.**

Använd egenskapen ShapeFormat.Line istället.