---
title: Aspose.Cells för Java 17.3.0 Release Notes
type: docs
weight: 100
url: /sv/java/aspose-cells-for-java-17-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 17.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.3.0/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42205|Inställning av formel med lång sträng bokstavlig resulterar i korrupt Excel-fil|Förbättring|
|CELLSJAVA-42204|Prickade ramar från kalkylarket har inte renderats till HTML|Insekt|
|CELLSJAVA-42198|Formelberäkningen är fel med Aspose.Cells genererad Excel-fil|Insekt|
|CELLSJAVA-42156|De övre och nedre gränserna för celler försvinner vid konvertering till HTML|Insekt|
|CELLSJAVA-42208|Kommentarer (i slutet) skärs vertikalt när de genereras PDF via Aspose.Cells|Insekt|
|CELLSJAVA-42206|Seriestrecklinjer för diagram renderas inte korrekt i den utgående PDF-filen|Insekt|
|CELLSJAVA-42167 |Kategoriaxeletiketter visas i två rader efter konvertering av diagram till bild|Insekt|
|CELLSJAVA-42199|Vattenfallsdiagram, linjen från totalstapeln och stapeln precis innan den saknas|Insekt|
|CELLSJAVA-42201|Underuppgift - Kategoriaxeletiketter visas på två rader efter konvertering av diagram till bild|Insekt|
|CELLSJAVA-42155|Det exporterade diagrammet har x-axeletiketter som skiljer sig från den i Excel|Insekt|
|CELLSJAVA-42128|Diagrammet är fel när du öppnar och sparar källfilen i Excel|Insekt|
|CELLSJAVA-42203|Teckensnittet har ändrats efter att du enkelt laddat in och sparat XLSM|Insekt|
|CELLSJAVA-42196|Formateringen av den resulterande filen är förstörd i den återsparade filen|Insekt|
|CELLSJAVA-42195|Vattenfallsdiagram, Totalserie ser fel ut|Insekt|
|CELLSJAVA-42181|Skyddad vy efter att ha sparat en XLS-fil igen|Insekt|
|CELLSJAVA-42045|Radardiagrambild genereras inte|Insekt|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Anpassa globaliseringsinställningarna för en pivottabell**
Med den senaste versionen 17.3.0 eller senare kan utvecklare anpassa globaliseringsinställningarna för en pivottabell i en Excel-fil. De kan ändra pivotsumman, delsumman, totalsumman, alla artiklar, flera artiklar, kolumnetiketter, radetiketter, tomma värden enligt kraven. Utvecklare kan införliva den här funktionen i sina .NET-applikationer, oavsett Excel-textspråk. Det kan vara arabiska, hindi, polska, etc. Alla nya metoder som stöds listas nedan:

1. **Lägger till metoden GlobalizationSettings.getPivotTotalName().** Den får namnet "Total"-etiketten i pivottabellen. Utvecklare kan åsidosätta denna metod när pivottabellen innehåller två eller flera pivotfält i dataområdet.
1. **Lägger till metoden GlobalizationSettings.getPivotGrandTotalName().** - Den får namnet "Grand Total"-etiketten i pivottabellen.
1. **Lägger till metoden GlobalizationSettings.getMultipleItemsName().** - Den får namnet "(Flera artiklar)"-etiketten i pivottabellen.
1. **Lägger till metoden GlobalizationSettings.getAllName().** - Den får namnet "(Alla)"-etiketten i pivottabellen.
1. **Lägger till GlobalizationSettings.getColumnLablesName()** metod - Den får namnet "kolumnetiketter" i pivottabellen.
1. **Lägger till metoden GlobalizationSettings.getRowLablesName().** - Den får namnet "Row Labels"-etiketten i pivottabellen.
1. **Lägger till metoden GlobalizationSettings.getEmptyDataName().** - Den får namnet "(tom)"-etikett i pivottabellen.
1. **Lägger till metoden GlobalizationSettings.getSubTotalName(PivotFieldSubtotalType subTotalType)** - Den får namnet på typen "PivotFieldSubtotalType" i pivottabellen.

Detta kodexempel utvecklar hur man anpassar globaliseringsinställningarna för en pivottabell. Den skapar en klass CustomPivotTableGlobalizationSettings härledd från en basklass GlobalizationSettings och åsidosätter alla nödvändiga metoder. Dessa metoder returnerar den anpassade texten för Pivot Summa, Sub Summa, Totalsumma, Alla artiklar, Flera artiklar, Kolumnetiketter, Radetiketter, Tomma värden. Sedan tilldelar den objektet för den här klassen till egenskapen Workbook.GlobalizationSettings. Koden laddar källexcel-filen som innehåller pivottabellen, uppdaterar och beräknar dess data och sparar den som en utdata-PDF-fil. Utvecklare kan också spara arbetsboken i valfritt format som stöds.

**Java**

{{< highlight "java" >}}

 //Load your excel file

Workbook wb = new Workbook(dirPath + "samplePivotTableGlobalizationSettings.xlsx");



//Setting Custom Pivot Table Globalization Settings

wb.getSettings().setGlobalizationSettings(new CustomPivotTableGlobalizationSettings());



//Hide first worksheet that contains the data of the pivot table

wb.getWorksheets().get(0).setVisible(false);



//Access second worksheet

Worksheet ws = wb.getWorksheets().get(1);



//Access the pivot table, refresh and calculate its data

PivotTable pt = ws.getPivotTables().get(0);

pt.setRefreshDataFlag(true);

pt.refreshData();

