---
title: ライセンス
type: docs
weight: 21
url: /ja/python-net/licensing/
---
{{% alert color="primary" %}}

 .Net 経由で Aspose.Cells Python の評価版を簡単にダウンロードできます。[ダウンロードページ](https://pypi.org/project/aspose-cells-python/) Pypi リポジトリ。評価版は、コンポーネントのライセンス版とまったく同じ機能を提供します。さらに、評価版は、ライセンスを購入し、数行のコードを追加してライセンスを適用するだけで、ライセンスが付与されます。

{{% /alert %}}

## **評価版の制限事項**

.Net 製品経由の Aspose.Cells Python の評価版 (ライセンスが指定されていない) は、完全な製品機能を提供しますが、1 つのプログラムで 100 個のファイルを開くことができ、評価用の透かしが付いた追加のワークシートに制限されています。

制限事項を以下に示します。

- **開いているファイルの数** (Aspose.Cells Python .Net経由)
プログラムを実行すると、.Net ライブラリ経由で Aspose.Cells Python を使用して 100 個の Excel ファイルしか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。


さらに、評価の透かしを含むワークシートは、ライブラリ経由で Aspose.Cells Python を使用して、生成された Excel ファイルで常にアクティブなワークシートとして表示されます。ライセンス版のみ、アクティブなワークシートを他のワークシートに設定できます。出力 PDF または Aspose.Cells Python による画像ファイルでは、ドキュメント/画像の上部に評価透かしが貼り付けられます。

{{% alert color="primary" %}}

評価版の制限なしで Aspose.Cells Python をテストしたい場合は、[30日間の一時ライセンス](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **コンポーネント経由で Aspose.Cells Python にライセンスを適用する**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細を含むプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。不用意にファイルに改行を追加しても無効になります。評価制限を回避したい場合は、Aspose.Cells Python 経由で使用する前にライセンスを設定する必要があります。アプリケーション (またはプロセス) ごとに 1 回だけライセンスを設定する必要があります。ライセンスはファイルからロードできます。

Aspose.Cells Python via は、明示的なパスの場所でライセンスを見つけようとします。

ファイルからライセンスを適用するには、2 つの一般的な方法があります。

### **ディスクからのライセンスの適用**

ライセンスを設定する最も簡単な方法は、ライセンス ファイルを明示的なパスに配置することです。

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

セットを呼び出すと_ライセンス方式の場合、ライセンス名はライセンス ファイル名と同じにする必要があります。たとえば、ライセンス ファイル名を **Aspose.Cells.lic.xml** に変更できます。次に、コードで、セットの変更されたライセンス名 (**Aspose.Cells.lic.xml**) を使用する必要があります。_ライセンス方式。

{{% /alert %}}


