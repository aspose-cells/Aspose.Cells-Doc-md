---
title: Licensiering
type: docs
weight: 50
url: /sv/java/licensing/
description: Aspose.Cells for JAVA tillhandahåller olika planer för köp eller erbjuder en gratis provperiod och en 30 dagars tillfällig licens för utvärdering med licensierings och prenumerationspolicyer i Java.
keywords: Java Apply License från Disk eller Ström. Java Set Licens från Disk eller Ström. Tillämpa Licens i Aspose.Cells for Java.
---

## **Hur man ansöker om en licens i Aspose.Cells-komponenten**

Licensen är en vanlig text XML-fil som innehåller detaljer som produktens namn, antalet utvecklare den är licensierad till, prenumerations utgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen; även det oavsiktliga tillskottet av en extra radbrytning i filen kommer ogiltigförklara den.

Du behöver aktivera en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsningar. Du behöver bara aktivera en licens en gång per applikation eller process.

Licensen kan laddas från en ström eller fil på följande platser:

1. Explicit sökväg.
1. Mappen som innehåller Aspose.Cells.jar.

Använd metoden [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-) för att licensiera komponenten. Ofta är det enklaste sättet att sätta licensen att lägga licensfilen i samma mapp som Aspose.Cells.jar och bara specificera filnamnet utan sökväg som visas i följande exempel:

### **Hur man ansöker om en licens från disk**

I detta exempel kommer **Aspose.Cells** försöka hitta licensfilen i mappen som innehåller JAR-filerna för din applikation.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Hur man ansöker om en licens från Ström**

Initierar en licens från en ström.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Hur man ansöker om en licens i Aspose.Cells.GridWeb**

Det rekommenderas att placera licensieringskoden på en plats i din webbapplikation där den bör bearbetas först.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Hur man ansöker om ett metered licens**

Aspose.Cells tillåter utvecklare att tillämpa meterednyckel. Det är en ny licensieringsmekanism. Den nya licensieringsmekanismen kommer att användas tillsammans med den befintliga licensieringsmetoden. De kunder som vill faktureras utifrån användningen av API-funktionerna kan använda den metered licensieringen. För mer information, vänligen hänvisa till [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) avsnittet.

En ny klass [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) har introducerats för att tillämpa meterednyckel. Följande är ett exempel på kod som visar hur man ställer in metered offentlig och privat nyckel.

{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
