---
title: Offentliga API ändringar i Aspose.Cells 8.2.1
type: docs
weight: 80
url: /sv/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar av Aspose.Cells API från version 8.2.0 till 8.2.1, som kan vara av intresse för modul/tillämpningsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lägg till GetValidation() -metoden för Cell Class**
Datavalidering är en av funktionerna som kalkylbladsformgivare använder för att förhindra användare från att infoga ogiltiga värden i en specifik cell. Med Aspose.Cells for .NET 8.2.1 har API:et exponerat en enkel mekanism som identifierar om datavalidering har tillämpats på en cell. Använd GetValidation-metoden för Cell-klassen för att få eventuella tillämpade valideringar. Om det inte finns någon validering returnerar metoden null. På samma sätt kan du använda metoden GetValidationInCell i ValidationCollection-klassen för att få valideringen som tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Få validering tillämpade på en cell](/cells/sv/net/get-validation-applied-on-a-cell/) för mer information.

{{% /alert %}}
## **Lägg till GetValidationValue() -metoden för Cell Class**
Förutom att avgöra om validering har tillämpats kan du också verifiera om ett givet värde uppfyller datavalideringsreglerna för en specifik cell. Denna funktion är användbar i scenarier när du vill verifiera om det inmatade värdet i cellen uppfyller datavalideringsreglerna på flyg. Aspose.Cells API har exponerat GetValidationValue-metoden för Cell-klassen. Om värdet som skrivs in i en cell inte uppfyller datavalideringsreglerna returnerar GetValidationValue-metoden för Cell-klassen false.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Verifiera att Cellvärdet uppfyller datavalideringsreglerna](/cells/sv/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Lägg till överbelastningsmetoden ToPrinter(PrinterSettings printerSettings) för WorkbookRender-klassen**
Du kan använda den överbelastade metoden för att rendera arbetsbok till skrivare via PrinterSettings.
