---
title: Offentliga API-ändringar i Aspose.Cells 17.1.0
type: docs
weight: 20
url: /sv/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.12.0 till 17.1.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för namngivna intervall**
 Aspose.Cells för C++ stöder nu skapande såväl som manipulering av de namngivna intervallen. Följande kodavsnitt visar hur enkelt det är att använda Aspose.Cells för C++ API för att[skapa namngivna intervall](/cells/sv/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 Förutom att skapa nya namngivna intervall, stödjer Aspose.Cells för C++ API:er också för att manipulera befintliga namngivna intervall. Följande kodavsnitt använder Aspose.Cells för C++ API till[manipulera ett befintligt namngivet intervall](/cells/sv/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Lade till ICells::LinkToXmlMap Method**
Metoden LinkToXmlMap har lagts till i klassen ICells som är användbar för att länka en XML-karta.
### **Lade till ICells::ImportCSV-metod**
ImportCSV-metoden har lagts till i ICells-klassen vilket är användbart när man importerar en CSV-fil till cellerna i ett kalkylblad.
### **Lade till ICells::ImportTwoDimensionArray Method**
Metoden GetIProtectedRangeCollection har lagts till i klassen ICells, vilket är användbart för att importera en tvådimensionell matris av data till ett kalkylblad.
### **Lade till IWorksheet::GetIProtectedRangeCollection Method**
Metoden GetIProtectedRangeCollection har lagts till i IWorksheet-klassen som är användbar för att hämta samlingen av IProtectedRange-objekt.
### **Lade till IWorksheet::GetIProtectedRangeCollection Method**
Metoden GetIProtectedRangeCollection har lagts till i IWorksheet-klassen som är användbar för att hämta redigeringsintervallsamlingen från kalkylbladet.
### **Lade till IWorkbookSettings::ClearPivottables Method**
Metoden ClearPivottables har lagts till i klassen IWorkbookSettings som är användbar för att rensa alla pivottabeller från ett givet kalkylblad.
### **Lade till IWorksheetCollection::CreateIRange Method**
Metoden CreateIRange har lagts till i klassen IWorksheetCollection som är användbar för att skapa ett objekt av IRange genom att skicka cellreferenser i strängformat.
### **Lade till IExternalLink::IsVisible Method**
IsVisible-metoden får synlighetsstatusen för en extern länk i Excel-applikationen.
### **Lade till GetScaleCrop & SetScaleCrop-metoder**
Aspose.Cells för C++ 17.1.0 har exponerat GetScaleCrop & SetScaleCrop-metoderna för klassen IBuiltInDocumentPropertyCollection. Dessa metoder är användbara för att få eller ställa in egenskapen ScaleCrop som indikerar visningsläget för dokumentminiatyren.
### **Lade till metoderna GetLinksUpToDate & SetLinksUpToDate**
Aspose.Cells för C++ 17.1.0 har exponerat metoderna GetLinksUpToDate & SetLinksUpToDate för klassen IBuiltInDocumentPropertyCollection. Dessa metoder är användbara för att få eller ställa in LinkUpToDate-egenskapen som anger om hyperlänkar i ett dokument är uppdaterade.
### **Lade till GetAbsolutePath & SetAbsolutePath-metoder**
Aspose.Cells för C++ 17.1.0 har exponerat GetAbsolutePath & SetAbsolutePath-metoderna för IWorkbook-klassen. Dessa metoder är användbara för att få eller ställa in den absoluta sökvägen till filen som endast kan användas för externa länkar.
### **Lade till GetFormula & SetFormula Methods**
Den här versionen av Aspose.Cells för C++ har avslöjat metoderna GetFormula & SetFormula för klassen IListColumn. Dessa metoder är användbara för att få eller ställa in formeln för en listkolumn.
### **Lade till metoder för GetCheckCompatibility & SetCheckCompatibility**
Den här versionen av Aspose.Cells för C++ har avslöjat metoderna GetCheckCompatibility & GetCheckCompatibility för klassen IWorkbookSettings. Dessa metoder är användbara för att få eller ställa in kompatibilitetskontrollegenskapen som anger om API:et ska kontrollera kompatibiliteten när arbetsboken sparas. Standardvärdet är sant och kan ställas in på falskt om applikationskravet inte är att kontrollera kompatibiliteten.
### **Lade till metoder för GetILightCellsDataHandler & SetILightCellsDataHandler**
Aspose.Cells för C++ har nu avslöjat metoderna GetILightCellsDataHandler & SetILightCellsDataHandler för klassen ILoadOptions. Dessa metoder betecknar datahanteraren för bearbetning av celldata under läsning av mallfil.
### **Lade till GetCultureInfo & SetCultureInfo-metoder**
Aspose.Cells för C++ har avslöjat metoderna GetCultureInfo & SetCultureInfo för klassen ILoadOptions. Dessa metoder kan hämta eller ställa in systemkulturinformationen när filen laddas.
## **Borttagna API:er**
### **Tog bort ICells::MaxDataRowInColumn Method**
Det rekommenderas att använda metoden ICells::GetLastDataRow istället.
### **Tog bort ICell::GetConditionalIStyle-metoden**
Det rekommenderas att använda metoden ICell::GetIConditionalFormattingResult istället.
### **Tog bort IPageSetup::GetDraft & SetDraft Methods**
Det rekommenderas att använda metoderna IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft istället.

{{% alert color="primary" %}} 

Med lanseringen av Aspose.Cells för C++ 17.1.0 har vi tagit bort några metoder som inte användes och därför ansågs vara onödiga. Här är listan över alla sådana metoder.

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType Methods
- IRange::ToString-metod
- IRow::Equals Method
- IWorkbook::SetISettings Method
- ICell::ToString() Metod
- ICell::Equals(ObjectPtr)-metod
- ICell::GetHashCode-metod
- IWorksheet::ToString Method

{{% /alert %}}
