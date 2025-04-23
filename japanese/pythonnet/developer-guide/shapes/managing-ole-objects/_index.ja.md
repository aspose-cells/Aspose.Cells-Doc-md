---
title: OLE オブジェクトを管理する
type: docs
weight: 50
url: /ja/python-net/managing-ole-objects/
---

## **紹介**

OLE (Object Linking and Embedding) は、Microsoft の複合ドキュメントテクノロジーのフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、音声、動画、3D、定期的に更新されるニュース、コントロールなど、あらゆる種類の視覚的および情報オブジェクトを含む表示デスクトップのことです。各デスクトップオブジェクトは、ユーザーと相互作用し、他のデスクトップ上の他のオブジェクトとも通信できる独立したプログラムエンティティです。

OLE (Object Linking and Embedding) は、さまざまなプログラムでサポートされており、あるプログラムで作成したコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入することができます。挿入可能なコンテンツの種類を確認するには、**挿入** メニューで **オブジェクト** をクリックします。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムだけが **オブジェクトの種類** ボックスに表示されます。

### **ワークシートにOLEオブジェクトを挿入する**

Aspose.Cells for Python via .NET は、ワークシート内のOLEオブジェクトの追加、抽出、操作をサポートします。そのため、`[**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection)`クラスを使用して新しいOLEオブジェクトをコレクションリストに追加します。もう一つのクラス、`[**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject)`はOLEオブジェクトを表し、いくつかの重要なメンバーを持ちます：

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data)プロパティはバイト配列型の画像（アイコン）データを指定します。画像はOLEオブジェクトを示すために表示されます。
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data)プロパティはバイト配列形式のオブジェクトデータを指定します。このデータは、OLEオブジェクトアイコンをダブルクリックすると関連するプログラムに表示されます。

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **ワークブックからOLEオブジェクトを抽出**

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。

コードを実行した後、対応するOLEオブジェクト形式の異なるファイルを保存できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **埋め込まれたMOLファイルの抽出**

Aspose.Cells for Python via .NETは、MOL（原子と結合に関する情報を含む分子データファイル）のような珍しいタイプのオブジェクトの抽出もサポートしています。以下のコードスニペットは、組み込まれたMOLファイルを抽出し、この[サンプルExcelファイル](94896196.xlsx)を使用してディスクに保存する例です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **高度なトピック**
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [OLEオブジェクトを自動的に更新](/cells/ja/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/python-net/extract-ole-objects-from-workbook/)
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole ObjectとしてWAVファイルを挿入する](/cells/ja/python-net/inserting-a-wav-file-as-an-ole-object/)

