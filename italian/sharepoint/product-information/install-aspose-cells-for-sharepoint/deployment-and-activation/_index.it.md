---
title: Implementazione e Attivazione
type: docs
weight: 20
url: /it/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[L'installazione di Aspose.Cells for SharePoint](/cells/it/sharepoint/installing-aspose-cells-for-sharepoint/) ti guida attraverso il processo di installazione. Questo articolo spiega come viene distribuito e attivato il processo di installazione.

{{% /alert %}} 
### **Implementazione**
Aspose.Cells for SharePoint esegue le seguenti azioni durante l'implementazione:

1. Installa **Aspose.Cells.SharePoint.dll** nel Global Assembly Cache e aggiunge un'entrata SafeControl nel file **web.config**.
1. Installa il manifesto della funzionalità e altri file necessari nelle directory appropriate.
1. Registra la funzionalità nel database di SharePoint e la rende disponibile per l'attivazione nel contesto della funzionalità.
### **Attivazione**
Aspose.Cells for SharePoint è confezionato come una funzionalità a livello di sito (raccolta siti) e può essere attivato e disattivato nelle raccolte siti. 

Durante l'attivazione, la funzionalità apporta alcune modifiche alla directory virtuale dell'applicazione Web genitore della raccolta siti:

1. Aggiunge una pagina di impostazioni di conversione al file mappa del sito.
1. Copia i file di risorse necessari nella cartella App_GlobalResources nella directory virtuale.
