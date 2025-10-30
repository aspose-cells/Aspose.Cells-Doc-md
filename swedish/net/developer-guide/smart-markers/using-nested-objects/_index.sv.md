---
title: Smart import av inbäddade objekt till Excel med smarta markörer
type: docs
weight: 30
url: /sv/net/how-to-import-nested-objects-with-smart-markers/
---

## **Varför använda inbäddade objekt för smarta markörer**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Hierarkisk datastyrning: Verkliga data är i sig inbäddade (t.ex. en Order innehåller en Kund, som har en Adress). Inbäddade objekt speglar denna struktur och undviker platta/ artificiella fält som kund_stad.
2. Undvik namnkollisioner: Platta strukturer riskerar att krocka (t.ex. produkt_namn vs. leverantör_namn). Inbäddning skapar naturliga namnrymder:
<<product.name>> vs. <<supplier.name>>.
3. Modularitet & Återanvändbarhet: Återanvänd delobjekt i olika sammanhang, Adress-objekt kan ingå i Kund-, Leverantör- eller Anställda-markörer. Ändringar i Adress sprids globalt.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Ramverks-/Verktygsstöd: Moderna motorer (t.ex. Handlebars, React, FoxPro) hanterar inbäddade sökvägar inbyggt. Samma gäller för JSON/APIs där inbäddad data är standard.

## **Hur man importerar anonyma typer eller anpassade objekt med smarta markörer**
Aspose.Cells stöder också anonyma typer eller anpassade objekt i smarta markörer. Exemplet nedan visar hur detta fungerar. För att importera data från dynamiska objekt med hjälp av Smarta Markörer, besök följande artikel:

[Importering från dynamiskt objekt som datakälla](/cells/sv/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Hur man importerar inbäddade objekt med smarta markörer**
Aspose.Cells stödjer inbäddade objekt i smarta markörer, de inbäddade objekten bör vara enkla. Vi använder en enkel mallfil. Se den designer-kalkylblad som innehåller några inbäddade smarta markörer.

|**Det första kalkylbladet i filen SM_NestedObjects.xlsx som visar inbäddade smarta markörer.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Exemplet nedan visar hur detta fungerar.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Hur man importerar generiska listor som inbäddade objekt med smarta markörer**
Aspose.Cells stöder nu även användning av generiska listor som inbäddade objekt. Var god kontrollera skärmbilden av den genererade Excel-filen med följande kod. Som du kan se på skärmbilden innehåller ett lärarobjekt flera inbäddade studentobjekt.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Hur man importerar inbäddade objekt inte rad för rad med smarta markörer**
Den nuvarande standardbehandlingsmetoden är att behandla smartmaker rad för rad. Men ibland behöver smartmarkörer för samma datatabell behandlas tillsammans, oavsett 
om de är i samma rad eller inte, då måste du ange en angiven omfattning "_CellsSmartMarkers" och ange  WorkbookDesigner.LineByLine som falsk innan du anropar behandlingen.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
