﻿---
title: ライセンス
type: docs
weight: 50
url: /ja/python-java/licensing/
---
{{% alert color="primary" %}} 

の評価版をインストールできます。**Aspose.Cells**評価版は、製品のライセンス版とまったく同じ機能を提供します。さらに、評価版は、ライセンスを購入し、数行のコードを追加してライセンスを適用するだけで、ライセンスが付与されます。

評価に満足したら**Aspose.Cells**、 あなたはできる[ライセンスを購入する](https://purchase.aspose.com)Aspose ウェブサイトで。提供されるさまざまなサブスクリプションの種類に慣れてください。ご不明な点がございましたら、お気軽に Aspose 営業チームまでお問い合わせください。

すべての Aspose ライセンスには、この期間中に出てくる新しいバージョンまたは修正への無料アップグレードのための 1 年間のサブスクリプションが含まれています。テクニカル サポートは無料で無制限で、ライセンス ユーザーと評価ユーザーの両方に提供されます。

{{% /alert %}} {{% alert color="primary" %}} 

テストしたい場合**Aspose.Cells**評価版の制限がない場合は、30 日間の一時ライセンスをリクエストしてください。を参照してください。[仮免許を取得するには？](https://purchase.aspose.com/temporary-license)詳細については。

{{% /alert %}}

## **評価版の制限事項**

の評価版**Aspose.Cells**製品 (ライセンスが指定されていない) は製品の全機能を提供しますが、1 つのプログラムで 100 個のファイルを開くことができ、評価用のウォーターマーク付きの追加のワークシートに制限されています。

制限事項を以下に示します。

### **第 1 の制限: 開いているファイルの数**

プログラムを実行すると、100 個の Excel ファイルしか開くことができません。アプリケーションがこの数を超えると、例外がスローされます。

### **2 番目の制限: 評価用透かし付きワークシート**

![todo:画像_代替_文章](licensing_1.png)

このワークシートは常にアクティブなワークシートとして表示されます。ライセンス版のみ、アクティブなワークシートを他のワークシートに設定できます。

## **ライセンスの設定**

ライセンスは、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細を含むプレーン テキストの XML ファイルです。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を誤って追加しても、それは無効になります。

評価制限を回避したい場合は、Aspose.Cells を利用する前にライセンスを設定する必要があります。アプリケーションまたはプロセスごとに 1 回だけライセンスを設定する必要があります。

ライセンスは、次の場所にあるファイルからロードできます。

1. 明示的なパス。
1. 作業フォルダ。

使用[License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License)コンポーネントのライセンスを取得する方法。多くの場合、ライセンスを設定する最も簡単な方法は、次の例に示すように、ライセンス ファイルを Aspose.Cells.jar と同じフォルダーに置き、パスを指定せずにファイル名のみを指定することです。

### **例**

この例では**Aspose.Cells**は、作業フォルダでライセンス ファイルを見つけようとします。

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}