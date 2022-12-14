---
title: Licensiering
type: docs
weight: 50
url: /sv/java/licensing/
---
{{% alert color="primary" %}} 

 Du kan ladda ner en utvärderingsversion av**Aspose.Cells** för Java från[dess nedladdningssida](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. Utvärderingsversionen ger absolut samma möjligheter som den licensierade versionen av produkten. Dessutom blir utvärderingsversionen helt enkelt licensierad när du köper en licens och lägger till ett par rader kod för att tillämpa licensen.

 När du är nöjd med din utvärdering av**Aspose.Cells** , du kan[köpa en licens](https://purchase.aspose.com)på webbplatsen Aspose. Bekanta dig med de olika prenumerationstyperna som erbjuds. Om du har några frågor, tveka inte att kontakta Aspose säljteamet.

Varje Aspose-licens innehåller en ettårsprenumeration för gratis uppgraderingar till alla nya versioner eller korrigeringar som kommer ut under denna tid. Teknisk support är gratis och obegränsad och tillhandahålls både till licensierade användare och utvärderingsanvändare.

{{% /alert %}} {{% alert color="primary" %}} 

 Om du vill testa**Aspose.Cells** utan begränsningar i utvärderingsversionen, begär en 30-dagars tillfällig licens. Vänligen hänvisa till[Hur får man en tillfällig licens?](https://purchase.aspose.com/temporary-license) för mer information.

{{% /alert %}}

## **Begränsningar för utvärderingsversion**

 Utvärderingsversion av**Aspose.Cells** produkt (utan angiven licens) ger full produktfunktionalitet, men den är begränsad till att öppna 100 filer i ett program och ett extra kalkylblad med utvärderingsvattenstämpel.

Begränsningarna visas nedan:

### **Första begränsningen: Antal öppnade filer**

När du kör ditt program kan du bara öppna 100 Excel-filer. Om din ansökan överstiger detta antal kommer ett undantag att kastas.

### **2:a begränsningen: Arbetsblad med utvärderingsvattenstämpel**

![todo:image_alt_text](licensing_1.png)

Detta kalkylblad kommer alltid att visas som det aktiva kalkylbladet. Endast i licensierad version kan du ställa in det aktiva kalkylbladet till andra kalkylblad.

## **Ställa in en licens**

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal utvecklare den är licensierad till, prenumerationsutgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen; även ett oavsiktligt tillägg av en extra radbrytning i filen kommer att ogiltigförklara den.

Du måste ställa in en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsningar. Du behöver bara ange en licens en gång per ansökan eller process.

Licensen kan laddas från en stream eller fil på följande platser:

1. Explicit väg.
1. Mappen som innehåller Aspose.Cells.jar.

 Använd[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) metod för att licensiera komponenten. Ofta är det enklaste sättet att ställa in en licens att lägga licensfilen i samma mapp som Aspose.Cells.jar och ange bara filnamnet utan sökväg som visas i följande exempel:

### **Exempel 1**

 I detta exempel**Aspose.Cells** kommer att försöka hitta licensfilen i mappen som innehåller JAR:erna för din applikation.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Exempel 2**

Initierar en licens från en stream.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Anmärkningar om att tillämpa en licens i Aspose.Cells.GridWeb**

Det rekommenderas att du placerar licenskoden på en plats i din webbapplikation där den ska behandlas först.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Ansöker om mätlicens**

Aspose.Cells tillåter utvecklare att använda uppmätt nyckel. Det är en ny licensmekanism. Den nya licensmekanismen kommer att användas tillsammans med den befintliga licensmetoden. De kunder som vill bli fakturerade baserat på användningen av API-funktionerna kan använda den uppmätta licensen. För mer information, se[Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)sektion.

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
