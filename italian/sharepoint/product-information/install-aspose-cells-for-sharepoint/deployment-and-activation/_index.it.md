---
title: Distribuzione e attivazione
type: docs
weight: 20
url: /it/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[Installazione di Aspose.Cells per SharePoint](/cells/it/sharepoint/installing-aspose-cells-for-sharepoint/) ti guida attraverso il processo di installazione. Questo articolo spiega quale processo di installazione viene distribuito e attivato.

{{% /alert %}} 
### **Distribuzione**
Aspose.Cells per SharePoint esegue le azioni seguenti durante la distribuzione:

1.  Installa**Aspose.Cells.SharePoint.dll** nella Global Assembly Cache e aggiunge una voce SafeControl al file**web.config** file.
1. Installa il manifesto delle funzionalità e altri file necessari nelle directory appropriate.
1. Registra la funzionalità nel database di SharePoint e la rende disponibile per l'attivazione nell'ambito della funzionalità.
### **Attivazione**
 Aspose.Cells per SharePoint viene fornito come funzionalità a livello di sito (raccolta siti) e può essere attivato e disattivato nelle raccolte siti.

Durante l'attivazione, la funzionalità apporta alcune modifiche alla directory virtuale dell'applicazione Web padre della raccolta siti:

1. Aggiunge la pagina delle impostazioni di conversione al file della mappa del sito.
1. Copia i file di risorse necessari nella cartella App_GlobalResources nella directory virtuale.
