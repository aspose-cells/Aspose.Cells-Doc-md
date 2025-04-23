---
title: ライセンス
type: docs
weight: 50
url: /ja/go-cpp/licensing/
---

## **評価版の制限**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **ファイルからライセンスを読み込む**

{{% alert color="primary" %}}

SetLicenseメソッドを呼び出すときに渡すライセンス名は、そのライセンスファイルの名前である必要があります。例えば、ライセンスファイル名を"Aspose.Cells.lic.xml"に変更した場合、そのファイル名をLicense->SetLicense_String(…)メソッドに渡してください。

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
