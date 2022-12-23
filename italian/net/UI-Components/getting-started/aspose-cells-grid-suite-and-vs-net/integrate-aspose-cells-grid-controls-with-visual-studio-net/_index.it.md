---
title: Integra i controlli griglia Aspose.Cells con Visual Studio.NET
type: docs
weight: 10
url: /it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Gli sviluppatori di Visual Studio.NET possono facilmente trascinare i controlli dal file**Cassetta degli attrezzi** su un modulo Windows o Web. Aspose.Cells Grid suite può essere scaricato con un programma di installazione MSI o come set di pacchetti DLL. Questo articolo spiega cosa fare per assicurarsi che i controlli Aspose.Cells.Grid possano essere usati in Visual Studio.NET quando viene installato usando le DLL invece del programma di installazione.

{{% /alert %}} 
## **Integra i controlli griglia Aspose.Cells con Visual Studio.NET**
Per integrare i controlli griglia Aspose.Cells con Visual Studio.NET:

1. Apri la casella degli strumenti.
1. Seleziona la scheda Generale (o qualsiasi altra scheda a cui desideri aggiungere controlli).
1. Fare clic con il pulsante destro del mouse sulla scheda Generale.
1.  In Visual Studio.NET 2003: selezionare**Aggiungi/Rimuovi elementi** dal menù.
1. In Visual Studio.NET 2005 selezionare**Scegli Articoli** dal menù. Verrà visualizzata la finestra di dialogo Personalizza casella degli strumenti (questo processo è più o meno lo stesso per gli IDE VS.NET più recenti (ad es. VS.NET 2013/2015 o successivi)).
1.  Clic**Navigare** e individuare i file Aspose.Cells.GridDesktop.dll e Aspose.Cells.GridWeb.dll.
1.  Selezionare le DLL e quindi fare clic**Aprire**. La finestra di dialogo Personalizza casella degli strumenti ora conterrà i controlli di Aspose.Cells Grid Suite. I nuovi controlli aggiunti verranno evidenziati dalla finestra di dialogo.
1.  Clic**OK** per aggiungere i controlli alla casella degli strumenti di Visual Studio.NET.

 i controlli della griglia Aspose.Cells saranno stati aggiunti alla casella degli strumenti**Generale** scheda. Solo il controllo GridWeb non è attivo. Questo perché stiamo lavorando su un'applicazione di moduli Windows. GridWeb è disponibile solo quando si lavora su Web Form, mentre GridDesktop può essere utilizzato solo con i moduli Windows.
