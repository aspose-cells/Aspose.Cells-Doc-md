---
title: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato
type: docs
weight: 200
url: /it/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) che puoi usare per ottenere o impostare l'identificatore di classe dell'oggetto OLE incorporato. Gli identificatori di classe degli oggetti Ole sono in realtà GUID, cioè Globally Unique Identifiers. GUID è sempre lungo 16 byte, quindi gli identificatori di classe sono anche lunghi 16 byte. Si trovano spesso all'interno del Registro di Windows e forniscono informazioni all'applicazione host su come aprire l'oggetto OLE incorporato contenente varie risorse incorporate all'interno dell'applicazione client.
## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**
La seguente schermata mostra l'identificatore di classe dell'oggetto OLE, cioè GUID, che è stato letto dal [file di Excel di esempio](5115190.xls) contenente l'oggetto OLE di PowerPoint incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Codice di Esempio**
Si prega di consultare il seguente codice di esempio eseguito con il [file di Excel di esempio](5115190.xls) e la relativa output della console che stampa l'Identificatore di Classe dell'Oggetto OLE, cioè GUID. Il GUID stampato è esattamente lo stesso mostrato nella schermata.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Output della console**
Questo è l'output della console del codice di esempio precedente quando eseguito con il [file di Excel di esempio](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
