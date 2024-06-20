---
title: Offentliga API ändringar i Aspose.Cells 8.2.1
type: docs
weight: 90
url: /sv/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar av Aspose.Cells API från version 8.2.0 till 8.2.1, som kan vara av intresse för modul/tillämpningsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagd getValidation() metod för Cell Class**
Datavalidering är en av de funktioner som kalkylbladsdesigners använder för att förhindra användare från att ange ogiltiga värden i en specifik cell. Med Aspose.Cells for Java 8.2.1 har API:en exponerat en enkel mekanism som identifierar om datavalidering har tillämpats på en cell. Använd getValidation-metoden i Cell-klassen för att få reda på eventuella tillämpade valideringar. Om det inte finns någon validering returnerar metoden null. På samma sätt kan du använda getValidationInCell-metoden i ValidationCollection-klassen för att få reda på valideringen som har tillämpats på någon cell genom att ange dess rad- och kolumnindex.

{{% alert color="primary" %}} 

Se den detaljerade artikeln om [Få Validering Tillämpad på en Cell](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) för mer information.

{{% /alert %}}
## **Tillagd getValidationValue() metod för Cell-klassen**
Förutom att avgöra om validering har tillämpats kan du också verifiera om ett givet värde uppfyller datavalideringsreglerna för en specifik cell. Denna funktion är användbar i scenarier när du vill verifiera om värdet som angetts i cellen uppfyller datavalideringsreglerna på flyg. Aspose.Cells API:en har exponerat getValidationValue-metoden för Cell-klassen. Om det värde som angetts i en cell inte uppfyller datavalideringsreglerna returnerar getValidationValue-metoden för Cell-klassen false.

{{% alert color="primary" %}} 

Se den detaljerade artikeln om [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Tillagd överlagring tillPrinter(PrinterSettings printerSettings) metod för WorkbookRender-klassen**
Du kan använda den överbelastade metoden för att rendera arbetsbok till skrivare via PrinterSettings.
