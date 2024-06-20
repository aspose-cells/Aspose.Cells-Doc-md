---
title: ライセンス
type: docs
weight: 21
url: /ja/python-net/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells Pythonの評価版を、ライセンスされたバージョンとまったく同じ機能を提供します。さらに、評価バージョンはライセンスを購入し、コードにいくつかの行を追加してライセンスを適用するとライセンスが適用されます。

{{% /alert %}}

## **評価版の制限**

ライセンスが指定されていないAspose.Cells Python via .Netの評価版は、1つのプログラムで100個のファイルを開くことができ、評価ウォーターマークが付いた追加のワークシートがあります。

制限は以下の通りです:

- **開いたファイルの数**（Aspose.Cells Python via .Net）
  プログラムを実行する際、Aspose.Cells Python via .Netライブラリを使用してExcelファイルを100個までしか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。


さらに、Aspose.Cells Python viaライブラリを使用して生成されたExcelファイルのアクティブなワークシートには常に評価ウォーターマークが表示されます。ライセンスされたバージョンのみ、アクティブなワークシートを他のワークシートに設定できます。Aspose.Cells Python viaの出力PDFやイメージファイルには、評価ウォーターマークがドキュメントまたはイメージの先頭に貼り付けられます。

{{% alert color="primary" %}}

評価版の制限なしでAspose.Cells Python viaをテストしたい場合は、[30日間の一時ライセンス](https://purchase.aspose.com/temporary-license)をリクエストすることもできます。

{{% /alert %}}

## **Aspose.Cells Python viaコンポーネントでライセンスを適用する**

ライセンスは、製品名、ライセンスされた開発者数、サブスクリプション有効期限などの詳細を含むプレーンテキストのXMLファイルです。ファイルはデジタルに署名されているため、ファイルを変更しないでください。ファイルに行を誤って追加すると、ファイルが無効になります。評価制限を回避するためにAspose.Cells Python viaを利用する場合、ライセンスを設定する必要があります。アプリケーション（またはプロセス）ごとにライセンスを1回設定する必要があります。ライセンスはファイルから読み込むことができます。

Aspose.Cells Python viaは、ライセンスを明示的なパスの場所で見つけようとします。

ファイルからライセンスを適用する方法には、2つの一般的な方法があります。

### **ディスクからライセンスを適用**

ライセンスを設定する最も簡単な方法は、ライセンスファイルを明示的なパスに置くことです。

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

set_licenseメソッドを呼び出すときは、ライセンス名をライセンスファイル名と同じにする必要があります。 たとえば、ライセンスファイル名を**Aspose.Cells.lic.xml**に変更してもかまいません。その場合、コード内でset_licenseメソッドに変更したライセンス名(**Aspose.Cells.lic.xml**)を使用する必要があります。

{{% /alert %}}


