---
title: Licenza
type: docs
weight: 50
url: /it/go-cpp/licensing/
---

## **Limitazioni della Versione di Valutazione**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Caricamento di una licenza da file**

{{% alert color="primary" %}}

Quando chiami il metodo SetLicense, il nome della licenza che passi dovrebbe corrispondere a quello del file di licenza. Ad esempio, se cambi il nome del file di licenza in "Aspose.Cells.lic.xml", passa quel nome di file al metodo License->SetLicense_String(…).

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
