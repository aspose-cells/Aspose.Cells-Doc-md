---
title: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato
type: docs
weight: 920
url: /it/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) che è possibile utilizzare per ottenere o impostare l'identificatore di classe di un oggetto ole incorporato. Gli identificatori di classe degli oggetti Ole sono in realtà GUID, ovvero Globally Unique Identifiers. GUID è sempre lungo 16 byte, quindi gli identificatori di classe sono anche lunghi 16 byte. Sono spesso trovati all'interno del Registro di Windows e forniscono informazioni all'applicazione host su come aprire l'oggetto ole incorporato contenente varie risorse incorporate all'interno dell'applicazione client.
## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**
La seguente schermata mostra l'identificatore di classe dell'oggetto Ole cioè GUID che è stato letto dal [file Excel di esempio](5473378.xls) contenente l'oggetto ole di PowerPoint incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Codice di Esempio**
Si prega di vedere il seguente codice di esempio eseguito con il [file Excel di esempio](5473378.xls) e il suo output della console che stampa il *Class Identifier* dell'oggetto Ole cioè GUID. Il GUID stampato è esattamente lo stesso mostrato all'interno della schermata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Output della console**
Questo è l'output della console del codice di esempio sopra eseguito con il [file Excel di esempio](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
