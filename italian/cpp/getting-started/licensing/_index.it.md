---
title: Licensing
type: docs
weight: 50
url: /it/cpp/licensing/
---
##  **Limitazioni della versione di valutazione**
 Una versione di valutazione gratuita di Aspose.Cells for C++ può essere scaricata dalla sezione download del sito Web di Aspose all'indirizzo:<https://downloads.aspose.com/cells/cpp>.
##  **Applicare la licenza utilizzando il file o l'oggetto flusso**
La licenza può essere caricata da un file o da un oggetto flusso. Aspose.Cells for C++ cercherà di trovare la licenza nelle seguenti località:

1. Percorso esplicito.
1. La cartella che contiene Aspose.Cells.dll.
1. La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll.
1. La cartella che contiene l'assembly della voce (il tuo file .exe).
1. Una risorsa incorporata nell'assembly che ha chiamato Aspose.Cells.dll.

Il modo più semplice per impostare una licenza è inserire il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare il nome del file, senza percorso, come mostrato nell'esempio seguente.
###  **Caricamento di una licenza da file**
Il modo più semplice per applicare una licenza è inserire il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare solo il nome del file senza percorso.

{{% alert color="primary" %}} 

Quando chiami il metodo SetLicense, il nome della licenza che passi dovrebbe essere quello del file di licenza. Ad esempio, se si modifica il nome del file di licenza in "Aspose.Cells.lic.xml", passare il nome del file al metodo Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **Caricamento di una licenza da un oggetto stream**
L'esempio seguente mostra come caricare una licenza da un flusso.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
