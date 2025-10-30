---
title: Ottieni o imposta l identificatore della classe dell oggetto OLE incorporato con Golang tramite C++
linktitle: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato
type: docs
weight: 200
url: /it/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Impara come ottenere o impostare l identificatore della classe degli oggetti OLE incorporati usando Aspose.Cells con Golang tramite C++.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells fornisce la proprietà [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) che puoi usare per ottenere o impostare l'identificatore della classe dell'oggetto OLE incorporato. Gli identificatori di classe dell'oggetto OLE sono in realtà GUID, ovvero Identificatori Unici Globali. Il GUID è sempre lungo 16 byte, quindi gli identificatori di classe sono anche di 16 byte. Sono spesso trovati all'interno del Registro di Windows e forniscono informazioni all'applicazione host su come aprire oggetti OLE incorporati contenenti varie risorse incorporate all'interno dell'applicazione client.

## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**
Il seguente screenshot mostra l'identificatore di classe dell'oggetto OLE, cioè GUID, che è stato letto dal [file Excel di esempio](5115190.xls) contenente l'oggetto PowerPoint OLE incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Codice di Esempio**
Vedi il seguente esempio di codice eseguito con il [file Excel di esempio](5115190.xls) e l’output della console che stampa l'ID di classe dell'OLE, ovvero GUID. Il GUID stampato è esattamente lo stesso mostrato nello screenshot.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Output della console**
Questo è l'output della console del codice di esempio precedente quando eseguito con il [file di Excel di esempio](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
