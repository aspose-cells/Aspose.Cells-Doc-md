---
title: Öffentliche API Änderungen in Aspose.Cells 17.1.0
type: docs
weight: 20
url: /de/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 16.12.0 auf 17.1.0, die für Modulentwickler/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für benannte Bereiche**
Aspose.Cells for C++ unterstützt jetzt die Erstellung sowie die Manipulation der benannten Bereiche. Der folgende Code-Schnipsel zeigt, wie einfach es ist, die Aspose.Cells for C++ API zum [Erstellen benannter Bereiche](/cells/de/cpp/create-named-range-in-a-workbook/) zu verwenden.

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

Neben dem Erstellen neuer benannter Bereiche unterstützen die Aspose.Cells for C++-APIs auch die Manipulation bestehender benannter Bereiche. Der folgende Code-Schnipsel verwendet die Aspose.Cells for C++-API zum [Manipulieren eines vorhandenen benannten Bereichs](/cells/de/cpp/manipulate-named-range-in-a-workbook/).

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
### **Methode ICells::LinkToXmlMap hinzugefügt**
Die Methode LinkToXmlMap wurde der Klasse ICells hinzugefügt, was nützlich ist, um eine XML-Map zu verknüpfen.
### **Methode ICells::ImportCSV hinzugefügt**
Die Methode ImportCSV wurde der Klasse ICells hinzugefügt, um eine CSV-Datei in die Zellen eines Arbeitsblatts zu importieren.
### **Methode ICells::ImportTwoDimensionArray hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der Klasse ICells hinzugefügt, um ein zweidimensionales Datenarray in ein Arbeitsblatt zu importieren.
### **Methode IWorksheet::GetIProtectedRangeCollection hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der Klasse IWorksheet hinzugefügt, um die Sammlung von IProtectedRange-Objekten abzurufen.
### **Methode IWorksheet::GetIProtectedRangeCollection hinzugefügt**
Die Methode GetIProtectedRangeCollection wurde der Klasse IWorksheet hinzugefügt, um die Bearbeitungsbereichssammlung aus dem Arbeitsblatt abzurufen.
### **Methode IWorkbookSettings::ClearPivottables hinzugefügt**
Die Methode ClearPivottables wurde der Klasse IWorkbookSettings hinzugefügt, um alle Pivot-Tabellen aus einer bestimmten Tabelle zu löschen.
### **Hinzugefügte CreateIRange-Methode für IWorksheetCollection**
Die CreateIRange-Methode wurde der Klasse IWorksheetCollection hinzugefügt, die nützlich ist, um ein Objekt von IRange zu erstellen, indem Zellenreferenzen im Zeichenfolgenformat übergeben werden.
### **Hinzugefügte IsVisible-Methode für IExternalLink**
Die IsVisible-Methode ruft den Sichtbarkeitsstatus eines externen Links in der Excel-Anwendung ab.
### **Hinzugefügte GetScaleCrop- und SetScaleCrop-Methoden**
Aspose.Cells for C++ 17.1.0 hat die GetScaleCrop- und SetScaleCrop-Methoden für die IBuiltInDocumentPropertyCollection-Klasse freigelegt. Diese Methoden sind nützlich, um die ScaleCrop-Eigenschaft abzurufen oder festzulegen, die den Anzeigemodus des Dokument-Thumbnail angibt.
### **Hinzugefügte GetLinksUpToDate- und SetLinksUpToDate-Methoden**
Aspose.Cells for C++ 17.1.0 hat die GetLinksUpToDate- und SetLinksUpToDate-Methoden für die IBuiltInDocumentPropertyCollection-Klasse freigelegt. Diese Methoden sind nützlich, um die LinkUpToDate-Eigenschaft abzurufen oder festzulegen, die angibt, ob Hyperlinks in einem Dokument auf dem neuesten Stand sind.
### **Hinzugefügte GetAbsolutePath- und SetAbsolutePath-Methoden**
Aspose.Cells for C++ 17.1.0 hat die GetAbsolutePath- und SetAbsolutePath-Methoden für die IWorkbook-Klasse freigelegt. Diese Methoden sind nützlich, um den absoluten Pfad der Datei abzurufen oder festzulegen, der nur für externe Links verwendet werden kann.
### **Hinzugefügte GetFormula- und SetFormula-Methoden**
Diese Version von Aspose.Cells for C++ hat die GetFormula- und SetFormula-Methoden für die IListColumn-Klasse freigelegt. Diese Methoden sind nützlich, um die Formel einer Listen-Spalte abzurufen oder festzulegen.
### **Hinzugefügte GetCheckCompatibility- und SetCheckCompatibility-Methoden**
Diese Version von Aspose.Cells for C++ hat die GetCheckCompatibility- und GetCheckCompatibility-Methoden für die IWorkbookSettings-Klasse freigelegt. Diese Methoden sind nützlich, um die Kompatibilitätsprüfeigenschaft abzurufen oder festzulegen, die angibt, ob die API die Kompatibilität beim Speichern der Arbeitsmappe überprüfen soll. Der Standardwert ist true und kann auf false gesetzt werden, wenn keine Kompatibilitätsprüfung erforderlich ist.
### **Hinzugefügte GetILightCellsDataHandler- und SetILightCellsDataHandler-Methoden**
Aspose.Cells for C++ hat nun die GetILightCellsDataHandler- und SetILightCellsDataHandler-Methoden für die ILoadOptions-Klasse freigelegt. Diese Methoden geben den Datenhandler zur Verarbeitung von Zellendaten beim Lesen der Vorlagendatei an.
### **Hinzugefügte GetCultureInfo- und SetCultureInfo-Methoden**
Aspose.Cells for C++ hat die GetCultureInfo- und SetCultureInfo-Methoden für die ILoadOptions-Klasse freigelegt. Diese Methoden können die Systemkulturinfo zum Zeitpunkt des Dateiladens abrufen oder festlegen.
## **Entfernte APIs**
### **Entfernte MaxDataRowInColumn-Methode für ICells**
Es wird empfohlen, die Methode ICells::GetLastDataRow zu verwenden.
### **Entfernte Methode ICell::GetConditionalIStyle**
Es wird empfohlen, die Methode ICell::GetIConditionalFormattingResult zu verwenden.
### **Entfernte Methoden IPageSetup::GetDraft & SetDraft**
Es wird empfohlen, die Methoden IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft zu verwenden.

{{% alert color="primary" %}} 

Mit der Veröffentlichung von Aspose.Cells for C++ 17.1.0 haben wir einige nicht verwendete Methoden entfernt, die daher als unnötig angesehen wurden. Hier ist eine Liste aller solcher Methoden.

- IPaneCollection::GetAcitvePaneType & SetAcitvePaneType Methoden
- IRange::ToString Methode
- IRow::Equals Methode
- IWorkbook::SetISettings Methode
- ICell::ToString() Methode
- ICell::Equals(ObjectPtr) Methode
- ICell::GetHashCode Methode
- IWorksheet::ToString Methode

{{% /alert %}}
