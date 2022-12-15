---
title: Offentlig API Ändringar i Aspose.Cells 8.2.1
type: docs
weight: 90
url: /sv/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.2.0 till 8.2.1, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till metoden getValidation() för klassen Cell**
Datavalidering är en av funktionerna som kalkylbladsdesigners använder för att hindra användare från att infoga ogiltiga värden i en viss cell. Med Aspose.Cells for Java 8.2.1 har API avslöjat en enkel mekanism som identifierar om datavalidering har tillämpats på en cell. Använd getValidation-metoden för klassen Cell för att skaffa eventuell tillämpad validering. Om det inte finns någon validering returnerar metoden null. På samma sätt kan du använda metoden getValidationInCell i klassen ValidationCollection för att få valideringen som tillämpas på valfri cell genom att tillhandahålla dess rad- och kolumnindex.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Få validering tillämpad på en Cell](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) för mer information.

{{% /alert %}}
## **Lade till metoden getValidationValue() för klassen Cell**
Förutom att avgöra om validering har tillämpats kan du också verifiera om ett givet värde uppfyller datavalideringsreglerna för en viss cell. Den här funktionen är användbar i scenarier när du vill verifiera om värdet som anges i cellen uppfyller reglerna för datavalidering direkt. Aspose.Cells API har exponerat getValidationValue-metoden för klassen Cell. Om värdet som anges i en cell inte uppfyller datavalideringsreglerna, returnerar getValidationValue-metoden för klassen Cell false.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Verifiera att Cell-värdet uppfyller reglerna för datavalidering](/cells/sv/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Lade till överbelastning tillPrinter(PrinterSettings printerSettings) metod för WorkbookRender-klassen**
Du kan använda den överbelastade metoden för att rendera arbetsboken till skrivaren via PrinterSettings.
