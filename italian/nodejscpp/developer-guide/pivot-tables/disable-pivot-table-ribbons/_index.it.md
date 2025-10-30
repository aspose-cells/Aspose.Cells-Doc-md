---
title: Disabilita le barre delle tabelle pivot
type: docs
weight: 90
url: /it/nodejs-cpp/disable-pivot-table-ribbons/
description: Come disattivare le barre degli strumenti della tabella pivot con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells per Node.js Excel, libreria Excel Node.js, Disattivare le barre degli strumenti della tabella pivot usando Aspose.Cells for Node.js via C++ Excel Library.
---

{{% alert color="primary" %}}

I rapporti basati sulle tabelle pivot sono utili ma soggetti a errori se gli utenti target non hanno conoscenze approfondite di Excel per configurare tali rapporti. In questi casi, le organizzazioni vorranno limitare la possibilità agli utenti di modificare un rapporto basato su tabella pivot. Funzionalità comuni come aggiungere filtri, slicer, campi o cambiare l'ordine di alcuni elementi nel rapporto non sono generalmente raccomandate per tutti gli utenti. D'altro canto, questi utenti devono poter aggiornare il rapporto e usare filtri o slicer esistenti. Aspose.Cells for Node.js via C++ ha fornito questa possibilità agli sviluppatori per limitare le modifiche degli utenti durante la creazione di rapporti. A tal fine, Excel offre una funzione per disattivare la barra degli strumenti della tabella pivot e la stessa funzione è fornita da Aspose.Cells for Node.js via C++, cioè lo sviluppatore può disabilitare la barra che contiene i controlli per modificare questi rapporti.

{{% /alert %}}

## **Come disabilitare la barra degli strumenti della tabella pivot con Aspose.Cells for Node.js via C++**

Il seguente codice dimostra questa funzionalità accedendo a una tabella pivot da un foglio e impostando [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) su **false**. Il file di esempio della tabella pivot può essere scaricato da questo [link](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
