---
title: Licence
type: docs
weight: 50
url: /fr/go-cpp/licensing/
---

## **Limitations de la version d'évaluation**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Chargement d'une Licence depuis un Fichier**

{{% alert color="primary" %}}

Lorsque vous appelez la méthode SetLicense, le nom de la licence que vous passez doit correspondre à celui du fichier de licence. Par exemple, si vous changez le nom du fichier de licence en "Aspose.Cells.lic.xml", transmettez ce nom de fichier à la méthode License->SetLicense_String(…) .

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
