---
title: Licensing
type: docs
weight: 50
url: /ja/cpp/licensing/
---
##  **評価版の制限事項**
Aspose.Cells for C++ の無料評価版は、Aspose の Web サイトのダウンロード セクションからダウンロードできます。<https://downloads.aspose.com/cells/cpp>.
##  **ファイルまたはストリーム オブジェクトを使用してライセンスを適用する**
ライセンスはファイルまたはストリーム オブジェクトからロードできます。 Aspose.Cells for C++ は、次の場所でライセンスを検索しようとします。

1. 明示的なパス。
1. Aspose.Cells.dll が含まれるフォルダー。
1. Aspose.Cells.dll を呼び出したアセンブリが含まれるフォルダー。
1. エントリ アセンブリ (.exe) が含まれるフォルダー。
1. Aspose.Cells.dll というアセンブリ内の埋め込みリソース。

ライセンスを設定する最も簡単な方法は、次の例に示すように、ライセンス ファイルを Aspose.Cells.dll ファイルと同じフォルダーに置き、パスを指定せずにファイル名を指定することです。
###  **ファイルからライセンスをロードする**
ライセンスを適用する最も簡単な方法は、ライセンス ファイルを Aspose.Cells.dll ファイルと同じフォルダーに置き、パスを指定せずにファイル名だけを指定することです。

{{% alert color="primary" %}} 

SetLicense メソッドを呼び出す場合、渡すライセンス名はライセンス ファイルのライセンス名である必要があります。たとえば、ライセンス ファイル名を「Aspose.Cells.lic.xml」に変更する場合は、そのファイル名を Cells->SetLicense(…) メソッドに渡します。

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **ストリームオブジェクトからのライセンスのロード**
次の例は、ストリームからライセンスをロードする方法を示しています。

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
