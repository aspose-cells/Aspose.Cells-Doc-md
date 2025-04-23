---
title: Licencias
type: docs
weight: 50
url: /es/go-cpp/licensing/
---

## **Limitaciones de la versión de evaluación**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Cargando una Licencia desde un Archivo**

{{% alert color="primary" %}}

Cuando llame al método SetLicense, el nombre de la licencia que pase debe ser el del archivo de licencia. Por ejemplo, si cambia el nombre del archivo de licencia a "Aspose.Cells.lic.xml", pase ese nombre de archivo al método License->SetLicense_String(…)

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
