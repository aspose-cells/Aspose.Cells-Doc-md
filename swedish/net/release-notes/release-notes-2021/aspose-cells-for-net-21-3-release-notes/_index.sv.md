---
title: Aspose.Cells for .NET 21.3 Release Notes
type: docs
weight: 28
url: /sv/net/aspose-cells-for-net-21-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.3](https://www.nuget.org/packages/Aspose.Cells/21.3.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47857|Rensar alla sammanslagningsområden på arket|Ny funktion|
|CELLSNET-47892| Signera digitalt Microsoft Signaturrad i Excel-kalkylblad|Förbättring|
|CELLSNET-47905|Implementera sammanfattningsalgoritm av BouncyCastel's API|Förbättring|
|CELLSNET-47838|Inbyggd diagramfärgpalett bevaras inte|Förbättring|
|CELLSNET-47877|Workbook.Settings.RemovePersonalInformation är inte effektiv|Förbättring|
|CELLSNET-47879|Den genererade filen är skadad när du sparar xls-fil med inbäddad word6.0 doc-fil som xlsx.|Förbättring|
|CELLSNET-47893|Konvertera signaturlinje till bild.|Förbättring|
|CELLSNET-47899|Stöd kopiering av QueryTable vid kopiering av arbetsbok.|Förbättring|
|CELLSNET-47842|Långsam prestanda när du uppdaterar ett stort pivotbord|Prestanda|
|CELLSNET-42846|Ekvationen går förlorad när ODS-filen sparas på nytt|Insekt|
|CELLSNET-47794|Storleken och placeringen av pilformen är felaktig|Insekt|
|CELLSNET-46469|Chart.RefreshPivotData() tar bort axelnummerformat|Insekt|
|CELLSNET-47871|Fel rubriker vid rendering av utskriftsområde|Insekt|
|CELLSNET-47875| MS Excel måste reparera filen efter återspara via Aspose.Cells|Insekt|
|CELLSNET-47829| Formelberäkningsresultaten skiljer sig när man implementerar cirkulära referenser och iterationer|Insekt|
|CELLSNET-47865|Aspose.Cells visar felaktigt datum i japanskt format|Insekt|
|CELLSNET-47872|MS Excel visar ett felmeddelande när en återsparad XLTM-fil öppnas med Aspose.Cells|Insekt|
|CELLSNET-47897|Val av listobjekt fungerar inte när det laddas in i ASP.NET-applikationen|Insekt|
|CELLSNET-47862|Excel Accounting Underline skärs av vid export till PDF|Insekt|
|CELLSNET-47881|Kolumnbredden är mindre än förväntat när du importerar/mappar XML-filen till arbetsboken|Insekt|
|CELLSNET-47804|Sjökortsförklaringstext visas inte korrekt|Insekt|
|CELLSNET-47834|Chart.Calculate() i diagram ändrar diagramformateringen|Insekt|
|CELLSNET-47856|XLSX till PDF konverteringsproblem med pivottabeller|Insekt|
|CELLSNET-41275|Diagram som hänvisar till andra blad visas inte|Insekt|
|CELLSNET-42847|Diagrammet går förlorat när ODS-filen sparas på nytt|Insekt|
|CELLSNET-47861|Skillnad i radhöjdsberäkning|Insekt|
|CELLSNET-47876|Autopassning av rader och standardhöjd fungerar inte korrekt för sammanslagna celler|Insekt|
|CELLSNET-47903|Att infoga kolumn i en tabell gör att arbetsboken skadas|Insekt|
|CELLSNET-47906|Problem med InsertCutCells API som påverkar formelreferenser mellan kalkylblad|Insekt|
|CELLSNET-47908|ForceFullCalculation återgår till falskt efter återsparning|Insekt|
|CELLSNET-47909|Att ta bort tomma rader uppdaterar inte kommentarsformerna därefter|Insekt|
|CELLSNET-47913|Shape.UpdateSelectedValue() orsakar felaktig formuppdatering|Insekt|
|CELLSNET-47866|Undantag vid laddning av en HTML|Undantag|
|CELLSNET-47882|Undantag uppstod vid import av html till excel-fil|Undantag|
|CELLSNET-47863|Att lägga till HTML-taggar i cell kastar System.FormatException|Undantag|
|CELLSNET-47868|Ogiltigt undantag för slutradindex vid öppning av Office 2000 XLS-fil|Undantag|
|CELLSNET-47869|Cells Arbetsbokladdningsfel med undantag|Undantag|
|CELLSNET-47870|Undantag uppstod när filen XLS laddades|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen SignatureLine.Id.**

Hämtar eller ställer in identifierare för denna signaturrad.

### **Lägger till egenskapen DigitalSignature.Id.**

Anger en GUID som kan korsreferens med GUID för signaturraden som lagras i dokumentinnehållet.

### **Lägger till egenskapen DigitalSignature.ProviderId.**

Anger klass-ID för signaturleverantören.

### **Lägger till egenskapen DigitalSignature.Image.**

Anger en bild för den digitala signaturen.

### **Lägger till egenskapen DigitalSignature.Text.**

Anger texten för den faktiska signaturen i den digitala signaturen.

### **Lägger till metoden Cells.ClearMergedCells().**

Tar bort alla sammanslagna celler.

### **Lägger till metoden Workbook.RemovePersonalInformation().**

Tar bort all personlig information.

### **Lägger till egenskapen WorkbookSettings.ForceFullCalculate.**

 
Beräknar helt varje gång en beräkning utlöses.

### **Lägger till DocxSaveOptions(Boolean) konstruktor.**

 Representerar alternativ för att spara .docx-filer.

### **Tar bort föråldrad WorkbookSettings.IsWriteProtected-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.IsWriteProtected istället.

### **Tar bort föråldrad WorkbookSettings.RecommendReadOnly-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.RecommendReadOnly istället.

### **Tar bort föråldrad WorkbookSettings.WriteProtectedPassword-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.Password istället.

