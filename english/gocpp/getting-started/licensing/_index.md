---  
title: Licensing  
type: docs  
weight: 50  
url: /go-cpp/licensing/  
---  

## **Evaluation Version Limitations**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's website at: <https://releases.aspose.com/cells/go-cpp/>.  

## **Loading a License from File**

{{% alert color="primary" %}}

When you call the SetLicense method, the license name that you pass should be that of the license file. For example, if you change the license file name to "Aspose.Cells.lic.xml", pass that file name to the License->SetLicense_String(…) method.

{{% /alert %}}

**Go**

{{< highlight go >}}  
lic, _ := NewLicense()  
lic.SetLicense_String(os.Getenv("LicensePath"))  
{{< /highlight >}}