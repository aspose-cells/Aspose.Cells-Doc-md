---
title: Pdf
type: docs
weight: 220
url: /sv/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel Workbook till PDF. I det här exemplet kommer vi att se den fullständiga konverteringen av en Excel-arbetsbok till PDF.

{{% /alert %}}

## **Konvertera Excel-arbetsbok till PDF**

PDF-filer används ofta för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{% alert color="primary" %}}

 Aspose.Cells för .NET skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, vid rendering av dokument till PDF, fylls Aspose.Cells för .NET**Ansökan** fält med värdet 'Aspose.Cells' och**PDF-producent** fält med värde, t.ex. 'Aspose.Cells v17.9'.

Observera att du inte kan instruera Aspose.Cells för .NET att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}}

### **Direkt konvertering**

 Aspose.Cells för .NET stöder konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil till PDF med hjälp av**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** klass'**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metod. De**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metoden ger**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**uppräkningsmedlem som konverterar de ursprungliga Excel-filerna till PDF-format.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1.  Instantiera ett objekt av**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)**klass genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda in en befintlig mallfil eller hoppa över det här steget om du skapar arbetsboken från början.
1. Gör något arbete (mata in data, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, och så vidare) på kalkylarket med hjälp av Aspose.Cells' API:er.
1.  När kalkylarkskoden är klar ringer du**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** klass'**[Spara](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metod för att spara kalkylarket.

 Filformatet ska vara PDF så välj*Pdf* (ett fördefinierat värde) från**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**uppräkning för att generera det slutliga PDF-dokumentet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Avancerad konvertering**

Du kan också välja att använda**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** klass för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** klass ger dig kontroll över utskrifts-, teckensnitts-, säkerhets- och komprimeringsinställningar för utdata-PDF. Den viktigaste egendomen är**[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**som gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.

#### **Spara arbetsbok till PDF/A-kompatibla filer**

 Det nedan tillhandahållna kodavsnittet visar hur du använder**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**klass för att spara Excel-filer till PDF/A-kompatibelt PDF-format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Observera att**[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Egenskapen lades till med utgåvan av Aspose.Cells för .NET 5.3.0.

{{% /alert %}}

#### **Ställ in tid för att skapa PDF**

 Med**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**klass, kan du hämta eller ställa in PDF-genereringstiden. Följande kod visar användningen av**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** egenskap för att ställa in skapandet av PDF-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Ställ in alternativet ContentCopyForAccessibility**

Med**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** klass, kan du hämta eller ställa in PDF:en**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**alternativet för att kontrollera innehållsåtkomsten i den konverterade PDF-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Exportera anpassade egenskaper till PDF**

Med**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** klass, kan du exportera de anpassade egenskaperna i källarbetsboken till PDF:en.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)** Enumerator tillhandahålls för att specificera hur egenskaper exporteras. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Arkiv och sedan egenskaper alternativ som visas i följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ner[här](sourceWithCustProps.xlsx) för testning och utdata PDF-filen "outSourceWithCustProps" är tillgänglig[här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Konverteringsattribut**

Vi arbetar för att förbättra konverteringsfunktionerna med varje ny version. Aspose.Cell's Excel till PDF-konvertering har fortfarande ett par begränsningar. Viss kalkylarksformatering kan gå förlorad vid konvertering till PDF-format. Dessutom stöds inte vissa ritobjekt ännu.

Tabellen som följer listar alla funktioner som helt eller delvis stöds vid export till PDF med Aspose.Cells. Den här tabellen är inte slutgiltig och täcker inte alla kalkylbladsattribut men den identifierar de funktioner som inte stöds eller delvis stöds för konvertering till PDF .

|**Dokumentelement**|**Attribut**|**Stöds**|**Anteckningar**|
|:- |:- |:- |:- |
|Inriktning||Ja||
|Bakgrundsinställningar||Ja||
|Gräns|Färg|Ja||
|Gräns|Linjestil|Ja||
|Gräns|Linjebredd|Ja||
|Cell Data||Ja||
|Kommentarer||Ja||
|Villkorlig formatering||Ja||
|Dokument egenskaper||Ja||
|Rita objekt||Delvis|Objekt som stöds: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Font|Storlek|Ja||
|Font|Färg|Ja||
|Font|Stil|Ja||
|Font|Understrykning|Ja||
|Font|Effekter|Delvis|Endast genomslagseffekt stöds|
|Bilder||Ja||
|Hyperlänk||Ja||
|Diagram||Delvis||
|Sammanslagna Cells||Ja||
|Sidbrytning||Ja||
|Utskriftsformat|Sidhuvud/sidfot|Ja||
|Utskriftsformat|Marginaler|Ja||
|Utskriftsformat|Sidorientering|Ja||
|Utskriftsformat|Sidstorlek|Ja||
|Utskriftsformat|Utskriftsområde|Ja||
|Utskriftsformat|Skriv ut titlar|Ja||
|Utskriftsformat|Skalning|Ja||
|Radhöjd/kolumnbredd||Ja||
|RTL-språk (Right to Left).||Ja||

{{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}

## **Förhandsämnen**
- [Lägg till PDF-bokmärken](/cells/sv/net/add-pdf-bookmarks/)
- [Lägg till PDF-bokmärken med namngivna destinationer](/cells/sv/net/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utdata-PDF när det inte finns något att skriva ut](/cells/sv/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändra teckensnittet på bara de specifika Unicode-tecken medan du sparar till PDF](/cells/sv/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Kontrollera laddningen av externa resurser i MS Excel Workbook medan du renderar till PDF](/cells/sv/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Konvertera en XLS-fil till PDF-format](/cells/sv/net/convert-an-xls-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format som är kompatibelt med PDFA-1a](/cells/sv/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla kalkylbladskolumner på en enda PDF-sida](/cells/sv/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Hämta DrawObject and Bound medan du renderar till PDF med DrawObjectEventHandler-klassen](/cells/sv/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Få varningar för teckensnittsersättning när du renderar Excel-fil](/cells/sv/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorera fel när du renderar Excel till PDF](/cells/sv/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer samtidigt som du sparar till PDF](/cells/sv/net/print-comments-while-saving-to-pdf/)
- [Återge Office-tillägg medan du konverterar Excel till PDF](/cells/sv/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Återge en PDF-sida per Excel-arbetsblad - Excel till PDF-konvertering](/cells/sv/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Återge Unicode-tilläggstecken i utdata-PDF med Aspose.Cells](/cells/sv/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Sampling av tillagda bilder - Excel till PDF-konvertering](/cells/sv/net/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje kalkylblad till en annan PDF-fil](/cells/sv/net/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel till PDF med standard- eller minimistorlek](/cells/sv/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Säkra PDF-dokument](/cells/sv/net/secure-pdf-documents/)
- [Ange hur strängen ska korsas i utdata-PDF och bild](/cells/sv/net/specify-how-to-cross-string-in-output-pdf-and-image/)