pt.calculateData();

pt.setRefreshDataFlag(false);



//Pdf save options - save entire worksheet on a single pdf page

PdfSaveOptions options = new PdfSaveOptions();

options.setOnePagePerSheet(true);



//Save the output pdf 

wb.save(dirPath + "outputPivotTableGlobalizationSettings.pdf", options);



// it derives a new class, called CustomPivotTableGlobalizationSettings, from the GlobalizationSettings class, as follows:

class CustomPivotTableGlobalizationSettings extends GlobalizationSettings

{   

    //Gets the name of "Total" label in the PivotTable.

    //You need to override this method when the PivotTable contains two or more PivotFields in the data area.

    public String getPivotTotalName()

    {

        System.out.println("---------GetPivotTotalName-------------");

        return "AsposeGetPivotTotalName";

    }



    //Gets the name of "Grand Total" label in the PivotTable.

    public String getPivotGrandTotalName()

    {

        System.out.println("---------GetPivotGrandTotalName-------------");

        return "AsposeGetPivotGrandTotalName";

    }



    //Gets the name of "(Multiple Items)" label in the PivotTable.

    public String getMultipleItemsName()

    {

        System.out.println("---------GetMultipleItemsName-------------");

        return "AsposeGetMultipleItemsName";

    }



    //Gets the name of "(All)" label in the PivotTable.

    public String getAllName()

    {

        System.out.println("---------GetAllName-------------");

        return "AsposeGetAllName";

    }



    //Gets the name of "Column Labels" label in the PivotTable.

    public String getColumnLablesName()

    {

        System.out.println("---------GetColumnLablesName-------------");

        return "AsposeGetColumnLablesName";

    }



    //Gets the name of "Row Labels" label in the PivotTable.

    public String getRowLablesName()

    {

        System.out.println("---------GetRowLablesName-------------");

        return "AsposeGetRowLablesName";

    }



    //Gets the name of "(blank)" label in the PivotTable.

    public String getEmptyDataName()

    {

        System.out.println("---------GetEmptyDataName-------------");

        return "(blank)AsposeGetEmptyDataName";

    }



    //Gets the name of PivotFieldSubtotalType type in the PivotTable.

    public String getSubTotalName(int subTotalType)

    {

        System.out.println("---------GetSubTotalName-------------");



        switch (subTotalType)

        {

            case PivotFieldSubtotalType.SUM:

                return "AsposeSum";//polish



            case PivotFieldSubtotalType.COUNT:

                return "AsposeCount";



            case PivotFieldSubtotalType.AVERAGE:

                return "AsposeAverage";



            case PivotFieldSubtotalType.MAX:

                return "AsposeMax";



            case PivotFieldSubtotalType.MIN:

                return "AsposeMin";



            case PivotFieldSubtotalType.PRODUCT:

                return "AsposeProduct";



            case PivotFieldSubtotalType.COUNT_NUMS:

                return "AsposeCount";



            case PivotFieldSubtotalType.STDEV:

                return "AsposeStdDev";



            case PivotFieldSubtotalType.STDEVP:

                return "AsposeStdDevp";



            case PivotFieldSubtotalType.VAR:

                return "AsposeVar";

            case PivotFieldSubtotalType.VARP:

                return "AsposeVarp";

        }

        return "AsposeSubTotalName";

    }

}//End CustomPivotTableGlobalizationSettings

{{< /highlight >}}
### **Kör klientsideskriptet på Page Change Event of GridWeb Control**
Genom att använda OnPageChangeClientFunction-egenskapen för GridWeb-kontroll kan utvecklare köra ett skript på klientsidan på sidändringshändelsen eftersom GridWeb-kontrollen kan hålla data på flera sidor. De kan behöva visa det aktuella sidindexet i sina webbapplikationer.

1. **Lägger till en OnPageChangeClientFunction-egenskap i GridWeb Control** - den hämtar eller ställer in klientsidans skriptfunktion så att den anropas när sidindexet ändras. Det träder bara i kraft när EnablePaging är sant.

Det här kodexemplet visar användningen av egenskapen OnPageChangeClientFunction. Den ställer in egenskapen med klientsidans funktion som heter MyOnPageChange. Nu, närhelst användaren ändrar GridWeb-sidan, kommer den att anropa klientsidans funktion MyOnPageChange som skriver ut**aktuellt sidindex**på**trösta**:

**Java**

{{< highlight "java" >}}

 // It is the client side function MyOnPageChange that will be executed because of setting OnPageChangeClientFunction ="MyOnPageChange"property in GridWeb.

function MyOnPageChange(index) {

    console.log("current page is:" + (index+1));

}



// The following code explains how to enable paging and set the OnPageChangeClientFunction property.

GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
### **Validera hela Excel-arbetsbladet**
Som standard validerar GridWeb endast de uppdaterade cellerna och validerar inte hela Excel-kalkylbladet. Men om utvecklare kräver att validera hela Excel-arbetsbladet på klientsidan innan GridWeb skickar begäran till servern, bör du ställa in needValidateall-variabeln inuti acwmain.js till true.
### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

1. [Anpassa globaliseringsinställningar för pivottabell](/cells/sv/java/customize-globalization-settings-for-pivot-table/)
1. [Utför klientsidans funktion på GridWeb-sidaändring](/cells/sv/java/execute-client-side-function-on-gridweb-page-change/)
1. [Validera hela kalkylbladet istället för bara de uppdaterade cellerna](/cells/sv/java/validate-entire-worksheet-instead-of-only-the-updated-cells/)
