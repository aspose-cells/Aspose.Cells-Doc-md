---
title: ライセンス
type: docs
weight: 50
url: /ja/cpp/licensing/
---

## **評価版の制限**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **ファイルまたはストリームオブジェクトを使用してライセンスを適用する**
ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。 Aspose.Cells for C++は次の場所でライセンスを検索しようとします：

1. 明示的なパス。
1. Aspose.Cells.dllを含むフォルダー。
1. Aspose.Cells.dllを呼び出したアセンブリを含むフォルダー。
1. エントリアセンブリ（.exe）を含むフォルダー。
1. Aspose.Cells.dllを呼び出したアセンブリ内の埋め込みリソース。

ライセンスを設定する最も簡単な方法は、Aspose.Cells.dllファイルと同じフォルダにライセンスファイルを配置し、以下の例に示すように、パスなしでファイル名を指定することです。
### **ファイルからライセンスを読み込む**
ライセンスを適用する最も簡単な方法は、Aspose.Cells.dllファイルと同じフォルダにライセンスファイルを配置し、パスなしでファイル名のみを指定することです。

{{% alert color="primary" %}} 

SetLicenseメソッドを呼び出す際に、渡すライセンス名はライセンスファイルのものである必要があります。たとえば、ライセンスファイル名を"Aspose.Cells.lic.xml"に変更した場合、そのファイル名をCells->SetLicense(…)メソッドに渡してください。

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **ストリームオブジェクトからライセンスを読み込む**
以下の例は、ストリームからライセンスを読み込む方法を示しています。

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
