---
title: Utilizzo di Aspose.Cells su piattaforme a 32 e 64 bit
type: docs
weight: 10
url: /it/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells è un componente .NET puro che può semplificare il processo di distribuzione utilizzando la distribuzione XCOPY. Per installare Aspose.Cells, è sufficiente copiare l'assieme del componente (Aspose.Cells.dll) in una directory per la propria applicazione: l'applicazione può iniziare a utilizzarlo immediatamente. Ciò è possibile grazie alla natura autodescrittiva dei componenti .NET. Questo tipo di distribuzione ha anche un impatto zero sul processo di installazione.

{{% /alert %}} 
## **Distribuzione**
Aspose.Cells supporta sia ambienti a 32 bit che a 64 bit. Quando si installa il componente Aspose.Cells for .NET utilizzando il programma di installazione MSI Aspose.Cells, diverse DLL vengono aggiunte a cartelle diverse nelle cartelle Aspose.Cells ${installation_Path}. Vedi la descrizione nella tabella quale cartella contiene gli assembly che devi usare con una particolare versione del Framework .NET.

|**Cartella**|**Descrizione**|
|:- |:- |
|net2.0|Contiene gli assembly da utilizzare con .NET Framework 2.0, 3.0, 3.5, 4.0 e Mono. Questi sono gli assembly da utilizzare normalmente sia per gli ambienti a 32 bit che per quelli a 64 bit.|
|net2.0_AuthenticodeSigned|Come sopra, ma gli assembly sono firmati digitalmente con Authenticode. Gli assembly firmati possono essere caricati più lentamente che senza Authenticode|
|net3.5_ClientProfile|Contiene assembly da utilizzare con .NET Framework 3.5 o 4.0 Client Profile.|
|netto3.5_Profilo del cliente_AuthenticodeSigned|Come sopra, ma gli assembly sono firmati digitalmente con Authenticode. Gli assembly firmati possono essere caricati più lentamente che senza Authenticode.|
|netto3.5|Contiene assembly da utilizzare con .NET Framework 3.5 o 4.0.|
|net3.5_AuthenticodeSigned|Come sopra, ma gli assembly sono firmati digitalmente con Authenticode. Gli assembly firmati possono essere caricati più lentamente che senza Authenticode.|
|net4.0|Contiene assembly da utilizzare con .NET Framework 4.0 e 4.5.|
|netStandard|Contiene assembly da usare con .Net Standard 2.0|
|netcoreapp2.1|Contiene assembly da utilizzare con .Net core 2.1|
|Novell. iOS|Contiene assembly da usare con Xamarin.iOS|
|Xamarin.Android|Contiene assembly da usare con Xamarin.Android|
|netto5.0|Contiene assembly da usare con .net5.0.|
|net6.0|Contiene assembly da utilizzare con .net6.0.|
{{% alert color="primary" %}} 

Nei progetti VS.NET (ad esempio 2005, 2008, 2010, 2012 ecc.), quando si aggiunge un riferimento a Aspose.Cells, la finestra di dialogo Aggiungi riferimento fa riferimento rispettivamente ai file Aspose.Cells.dll nelle cartelle net2.0 o net3.5. (Per ulteriori riferimenti, leggere Riferimento a Aspose.Cells da un progetto .NET.) È possibile modificare il riferimento alla libreria in base al proprio ambiente. Si noti che se il framework di destinazione del progetto è .NET Framework 3.5/4 Client Profile, utilizzare il file del componente Aspose.Cells.dll che si trova nella cartella net_ClientProfile.

{{% /alert %}}
