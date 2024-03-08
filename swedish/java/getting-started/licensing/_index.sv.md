---
title: Licensing
type: docs
weight: 50
url: /sv/java/licensing/
description: Aspose.Cells för JAVA tillhandahåller olika planer för köp eller erbjuder en gratis provperiod och en 30-dagars tillfällig licens för utvärdering med Licensing och prenumerationspolicyer i Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Hur man ansöker om en licens i Aspose.Cells-komponenten**

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal utvecklare den är licensierad till, prenumerationsutgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen; även ett oavsiktligt tillägg av en extra radbrytning i filen kommer att ogiltigförklara den.

Du måste ställa in en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsningar. Du behöver bara ange en licens en gång per ansökan eller process.

Licensen kan laddas från en stream eller fil på följande platser:

1. Explicit väg.
1. Mappen som innehåller Aspose.Cells.jar.

 Använd[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)metod för att licensiera komponenten. Ofta är det enklaste sättet att ställa in en licens att lägga licensfilen i samma mapp som Aspose.Cells.jar och ange bara filnamnet utan sökväg som visas i följande exempel:

###  **Hur man ansöker om en licens från disk**

 I detta exempel**Aspose.Cells** kommer att försöka hitta licensfilen i mappen som innehåller JAR:erna för din applikation.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Hur man ansöker om en licens från Stream**

Initierar en licens från en stream.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Hur man ansöker om en licens i Aspose.Cells.GridWeb**

Det rekommenderas att du placerar licenskoden på en plats i din webbapplikation där den ska behandlas först.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Hur man ansöker om mätlicens**

Aspose.Cells tillåter utvecklare att använda uppmätt nyckel. Det är en ny licensmekanism. Den nya licensmekanismen kommer att användas tillsammans med den befintliga licensmetoden. De kunder som vill bli fakturerade baserat på användningen av API-funktionerna kan använda den uppmätta licensen. För mer information, se[Mät Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)sektion.

En ny klass[Uppmätt](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)har införts för att tillämpa mätt nyckel. Följande är exempelkoden som visar hur man ställer in mätt offentlig och privat nyckel.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
