---
title: Licenza
type: docs
weight: 50
url: /it/cpp/licensing/
---

## **Limitazioni della Versione di Valutazione**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Applicare la licenza utilizzando un file o un oggetto stream**
La licenza può essere caricata da un file o un oggetto stream. Aspose.Cells for C++ cercherà di trovare la licenza nei seguenti percorsi:

1. Percorso esplicito.
1. La cartella che contiene Aspose.Cells.dll.
1. La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll.
1. La cartella che contiene l'assembly di avvio (il tuo .exe).
1. Una risorsa incorporata nell'assembly che ha chiamato Aspose.Cells.dll.

Il modo più semplice per impostare una licenza è mettere il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare il nome del file, senza un percorso, come mostrato nell'esempio seguente.
### **Caricamento di una licenza da file**
Il modo più semplice per applicare una licenza è mettere il file di licenza nella stessa cartella del file Aspose.Cells.dll e specificare solo il nome del file senza un percorso.

{{% alert color="primary" %}} 

Quando chiami il metodo SetLicense, il nome della licenza che passi dovrebbe essere quello del file di licenza. Ad esempio, se cambi il nome del file di licenza in "Aspose.Cells.lic.xml" passa quel nome file al metodo Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Caricamento di una licenza da un oggetto stream**
Nell'esempio seguente viene mostrato come caricare una licenza da un oggetto stream.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
