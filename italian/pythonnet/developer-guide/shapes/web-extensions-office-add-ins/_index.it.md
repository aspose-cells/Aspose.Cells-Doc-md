---
title: Estensioni Web  Componenti aggiuntivi di Office
type: docs
weight: 130
url: /it/python-net/web-extensions-office-add-ins/
---

Le estensioni Web estendono le applicazioni di Office e interagiscono con i contenuti nei documenti di Office. Le estensioni Web aggiungono funzionalità aggiuntive al client di Office per migliorare l'esperienza dell'utente e la produttività.

Aspose.Cells per Python via .NET fornisce anche la possibilità di lavorare con Web Extensions.

## **Aggiungi estensione Web**

Potresti aggiungere Estensioni Web (componenti aggiuntivi di Office) in Excel facendo clic sulla scheda **Inserisci** e poi facendo clic sul collegamento **Archivio**/**Ottieni componenti aggiuntivi**. Nella casella dei componenti aggiuntivi, cerca il componente aggiuntivo desiderato e aggiungilo.

Aspose.Cells per Python via .NET offre anche la funzione di aggiungere Web Extensions utilizzando le classi [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). Il seguente esempio di codice dimostra l'uso delle classi [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) per aggiungere una web extension al file Excel. Si prega di vedere il [file Excel di output](89849869.xlsx) generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Accesso alle informazioni sull'estensione Web**

Aspose.Cells per Python via .NET fornisce la possibilità di accedere alle informazioni delle Web Extensions nel file Excel. Il seguente esempio di codice dimostra come accedere alle informazioni delle web extension caricando il [file Excel di esempio](89849870.xlsx). Si prega di vedere l'output della console generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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
