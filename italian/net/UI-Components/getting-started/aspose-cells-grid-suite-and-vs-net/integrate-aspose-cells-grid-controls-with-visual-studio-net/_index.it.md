---
title: Integra i controlli Aspose.Cells Grid con Visual Studio.NET
type: docs
weight: 10
url: /it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: Questo articolo descrive come utilizzare i controlli GridWeb e GridDesktop in Visual Studio .NET.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Gli sviluppatori di Visual Studio.NET possono trascinare facilmente i controlli dalla **Toolbox** su un modulo Windows o Web. Aspose.Cells Grid suite può essere scaricato con un programma di installazione MSI o come pacchetto di DLL. Questo articolo spiega cosa fare per assicurarsi che i controlli Aspose.Cells.Grid possano essere utilizzati in Visual Studio.NET quando viene installato utilizzando le DLL anziché il programma di installazione.

{{% /alert %}} 
## **Integra i controlli Aspose.Cells Grid con Visual Studio.NET**
Per integrare i controlli della griglia Aspose.Cells con Visual Studio.NET:

1. Aprire la Toolbox.
1. Selezionare la scheda Generale (o qualsiasi altra scheda in cui si desidera aggiungere i controlli).
1. Fare clic con il pulsante destro del mouse sulla scheda Generale.
1. Su Visual Studio.NET, selezionare **Scegli elementi** dal menu. Si aprirà la finestra di dialogo Personalizza Toolbox (Questo processo è più o meno lo stesso per le nuove IDE di VS.NET (ad es. VS.NET 2013/2015 o successive)).
1. Fare clic su **Sfoglia** e individuare i file Aspose.Cells.GridDesktop.dll e Aspose.Cells.GridWeb.dll.
1. Selezionare i file DLL e quindi fare clic su **Apri**. La finestra di dialogo Personalizza Toolbox conterrà ora i controlli della suite Aspose.Cells Grid. I controlli appena aggiunti saranno evidenziati dalla finestra di dialogo.
1. Fare clic su **OK** per aggiungere i controlli alla Toolbox di Visual Studio.NET.

I controlli della griglia Aspose.Cells saranno stati aggiunti alla scheda **Generale** della Toolbox. Solo il controllo GridWeb non è attivo. Ciò è dovuto al fatto che stiamo lavorando su un'applicazione Windows Forms. GridWeb è disponibile solo quando si lavora su Web Forms, mentre GridDesktop può essere utilizzato solo con Windows Forms.
