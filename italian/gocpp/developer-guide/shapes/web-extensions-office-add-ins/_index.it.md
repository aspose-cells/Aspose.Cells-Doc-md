---
title: Extension web  Componenti aggiuntivi di Office con Golang tramite C++
linktitle: Estensioni Web  Componenti aggiuntivi di Office
type: docs
weight: 130
url: /it/go-cpp/web-extensions-office-add-ins/
description: Impara come aggiungere e accedere alle estensioni web (Componenti aggiuntivi di Office) nei file Excel usando Aspose.Cells con Golang tramite C++.
---

Le Web Extensions estendono le applicazioni Office e interagiscono con il contenuto nei documenti Office. Le Web Extensions aggiungono funzionalità aggiuntive ai client Office per migliorare l’esperienza utente e la produttività.

Aspose.Cells fornisce anche la capacità di lavorare con le estensioni Web.

## **Aggiungi estensione Web**

Puoi aggiungere Web Extensions (Office Add-in) in Excel cliccando sulla scheda **Inserisci** e poi cliccando sul collegamento **Store**/**Ottieni componenti aggiuntivi**. Nella casella dei componenti aggiuntivi, cerca l’addin desiderato e aggiungilo.

Aspose.Cells offre anche la funzione di aggiungere Web Extensions utilizzando le classi [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). Il seguente esempio di codice dimostra l’uso delle classi [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) per aggiungere un’estensione web a un file Excel. Si prega di consultare il [file Excel di output](89849869.xlsx) generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Accesso alle informazioni sull'estensione Web**

Aspose.Cells fornisce la possibilità di accedere alle informazioni delle Web Extensions in un file Excel. Il seguente esempio di codice dimostra come accedere alle informazioni delle Web Extensions caricando il [file Excel di esempio](89849870.xlsx). Si prega di consultare l’output della console generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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
