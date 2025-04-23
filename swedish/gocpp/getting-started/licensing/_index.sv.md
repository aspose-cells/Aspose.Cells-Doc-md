---
title: Licensiering
type: docs
weight: 50
url: /sv/go-cpp/licensing/
---

## **Begränsningar för utvärderingsversionen**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Ladda en licens från fil**

{{% alert color="primary" %}}

När du anropar SetLicense-metoden bör licensnamnet du anger vara samma som i licensfilen. Till exempel, om du byter namn på licensfilen till "Aspose.Cells.lic.xml", ange det filnamnet i License->SetLicense_String(…) metoden.

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
