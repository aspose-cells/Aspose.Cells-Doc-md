---
title: Hur man ställer in utskriftsområde
type: docs
weight: 200
url: /sv/net/how-to-set-print-area/
description: Denna artikel visar kod som förklarar hur man ställer in utskriftsområde med Aspose.Cells biblioteket.
keywords: Begränsa utskriftsområdet, ställ in utskriftsområdet, rensa utskriftsområdet, ställ in och rensa utskriftsområdet med C#, Hur man ställer in utskriftsområde, Ställ in och rensa utskriftsområdet med C#, Hur man rensar utskriftsområdet i C#, Hur man lägger till utskriftsområde med C#, Hur man tar bort utskriftsområde med C#, Hur man ställer in utskriftsområdet i Excel, Hur man rensar utskriftsområdet i Excel.
---

## **Möjliga användningsscenario**

Att ställa in ett utskriftsområde i ett dokument, så som ett Excel-ark, hjälper till att kontrollera vilka innehåll som inkluderas vid utskrift. Här är några skäl att ställa in ett utskriftsområde:

1. Fokusera på specifika data: Du kan skriva ut endast de mest relevanta delarna, vilket undviker onödigt innehåll.
1. Förbättrad layout: Det hjälper till att organisera och passa innehållet snyggt på de utskrivna sidorna, vilket förhindrar avdelningar eller oönskade sidbrytningar.
1. Spara resurser: Genom att begränsa utskriftsområdet kan du minska mängden papper och bläck som används.
1. Professionell presentation: Det säkerställer att endast den polerade och slutgiltiga versionen av data skrivs ut, vilket är särskilt viktigt för rapporter eller presentationer.
1. Konsekvens: När du skriver ut samma dokument flera gånger, säkerställer ett inställt utskriftsområde konsekvent resultat.

<br>
Att ställa in ett utskriftsområde är särskilt användbart i större dokument där endast en del behöver delas eller granskas i tryckt form.

## **Hur man sätter in utskriftsområde i Excel**

För att ställa in ett utskriftsområde i Excel, följ dessa steg:

1. Välj cellerna: Klicka och dra för att välja det cellområde du vill ange som utskriftsområde.
1. Öppna fliken Sida Layout: Gå till "Sida Layout"-fliken i ribbonen längst upp i Excel-fönstret.
1. Ange Utskriftsområde: I gruppen "Sidan Setup" klickar du på "Utskriftsområde". Väljs från rullgardinsmenyn, välj "Ställ in Utskriftsområde".
<br>
<img src="3.png" width=60% />

1. Lägg till i Utskriftsområdet: Vill du lägga till fler celler till det befintliga utskriftsområdet, markera de ytterligare cellerna, gå till "Utskriftsområde" i "Sida Layout"-fliken, och välj "Lägg till i Utskriftsområde".

<br>
Denna åtgärd definierar de valda cellerna som utskriftsområdet. När du skriver ut kalkbladet, kommer endast detta område att skrivas ut.

## **Hur man rensar utskriftsområde i Excel**

Följ dessa steg för att rensa utskriftsområdet i Excel:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Rensa Utskriftsområde: I gruppen "Sidan Setup" klickar du på "Utskriftsområde". Välj "Rensa Utskriftsområde" från rullgardinsmenyn.
<br>
<img src="4.png" width=60% />

<br>
Denna åtgärd tar bort eventuellt tidigare angivet utskriftsområde, vilket gör att hela kalkbladet kan skrivas ut.

## **Vad händer efter att ha rensat utskriftsområdet**

Att rensa utskriftsområdet i ett kalkulsprogram som Excel med Aspose.Cells gör att hela kalkbladet inkluderas när du skriver ut dokumentet. Om ett utskriftsområde är angett, skrivs endast det specifika cellområdet ut. Genom att rensa utskriftsområdet säkerställer du att inget specifikt område är definierat, och den standardskrivningen som inkluderar hela bladet kommer att träda i kraft.

1. Standard utskriftsbeteende: Hela kalkbladet kommer att betraktas för utskrift. Det innebär att alla celler med data eller formatering kommer att skrivas ut.
1. Inga begränsningar för Utskriftsområde: Tidigare definierade gränser för utskriftsområdet tas bort. Om det fanns specifika rader och kolumner för utskrift, begränsas de inte längre av dessa.
1. Fullständig innehållsutskrift: Allt innehåll, inklusive rubriker, sidfötter och annan data inom kalkbladet, kommer att ingå i utskriftsjobbet.

## **Så ställer du in utskriftsområdet med Aspose.Cells**

För att ställa in utskriftsområdet i ett specificerat kalkblad: Först, ladda [exempelfilen](input.xlsx), och sedan behöver du ändra egenskapen [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) för objektet [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) för det önskade kalkbladet. Att sätta denna egenskap till en cellrange-sträng kommer att ange utskriftsområdet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-area.cs" >}}

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Så rensar du utskriftsområdet med Aspose.Cells**

För att rensa utskriftsområdet i ett specifikt kalkblad: Först, ladda [exempelfilen](input.xlsx), och sedan behöver du ändra egenskapen [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) för objektet [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) för det önskade kalkbladet. Att sätta denna egenskap till en tom sträng kommer att rensa utskriftsområdet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-area.cs" >}}

Utmatningsresultat:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
