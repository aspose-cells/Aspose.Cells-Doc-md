---
title: Offentliga API ändringar i Aspose.Cells 17.1.0
type: docs
weight: 20
url: /sv/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

I detta dokument beskrivs ändringarna i Aspose.Cells API från version 16.12.0 till 17.1.0 som kan vara intressanta för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tilläggade och borttagna klasser, etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för namngivna intervall.**
Aspose.Cells for C++ stöder nu både skapandet och manipulationen av namngivna intervall. Följande kodsnutt demonstrerar hur enkelt det är att använda Aspose.Cells for C++ API för [att skapa namngivna intervall](/cells/sv/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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

Förutom att skapa nya namngivna intervall stöder Aspose.Cells for C++ API:er också att manipulera befintliga namngivna intervall. Följande kodsnutt använder Aspose.Cells for C++ API för att [manipulera ett befintligt namngivet intervall](/cells/sv/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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
### **Tillagd metoden ICells::LinkToXmlMap**
Metoden LinkToXmlMap har lagts till i klassen ICells, vilket är användbart för att länka en XML-karta.
### **Tillagd metoden ICells::ImportCSV**
Metoden ImportCSV har lagts till i klassen ICells, vilket är användbart för att importera en CSV-fil till celler på ett kalkylblad.
### **Tillagd metoden ICells::ImportTwoDimensionArray**
Metoden ImportTwoDimensionArray har lagts till i klassen ICells, vilket är användbart för att importera en tvådimensionell databehållare till ett kalkylblad.
### **Tillagd metoden IWorksheet::GetIProtectedRangeCollection**
Metoden GetIProtectedRangeCollection har lagts till i klassen IWorksheet, vilket är användbart för att hämta en samling av IProtectedRange-objekt.
### **Tillagd metoden IWorksheet::GetIProtectedRangeCollection**
Metoden GetIProtectedRangeCollection har lagts till i klassen IWorksheet, vilket är användbart för att hämta redigeringsområdessamlingen från kalkylbladet.
### **Tillagd metoden IWorkbookSettings::ClearPivottables**
Metoden ClearPivottables har lagts till i klassen IWorkbookSettings, vilket är användbart för att rensa alla pivottabeller från en given kalkyl.
### **Tillagd metoden IWorksheetCollection::CreateIRange**
Metoden CreateIRange har lagts till i klassen IWorksheetCollection, vilket är användbart för att skapa ett objekt av typen IRange genom att ange cellreferenser i strängformat.
### **Tillagd metoden IExternalLink::IsVisible**
Metoden IsVisible returnerar synlighetsstatusen för en extern länk i Excel-programmet.
### **Tillagd metoden GetScaleCrop & SetScaleCrop**
Aspose.Cells for C++ 17.1.0 har exponerat metoderna GetScaleCrop & SetScaleCrop till IBuiltInDocumentPropertyCollection-klassen. Dessa metoder är användbara för att få eller sätta egenskapen ScaleCrop som indikerar visningsläget för dokumentets miniatyrbild.
### **Lade till GetLinksUpToDate & SetLinksUpToDate-metoder**
Aspose.Cells for C++ 17.1.0 har exponerat GetLinksUpToDate & SetLinksUpToDate-metoder till IBuiltInDocumentPropertyCollection-klassen. Dessa metoder är användbara för att få eller sätta egenskapen LinkUpToDate som indikerar om hyperlänkar i ett dokument är uppdaterade.
### **Lade till GetAbsolutePath & SetAbsolutePath-metoder**
Aspose.Cells for C++ 17.1.0 har exponerat GetAbsolutePath & SetAbsolutePath-metoder till IWorkbook-klassen. Dessa metoder är användbara för att få eller sätta den absoluta sökvägen för filen som endast kan användas för externa länkar.
### **Lade till GetFormula & SetFormula-metoder**
Denna version av Aspose.Cells for C++ har exponerat GetFormula & SetFormula metoder för IListColumn-klassen. Dessa metoder är användbara för att få eller sätta formeln för en listkolumn.
### **Lade till GetCheckCompatibility & SetCheckCompatibility-metoder**
Denna version av Aspose.Cells for C++ har exponerat GetCheckCompatibility & GetCheckCompatibility-metoder för IWorkbookSettings-klassen. Dessa metoder är användbara för att få eller sätta kompatibilitetskontrollen som indikerar om API:et ska kontrollera kompatibiliteten vid sparande av arbetsbok. Standardvärdet är sant och kan sättas till falskt om applikationskravet är att inte kontrollera kompatibiliteten.
### **Lade till GetILightCellsDataHandler & SetILightCellsDataHandler-metoder**
Aspose.Cells for C++ har nu exponerat GetILightCellsDataHandler & SetILightCellsDataHandler-metoder för ILoadOptions-klassen. Dessa metoder anger datahanteraren för bearbetning av cellsdata vid läsning av mallfilen.
### **Lade till GetCultureInfo & SetCultureInfo-metoder**
Aspose.Cells for C++ har exponerat GetCultureInfo & SetCultureInfo-metoder för ILoadOptions-klassen. Dessa metoder kan få eller sätta systemets kulturinfo vid tidpunkten för filinläsning.
## **Borttagen API:er**
### **Tog bort ICells::MaxDataRowInColumn-metoden**
Det rekommenderas att använda ICells::GetLastDataRow-metoden istället.
### **Tog bort ICell::GetConditionalIStyle-metoden**
Det rekommenderas att använda ICell::GetIConditionalFormattingResult-metoden istället.
### **Tog bort IPageSetup::GetDraft & SetDraft-metoder**
Det rekommenderas att använda IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft-metoderna istället.

{{% alert color="primary" %}} 

Med släppet av Aspose.Cells for C++ 17.1.0 har vi tagit bort några metoder som inte användes och därför ansågs onödiga. Här är listan över alla sådana metoder.

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType-metoder
- IRange::ToString Metod
- IRow::Equals Metod
- IWorkbook::SetISettings Metod
- ICell::ToString() Metod
- ICell::Equals(ObjectPtr) Metod
- ICell::GetHashCode Metod
- IWorksheet::ToString Metod

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
