---
title: Uso di Aspose.Cells su piattaforme a 32 e 64 bit
type: docs
weight: 10
url: /it/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells è un componente puro di .NET che può semplificare il processo di distribuzione utilizzando la distribuzione XCOPY. Per installare Aspose.Cells, è sufficiente copiare l'assembly del componente (Aspose.Cells.dll) in una directory per la tua applicazione: l'applicazione può iniziare a usarlo immediatamente. Questo è possibile grazie alla natura auto-descrittiva dei componenti .NET. Questo tipo di distribuzione non ha alcun impatto sul processo di installazione.

{{% /alert %}} 
## **Implementazione**
Aspose.Cells supporta sia ambienti a 32 bit che a 64 bit. Quando si installa il Aspose.Cells for .NET componente utilizzando l'installatore MSI di Aspose.Cells, diversi file DLL vengono aggiunti a diverse cartelle nella cartella Aspose.Cells ${installation_Path}. Vedi la descrizione nella tabella su quale cartella contiene le librerie che è necessario utilizzare con una particolare versione del framework .NET.

|**Cartella**|**Descrizione**|
| :- | :- |
|net2.0|Contiene le librerie da utilizzare con .NET Framework 2.0, 3.0, 3.5, 4.0 e Mono. Queste sono le librerie che si dovrebbero normalmente utilizzare per sia ambienti a 32 bit che a 64 bit.|
|net2.0_AuthenticodeSigned|Come sopra, ma le librerie sono firmate digitalmente con Authenticode. Le librerie firmate possono caricarsi più lentamente rispetto a quelle senza Authenticode.|
|net3.5_ClientProfile|Contiene le librerie da utilizzare con .NET Framework 3.5 o 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|Come sopra, ma le librerie sono firmate digitalmente con Authenticode. Le librerie firmate possono caricarsi più lentamente rispetto a quelle senza Authenticode.|
|net3.5|Contiene le librerie da utilizzare con .NET Framework 3.5 o 4.0.|
|net3.5_AuthenticodeSigned|Come sopra, ma le librerie sono firmate digitalmente con Authenticode. Le librerie firmate possono caricarsi più lentamente rispetto a quelle senza Authenticode.|
|net4.0|Contiene le librerie da utilizzare con .NET Framework 4.0 e 4.5.|
|netStandard|Contiene le librerie da utilizzare con .Net Standard 2.0|
|netcoreapp2.1|Contiene le librerie da utilizzare con .Net core 2.1|
|Xamarin.iOS|Contiene le librerie da utilizzare con Xamarin.iOS|
|Xamarin.Android|Contiene le librerie da utilizzare con Xamarin.Android|
|net5.0|Contiene le librerie da utilizzare con .net5.0.|
|net6.0|Contiene le librerie da utilizzare con .net6.0.|
|net8.0|Contiene assemblaggi da usare con .net8.0.|
|net9.0|Contiene assemblaggi da usare con .net9.0.|

{{% alert color="primary" %}} 

In VS.NET (ad esempio 2005, 2008, 2010, 2012 ecc.) projects, quando si aggiunge un riferimento a Aspose.Cells, la finestra Aggiungi Riferimento si riferisce ai file Aspose.Cells.dll nella cartella net2.0 o net3.5 rispettivamente. (Per ulteriori informazioni, leggere Riferimento di Aspose.Cells da un progetto .NET.) Si può cambiare il riferimento alla libreria in base al proprio ambiente. Si prega di notare che se il framework di destinazione del progetto è .NET Framework 3.5/4 Client Profile, utilizzare il file di componente Aspose.Cells.dll situato nella cartella net_ClientProfile.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
