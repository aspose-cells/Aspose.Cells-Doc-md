---
title: OLE オブジェクトを管理する
type: docs
weight: 50
url: /ja/net/managing-ole-objects/
---

## **紹介**

OLE (Object Linking and Embedding) は、Microsoft の複合ドキュメントテクノロジーのフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、音声、動画、3D、定期的に更新されるニュース、コントロールなど、あらゆる種類の視覚的および情報オブジェクトを含む表示デスクトップのことです。各デスクトップオブジェクトは、ユーザーと相互作用し、他のデスクトップ上の他のオブジェクトとも通信できる独立したプログラムエンティティです。

OLE (Object Linking and Embedding) は、さまざまなプログラムでサポートされており、あるプログラムで作成したコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入することができます。挿入可能なコンテンツの種類を確認するには、**挿入** メニューで **オブジェクト** をクリックします。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムだけが **オブジェクトの種類** ボックスに表示されます。

### **ワークシートにOLEオブジェクトを挿入する**

Aspose.Cellsはワークシート内のOLEオブジェクトの追加、抽出、および操作をサポートしています。そのため、Aspose.Cellsには新しいOLEオブジェクトをコレクションリストに追加するために使用される[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)クラスがあります。また、[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)という別のクラスはOLEオブジェクトを表します。いくつかの重要なメンバーがあります。

- [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)プロパティはバイト配列型の画像（アイコン）データを指定します。画像はOLEオブジェクトを示すために表示されます。
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)プロパティはバイト配列形式のオブジェクトデータを指定します。このデータは、OLEオブジェクトアイコンをダブルクリックすると関連するプログラムに表示されます。

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **ワークブックからOLEオブジェクトを抽出**

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。

コードを実行した後、対応するOLEオブジェクト形式の異なるファイルを保存できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **埋め込まれたMOLファイルの抽出**

Aspose.Cellsは、MOL（原子および結合に関する情報を含む分子データファイル）のような一般的でないタイプのオブジェクトを抽出する機能をサポートしています。次のコードスニペットは、埋め込まれたMOLファイルを抽出してディスクに保存する方法を示しています: [サンプルExcelファイル](94896196.xlsx)を使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **高度なトピック**
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する](/cells/ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/net/extract-ole-objects-from-workbook/)
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole ObjectとしてWAVファイルを挿入する](/cells/ja/net/inserting-a-wav-file-as-an-ole-object/)

