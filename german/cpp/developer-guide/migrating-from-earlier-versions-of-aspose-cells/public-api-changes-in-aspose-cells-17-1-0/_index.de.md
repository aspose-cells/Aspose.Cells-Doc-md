---
title: Öffentlich API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 20
url: /de/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.12.0 zu 17.1.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für benannte Bereiche**
 Aspose.Cells for C++ unterstützt jetzt sowohl die Erstellung als auch die Manipulation der benannten Bereiche. Das folgende Code-Snippet zeigt, wie einfach es ist, Aspose.Cells for C++ API zu verwenden[benannte Bereiche erstellen](/cells/de/cpp/create-named-range-in-a-workbook/).

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

 Neben der Erstellung neuer benannter Bereiche unterstützen Aspose.Cells for C++ APIs auch die Bearbeitung vorhandener benannter Bereiche. Das folgende Code-Snippet verwendet die Aspose.Cells for C++ API zu[manipuliert einen bestehenden benannten Bereich](/cells/de/cpp/manipulate-named-range-in-a-workbook/).

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
### **ICells::LinkToXmlMap-Methode hinzugefügt**
Die LinkToXmlMap-Methode wurde der ICells-Klasse hinzugefügt, die beim Verknüpfen einer XML-Karte nützlich ist.
### **ICells::ImportCSV-Methode hinzugefügt**
Die ImportCSV-Methode wurde der ICells-Klasse hinzugefügt, was beim Importieren einer CSV-Datei in die Zellen eines Arbeitsblatts nützlich ist.
### **ICells::ImportTwoDimensionArray-Methode hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der ICells-Klasse hinzugefügt, was beim Importieren eines zweidimensionalen Arrays von Daten in ein Arbeitsblatt nützlich ist.
### **IWorksheet::GetIProtectedRangeCollection-Methode hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der Klasse IWorksheet hinzugefügt, die beim Abrufen der Sammlung von IProtectedRange-Objekten hilfreich ist.
### **IWorksheet::GetIProtectedRangeCollection-Methode hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der Klasse IWorksheet hinzugefügt, die beim Abrufen der Bearbeitungsbereichssammlung aus dem Arbeitsblatt nützlich ist.
### **IWorkbookSettings::ClearPivottables-Methode hinzugefügt**
Die ClearPivottables-Methode wurde der IWorkbookSettings-Klasse hinzugefügt, die beim Löschen aller Pivot-Tabellen aus einer bestimmten Tabelle hilfreich ist.
### **IWorksheetCollection::CreateIRange-Methode hinzugefügt**
Die CreateIRange-Methode wurde der IWorksheetCollection-Klasse hinzugefügt, die beim Erstellen eines Objekts der IRange hilfreich ist, indem Zellreferenzen im Zeichenfolgenformat übergeben werden.
### **IExternalLink::IsVisible-Methode hinzugefügt**
Die IsVisible-Methode ruft den Sichtbarkeitsstatus eines externen Links in der Excel-Anwendung ab.
### **GetScaleCrop- und SetScaleCrop-Methoden hinzugefügt**
Aspose.Cells for C++ 17.1.0 hat die Methoden GetScaleCrop und SetScaleCrop für die Klasse IBuiltInDocumentPropertyCollection verfügbar gemacht. Diese Methoden sind nützlich, um die ScaleCrop-Eigenschaft abzurufen oder festzulegen, die den Anzeigemodus der Miniaturansicht des Dokuments angibt.
### **GetLinksUpToDate- und SetLinksUpToDate-Methoden hinzugefügt**
Aspose.Cells for C++ 17.1.0 hat die Methoden „GetLinksUpToDate“ und „SetLinksUpToDate“ für die Klasse „IBuiltInDocumentPropertyCollection“ verfügbar gemacht. Diese Methoden sind nützlich, um die LinkUpToDate-Eigenschaft abzurufen oder festzulegen, die angibt, ob Hyperlinks in einem Dokument aktuell sind.
### **GetAbsolutePath- und SetAbsolutePath-Methoden hinzugefügt**
Aspose.Cells for C++ 17.1.0 hat die Methoden „GetAbsolutePath“ und „SetAbsolutePath“ für die Klasse „IWorkbook“ verfügbar gemacht. Diese Methoden sind nützlich, um den absoluten Pfad der Datei zu erhalten oder festzulegen, der nur für externe Links verwendet werden kann.
### **GetFormula- und SetFormula-Methoden hinzugefügt**
Diese Version von Aspose.Cells for C++ hat die GetFormula- und SetFormula-Methoden für die IListColumn-Klasse verfügbar gemacht. Diese Methoden sind nützlich, um die Formel einer Listenspalte zu erhalten oder festzulegen.
### **GetCheckCompatibility- und SetCheckCompatibility-Methoden hinzugefügt**
Diese Version von Aspose.Cells for C++ hat die Methoden GetCheckCompatibility und GetCheckCompatibility für die Klasse IWorkbookSettings verfügbar gemacht. Diese Methoden sind nützlich, um die Kompatibilitätsprüfungseigenschaft abzurufen oder festzulegen, die angibt, ob API die Kompatibilität beim Speichern der Arbeitsmappe prüfen soll. Der Standardwert ist „true“ und kann auf „false“ gesetzt werden, wenn die Anforderung der Anwendung nicht darin besteht, die Kompatibilität zu prüfen.
### **GetILightCellsDataHandler- und SetILightCellsDataHandler-Methoden hinzugefügt**
Aspose.Cells for C++ hat jetzt die Methoden GetILightCellsDataHandler und SetILightCellsDataHandler für die Klasse ILoadOptions verfügbar gemacht. Diese Methoden bezeichnen den Datenhandler zum Verarbeiten von Zellendaten beim Lesen der Vorlagendatei.
### **GetCultureInfo- und SetCultureInfo-Methoden hinzugefügt**
Aspose.Cells for C++ hat die GetCultureInfo- und SetCultureInfo-Methoden für die ILoadOptions-Klasse verfügbar gemacht. Diese Methoden können die Systemkulturinformationen beim Laden der Datei abrufen oder festlegen.
## **Entfernte APIs**
### **ICells::MaxDataRowInColumn-Methode entfernt**
Es wird empfohlen, stattdessen die Methode ICells::GetLastDataRow zu verwenden.
### **ICell::GetConditionalIStyle-Methode entfernt**
Es wird empfohlen, stattdessen die Methode ICell::GetIConditionalFormattingResult zu verwenden.
### **IPageSetup::GetDraft- und SetDraft-Methoden entfernt**
Es wird empfohlen, stattdessen die Methoden IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft zu verwenden.

{{% alert color="primary" %}} 

Mit der Veröffentlichung von Aspose.Cells for C++ 17.1.0 haben wir einige Methoden entfernt, die nicht verwendet wurden und daher als unnötig erachtet wurden. Hier ist die Liste aller dieser Methoden.

- IPaneCollection::GetAcitvePaneType- und SetAcitvePaneType-Methoden
- IRange::ToString-Methode
- IRow::Equals-Methode
- IWorkbook::SetISettings-Methode
- ICell::ToString()-Methode
- ICell::Equals(ObjectPtr)-Methode
- ICell::GetHashCode-Methode
- IWorksheet::ToString-Methode

{{% /alert %}}
