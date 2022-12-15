---
title: Ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato
type: docs
weight: 200
url: /it/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells fornisce il[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)proprietà che è possibile utilizzare per ottenere o impostare l'identificatore di classe dell'oggetto ole incorporato. Gli identificatori di classi di oggetti obsoleti sono in realtà GUID, ovvero identificatori univoci globali. Il GUID è sempre lungo 16 byte, pertanto anche gli identificatori di classe sono lunghi 16 byte. Si trovano spesso all'interno del registro di Windows e forniscono informazioni all'applicazione host su come aprire un oggetto ole incorporato contenente varie risorse incorporate all'interno dell'applicazione client.
## **Ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato**
 Lo screenshot seguente mostra l'Ole Object Class Identifier, ovvero il GUID che è stato letto dal file[file excel di esempio](5115190.xls) contenente l'oggetto ole di PowerPoint incorporato.

![cose da fare:immagine_alt_testo](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Codice di esempio**
 Si prega di vedere il seguente codice di esempio eseguito con[file excel di esempio](5115190.xls) e il suo output della console che stampa l'identificatore di classe dell'oggetto Ole, ovvero il GUID. Il GUID stampato è esattamente lo stesso mostrato all'interno dello screenshot.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Uscita console**
 Questo è l'output della console del codice di esempio precedente quando eseguito con il file[file excel di esempio](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
