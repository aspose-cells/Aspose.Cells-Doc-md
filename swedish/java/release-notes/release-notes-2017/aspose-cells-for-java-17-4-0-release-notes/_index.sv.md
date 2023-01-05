---
title: Aspose.Cells for Java 17.4.0 Release Notes
type: docs
weight: 90
url: /sv/java/aspose-cells-for-java-17-4-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.4.0/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41975|Stöd DBNum-formatering (anpassat mönster).|Ny funktion|
|CELLSJAVA-42237|Åtkomst till cellen skapar HTML med tomma rader|Förbättring|
|CELLSJAVA-42236|Prestandaproblem med multi-threading-miljö|Förbättring|
|CELLSJAVA-42226|Begränsa till en mapp och dess undermappar för att använda teckensnitt för att rendera bilder/PDF|Förbättring|
|CELLSJAVA-42239|Inmatningssträngformatfel vid laddning av en HTML|Insekt|
|CELLSJAVA-42230|Ett ytterligare align-attribut genereras vid konvertering av XLSX till HTML|Insekt|
|CELLSJAVA-42229|Exportera XLSX till HTML - Hash-symboler genereras i stället för faktiska Cell-värden|Insekt|
|CELLSJAVA-42218|HTML är inte korrekt konverterad till Excel-fil|Insekt|
|CELLSJAVA-42210|En del av DataBars villkorliga formatering saknas i utgången HTML|Insekt|
|CELLSJAVA-41783|Bakgrundsbilden ska vara i formatet SVG men den är i formatet PNG|Insekt|
|CELLSJAVA-42253|Beroende cellvärde orsakar ett fel i XLS|Insekt|
|CELLSJAVA-42222|Summan är inte korrekt efter beräkning av arbetsboken|Insekt|
|CELLSJAVA-42254|GridWebServlet?acw_ajax_samtalsfel uppstår när GridWeb laddas|Insekt|
|CELLSJAVA-42243|Excel till PDF - Square ser ut som rektangel|Insekt|
|CELLSJAVA-42242|Excel till PDF - Cirkel ser ut som Oval Shape|Insekt|
|CELLSJAVA-42227|Bildfilen "x1.png" har en extra övre kant och saknad nedre kant|Insekt|
|CELLSJAVA-42212|Prestandaproblem vid export av en XLS till PDF|Insekt|
|CELLSJAVA-42246|Excel till HTML - Textjusteringen i diagrammets Y-axeletikett är fel|Insekt|
|CELLSJAVA-42223|Radardiagrammets poäng xy px returnerar 0|Insekt|
|CELLSJAVA-42216|Bundna värden för bubbeldiagrammets Y-axel ändras när AxisScalingValuesIssue-2.xlsx konverteras till PDF|Insekt|
|CELLSJAVA-42250|Kompileringsfel om koden innehåller definition av variabel med typen CommandBar|Insekt|
|CELLSJAVA-42241|Excel till PDF - parenteser kommer på nästa rad|Insekt|
|CELLSJAVA-42234|Att spara XLSM-filen som XLS tar bort makroåtgärder från knappen|Insekt|
|CELLSJAVA-42233|Uppgradera koden - Tillämpa 3D-format på diagram|Insekt|
|CELLSJAVA-42225|Det gick inte att ställa in Shape Input Range|Insekt|
|CELLSJAVA-42224|Problem med sortering Kommentarer|Insekt|
|CELLSJAVA-42221|Kritisk regression med anpassade kontroller|Insekt|
|CELLSJAVA-42220|Problem med inställning av sidlayoutvy för XLSB-filer|Insekt|
|CELLSJAVA-42217|Efter åtkomst till VbaModule via Aspose API har den resulterande Excel-filen brutit vba-projektet|Insekt|
|CELLSJAVA-42213|Teckensnittet ändrar oavsiktligt sin storlek i kommentaren med en CR inbäddad i den|Insekt|
|CELLSJAVA-42231|Undantag förekommer vid infogning av rader|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till metoden VbaProject.Protect (bool islockedForViewing, stränglösenord).**
Skyddar eller avskyddar VBA-projektet.
### **Lägger till egenskapen VbaProject.IsProtected**
Indikerar om vba-projektet är skyddat.
### **Lägger till egenskapen VbaProject.IslockedForViewing**
Indikerar om VBA-projektet är låst för visning.
### **Lägger till egenskapen CopyOptions.ExtendToAdjacentRange**
Anger om intervallet utökas när intervallet kopieras till intilliggande intervall.

{{< highlight "java" >}}

 Workbook wb = new Workbook("sample.xlsx");

Worksheet ws = wb.getWorksheets().get("Sheet1");

CopyOptions co = new CopyOptions();

co.setExtendToAdjacentRange(true);

Cells cells = ws.getCells();

cells.copyRows(cells, 0, 1, 1, co);

{{< /highlight >}}
### **Tar bort föråldrad Workbook.ValidateFormula(strängformel)-metod**
### **Lägger till egenskapen DataSorter.SortAsNumber**
Anger om något som ser ut som ett nummer sorteras.
### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Ange sorteringsvarning vid sortering av data](/cells/sv/java/specifying-sort-warning-while-sorting-data/)
- [Lösenordsskydda VBA Project of Excel Workbook](/cells/sv/java/password-protect-the-vba-project-of-excel-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/java/find-out-if-vba-project-is-protected/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/java/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Ange DBNum anpassad mönsterformatering](/cells/sv/java/specifying-dbnum-custom-pattern-formatting/)
