---
title: Licensing
type: docs
weight: 50
url: /go-cpp/licensing/
---

## **Evaluation Version Limitations**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/go-cpp>.

## **Apply License using File or Stream Object**

The license can be loaded from a file or stream object. Aspose.Cells for Go via C++ will try to find the license in the following locations:

1. Explicit path.
1. The folder that contains Aspose.Cells.dll or libAspose.Cells.so.
1. The folder that contains the assembly that called Aspose.Cells.dll or libAspose.Cells.so.
1. The folder that contains the entry assembly (your .exe).
1. An embedded resource in the assembly that called Aspose.Cells.dll or libAspose.Cells.so.

The easiest way to set a license is to put the license file in the same folder as the Aspose.Cells.dll file and specify the file name, without a path, as shown in the example below.

### **Loading a License from File**

The easiest way to apply a license is to put the license file in the same folder as the Aspose.Cells.dll file and specify just the file name without a path.

{{% alert color="primary" %}}

When you call the SetLicense method, the license name that you pass should be that of the license file. For example, if you change the license file name to "Aspose.Cells.lic.xml" pass that file name to the Cells->SetLicense_String(…) method.

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
