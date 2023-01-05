---
title: Licenza
type: docs
weight: 50
url: /it/cpp/licensing/
---
## **Limiti della versione di valutazione**
 Una versione di valutazione gratuita di Aspose.Cells for C++ può essere scaricata dalla sezione download del sito Web di Aspose all'indirizzo:<https://downloads.aspose.com/cells/cpp>.
## **Applica la licenza utilizzando l'oggetto File o Stream**
La licenza può essere caricata da un oggetto file o stream. Aspose.Cells for C++ cercherà di trovare la licenza nelle seguenti posizioni:

1. Percorso esplicito.
1. La cartella che contiene Aspose.Cells.dll.
1. La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll.
1. La cartella che contiene l'assembly della voce (il tuo .exe).
1. Una risorsa incorporata nell'assembly che ha chiamato Aspose.Cells.dll.

Il modo più semplice per impostare una licenza è inserire il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare il nome del file, senza un percorso, come mostrato nell'esempio seguente.
### **Caricamento di una licenza da file**
Il modo più semplice per applicare una licenza consiste nell'inserire il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare solo il nome del file senza un percorso.

{{% alert color="primary" %}} 

Quando si chiama il metodo SetLicense, il nome della licenza che si passa deve essere quello del file di licenza. Ad esempio, se si modifica il nome del file di licenza in "Aspose.Cells.lic.xml", passare il nome del file al metodo Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Caricamento di una licenza da un oggetto flusso**
L'esempio seguente mostra come caricare una licenza da un flusso.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
