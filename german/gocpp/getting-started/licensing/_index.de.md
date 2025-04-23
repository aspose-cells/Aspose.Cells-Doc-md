---
title: Lizenzierung
type: docs
weight: 50
url: /de/go-cpp/licensing/
---

## **Evaluierungsversion-Beschränkungen**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Laden einer Lizenz aus Datei**

{{% alert color="primary" %}}

Wenn Sie die Methode SetLicense aufrufen, sollte der Lizenzname derjenige der Lizenzdatei sein. Wenn Sie beispielsweise den Dateinamen der Lizenzdatei auf "Aspose.Cells.lic.xml" ändern, übergeben Sie diesen Dateinamen an die Methode License->SetLicense_String(…)

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
