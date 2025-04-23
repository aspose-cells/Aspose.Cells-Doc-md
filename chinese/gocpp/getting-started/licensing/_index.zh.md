---
title: 许可证
type: docs
weight: 50
url: /zh/go-cpp/licensing/
---

## **评估版本限制**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **从文件加载许可**

{{% alert color="primary" %}}

调用 SetLicense 方法时，传递的许可证名称应与许可证文件名相符。例如，如果将许可证文件名更改为 "Aspose.Cells.lic.xml"，则传递该文件名到 License->SetLicense_String(…) 方法。

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
