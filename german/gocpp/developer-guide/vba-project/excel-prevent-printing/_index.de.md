---  
title: So verhindern Sie, dass Benutzer die Excel Datei mit Golang via C++ drucken  
linktitle: Wie verhindert man, dass Benutzer eine Excel Datei drucken  
type: docs  
weight: 600  
url: /de/go-cpp/how-to-prevent-printing-excel/  
description: Erfahren Sie, wie Sie das Drucken von Excel durch die API Aspose.Cells for C++ verhindern.  
keywords: Excel Druck, Excel Druck verhindern, wie man das Drucken von Excel verhindert, Excel Druck verhindern, das Drucken des gesamten Arbeitsmappens mit VBA verhindern  
---  

## **Mögliche Verwendungsszenarien**  
In unserer täglichen Arbeit können wichtige Informationen in der Excel-Datei enthalten sein; um die Verbreitung interner Daten zu verhindern, erlaubt die Firma keinen Druck. Dieses Dokument zeigt, wie Sie andere vom Drucken von Excel-Dateien abhalten können.  

## **Wie man das Drucken einer Datei in MS-Excel verhindert**  
Sie können den folgenden VBA-Code anwenden, um Ihre spezifische Datei vor dem Drucken zu schützen.  
1. Öffnen Sie Ihre Arbeitsmappe, die Sie anderen nicht erlauben möchten zu drucken.  
1. Wählen Sie die Registerkarte **Entwicklertools** im Excel-Ribbon und klicken Sie auf die Schaltfläche **Code anzeigen** im Abschnitt **Steuerelemente**. Alternativ können Sie die Tasten ALT + F11 drücken, um das Microsoft Visual Basic for Applications Fenster zu öffnen.  
<br>  
<img src="1.png" width=70% />  
1. Doppelklicken Sie im linken Projekt-Explorer auf ThisWorkbook, um das Modul zu öffnen und einige VBA-Codes hinzuzufügen.  
<br>  
<img src="2.png" width=70% />  
1. Speichern und schließen Sie dieses Codefenster, kehren Sie zum Arbeitsbuch zurück, und wenn Sie die Beispiel-Datei drucken, wird dies nicht erlaubt, und Sie erhalten folgende Warnmeldung:  
<br>  
<img src="3.png" width=70% />  

## **Wie man Benutzer am Drucken von Excel-Datei mit Aspose.Cells for C++ hindert**  

Das folgende Beispiel zeigt, wie man das Drucken einer Excel-Datei durch Benutzer verhindert:  

1. Laden Sie die [Beispieldatei](sample.xlsx).  
1. Holen Sie sich das VbaModuleCollection-Objekt aus der VbaProject-Eigenschaft des Arbeitsbuchs.  
1. Holen Sie das VbaModule-Objekt über den Namen "ThisWorkbook".  
1. Setzen Sie die Eigenschaften des VbaModule-Codes.  
1. Speichern Sie die Beispieldatei im [xlsm-Format](out.xlsm).  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcelPreventPrinting.go" >}}
