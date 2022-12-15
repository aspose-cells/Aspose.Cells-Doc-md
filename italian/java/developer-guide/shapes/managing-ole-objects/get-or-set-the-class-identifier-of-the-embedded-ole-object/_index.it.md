---
title: Ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato
type: docs
weight: 920
url: /it/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells fornisce il[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)proprietà che è possibile utilizzare per ottenere o impostare l'identificatore di classe di un oggetto ole incorporato. Gli identificatori di classi di oggetti obsoleti sono in realtà GUID, ovvero identificatori univoci globali. Il GUID è sempre lungo 16 byte, pertanto anche gli identificatori di classe sono lunghi 16 byte. Si trovano spesso all'interno del registro di Windows e forniscono informazioni all'applicazione host su come aprire un oggetto ole incorporato contenente varie risorse incorporate all'interno dell'applicazione client.
## **Ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato**
 Lo screenshot seguente mostra l'Ole Object Class Identifier, ovvero il GUID che è stato letto dal file[file excel di esempio](5473378.xls) contenente l'oggetto ole di PowerPoint incorporato.

![cose da fare:immagine_alt_testo](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Codice di esempio**
 Si prega di vedere il seguente codice di esempio eseguito con[file excel di esempio](5473378.xls) e il suo output della console che stampa il file*Identificatore di classe*di Ole Object cioè GUID. Il GUID stampato è esattamente lo stesso mostrato all'interno dello screenshot.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Uscita console**
 Questo è l'output della console del codice di esempio precedente quando eseguito con il file[file excel di esempio](5473378.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
