---
title: セルのテキストの回転方法
type: docs
weight: 80
url: /ja/python-net/how-to-rotate-text-of-cell/
description: C#コードでセルのテキストを回転させてAspose.Cells for Python via .NET APIを使用
keywords: Pythonでセルのテキストを回転させる方法、Pythonでセルのテキストをプログラム的に回転させる、ワークブック内のセル回転角度を設定、PythonでExcelのセルのテキストを回転させる方法
---

## **Aspose.Cells for Python via .NETでセルのテキストを回転させる方法**

Aspose.Cells for Python via .NETは、Excelスプレッドシートをプログラムで操作できる強力な.NETおよびJavaのコンポーネントです。提供されている機能の一つに、セルの回転があります。これにより、テキストの向きをカスタマイズし、データの見栄えを改善できます。この資料では、Aspose.Cells for Python via .NETを使ったセルの回転方法を解説します。

## **Excel でセルのテキストを回転する方法**
Excel でセルを回転するには、次の手順を使用できます:
1. Excel を開き、回転させたいセルまたは範囲を選択します。
1. 選択したセルで右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excel リボンの「ホーム」タブで、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。
1. 「セルの書式設定」ダイアログボックスで、「配置」タブに移動します。
1. 「方向」セクションで、テキストの回転オプションが表示されます。『度』ボックスに、希望の回転角度を直接入力できます。正の値はテキストを反時計回りに、負の値は時計回りに回転させます。
<br>
![todo:image_alt_text](alignment.png)
1. 希望の回転を選択したら、「OK」をクリックして変更を適用します。選択したセルは、選択した回転角度または方向に基づいて回転されます。

## **Aspose.Cells for Python via .NETでセルのテキストを回転させるにはどうすればいいですか**

[**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) プロパティはセルの回転を便利にします。Aspose.Cells for Python via .NETでセルを回転させる手順は以下の通りです：
1. Excelワークブックをロードする
<br>
最初に、Aspose.Cells for Python via .NETを使ってExcelワークブックを読み込みます。Workbookクラスを利用して既存のExcelファイルを開くか、新しいファイルを作成します。 

1. ワークシートにアクセスする
<br>
ワークブックがロードされたら、セルを回転させたいワークシートにアクセスする必要があります。ワークシートはインデックスまたは名前でアクセスできます。 

1. セルのテキストを回転させる
<br>
ワークシートにアクセスできるようになったので、希望のセルのStyleオブジェクトを変更することでセルを回転させることができます。Styleオブジェクトを使用すると、回転を含むさまざまな書式設定オプションを設定できます。 

1. ワークブックを保存する
<br>
セルを回転させた後、変更されたワークブックをSaveメソッドを使用してファイルまたはストリームに保存できます。

## **Python サンプルコード**

以下のコードをご覧ください。これはワークブックオブジェクトを作成し、いくつかのセルに異なる回転角を設定しています。スクリーンショットはサンプルコードの実行後の結果を示しています。
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

{{< app/cells/assistant language="python-net" >}}
