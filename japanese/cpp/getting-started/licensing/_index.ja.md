---
title: ライセンス
type: docs
weight: 50
url: /ja/cpp/licensing/
---
## **評価版の制限事項**
Aspose.Cells for C++ の無料評価版は、Aspose の Web サイトのダウンロード セクションからダウンロードできます。<https://downloads.aspose.com/cells/cpp>.
## **ファイルまたはストリーム オブジェクトを使用してライセンスを適用する**
ライセンスは、ファイルまたはストリーム オブジェクトからロードできます。 Aspose.Cells for C++ は、次の場所でライセンスを見つけようとします。

1. 明示的なパス。
1. Aspose.Cells.dll を含むフォルダー。
1. Aspose.Cells.dll を呼び出したアセンブリを含むフォルダー。
1. エントリ アセンブリ (.exe) を含むフォルダー。
1. Aspose.Cells.dll を呼び出したアセンブリ内の埋め込みリソース。

ライセンスを設定する最も簡単な方法は、次の例に示すように、ライセンス ファイルを Aspose.Cells.dll ファイルと同じフォルダーに置き、パスなしでファイル名を指定することです。
### **ファイルからのライセンスのロード**
ライセンスを適用する最も簡単な方法は、ライセンス ファイルを Aspose.Cells.dll ファイルと同じフォルダーに置き、パスを指定せずにファイル名だけを指定することです。

{{% alert color="primary" %}} 

SetLicense メソッドを呼び出すときに渡すライセンス名は、ライセンス ファイルの名前にする必要があります。たとえば、ライセンス ファイル名を「Aspose.Cells.lic.xml」に変更する場合、そのファイル名を Cells->SetLicense(…) メソッドに渡します。

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **ストリーム オブジェクトからのライセンスのロード**
次の例は、ストリームからライセンスをロードする方法を示しています。

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
