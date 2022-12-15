---
title: Aspose.Cells for .NET 8.8.2 Release Notes
type: docs
weight: 90
url: /sv/net/aspose-cells-for-net-8-8-2-release-notes/
---
### **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44314 | Hur man återger Unicode tilläggstecken| Ny funktion|
|CELLSNET-41817 | Ställer in texteffekt på Offset i rektangelform| Förbättring|
|CELLSNET-41454 | Aspose.Cells bestämmer felaktigt vissa filformat| Förbättring|
|CELLSNET-44476 | Textriktning ignoreras när du sparar som HTML-filformat| Insekt|
|CELLSNET-44457 | De nedre ramarna i tabellen går förlorade vid konvertering till HTML-fil| Insekt|
|CELLSNET-44446 | Alla CSS-stilar har inte prefix när du sparar som HTML| Insekt|
|CELLSNET-44444 | Att öppna och spara filen som innehåller pivottabellen resulterar i korrupt kalkylblad| Insekt|
|CELLSNET-44443 | Pivotdiagram till PDF - Sekundär y-axel trasslat| Insekt|
|CELLSNET-44450 | Bildrotationen är inte korrekt i den resulterande PDF-filen| Insekt|
|CELLSNET-44303 | SheetRender.ToImage återger inte grafens dataetikett(er) korrekt| Insekt|
|CELLSNET-44478 |Zoomnivån ändras efter att Excel-filen öppnats och skrivits om| Insekt|
|CELLSNET-44477 | Listobjektnamn konflikt på kalkylbladskopia| Insekt|
|CELLSNET-44472 | CustomXmlParts fungerar inte korrekt för XLS-fil| Insekt|
|CELLSNET-44466 | Kan inte visa bilderna korrekt efter att ha exporterat HTML till Excel| Insekt|
|CELLSNET-44465 | Diagram tas bort när tomma rader/kolumner tas bort| Insekt|
|CELLSNET-44463 | Svart text i TextBox görs vit i PDF-filen| Insekt|
|CELLSNET-44456 | Fet stil i målfilen försvann efter Range.CopyData()-anrop| Insekt|
|CELLSNET-44453 | ExternalLink.IsReferred Property fungerar inte som förväntat| Insekt|
|CELLSNET-44445 | CopyStyle (smarta markörer) fungerar inte på alla sammanslagna celler| Insekt|
|CELLSNET-44263 | Formatering går förlorad när HTML importeras som XLSX| Insekt|
|CELLSNET-44439 | NullReferenceException vid PivotField.IsAscendSort| Undantag|
|CELLSNET-44430 | Fel uppstår när komplexa beräkningar utförs| Undantag|
### **2) Aspose.Cells Grid Suite**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSNET-44441 | När rad är markerad i nyare version, väljs också den första cellen i nästa rad| Insekt|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till DeleteOptions-klassen.**
Representerar inställningen för borttagning av rader/kolumner.
#### **Lägger till åsidosättande metoderna Cells.DeleteBlankRows(DeleteOptions-alternativ) och Cells.DeleteBlankColumns(DeleteOptions-alternativ).**
Tar bort tomma rader eller kolumner med inställning.
