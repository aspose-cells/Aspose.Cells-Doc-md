---
title: Estensioni Web  Componenti aggiuntivi di Office
type: docs
weight: 120
url: /it/java/web-extensions-office-add-ins/
---

Le estensioni Web estendono le applicazioni di Office e interagiscono con i contenuti nei documenti di Office. Le estensioni Web aggiungono funzionalità aggiuntive al client di Office per migliorare l'esperienza dell'utente e la produttività.

Aspose.Cells fornisce anche la capacità di lavorare con le estensioni Web.

## **Aggiungi estensione Web**

È possibile aggiungere estensioni Web (Componenti aggiuntivi di Office) in Excel facendo clic sulla scheda **Inserisci** e quindi facendo clic sul collegamento **Store**/**Ottieni componenti aggiuntivi**. Nella casella dei componenti aggiuntivi, cerca il componente aggiuntivo desiderato e aggiungilo.

Aspose.Cells fornisce anche la funzione di aggiungere estensioni Web usando le classi WebExtension e WebExtensionTaskPane. Il seguente codice di esempio dimostra l'uso delle classi WebExtension e WebExtensionTaskPane per aggiungere un'estensione Web al file Excel. Si prega di vedere il [file Excel di output](AddWebExtension_Out.xlsx) generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Accesso alle informazioni sull'estensione Web**

Aspose.Cells fornisce la possibilità di accedere alle informazioni delle estensioni Web nel file Excel. Il seguente esempio di codice dimostra come accedere alle informazioni dell'estensione Web caricando il [file Excel di esempio](WebExtensionsSample.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **Output della console**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
