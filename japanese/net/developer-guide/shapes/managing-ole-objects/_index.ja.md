---
title: OLE オブジェクトの管理
type: docs
weight: 50
url: /ja/net/managing-ole-objects/
---
## **序章**

OLE (Object Linking and Embedding) は、Microsoft の複合文書技術のフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、サウンド、モーション ビデオ、3D、継続的に更新されるニュース、コントロールなど、あらゆる種類のビジュアル オブジェクトと情報オブジェクトを含むことができるディスプレイ デスクトップのようなものです。各デスクトップ オブジェクトは、ユーザーとやり取りしたり、デスクトップ上の他のオブジェクトと通信したりできる独立したプログラム エンティティです。

 OLE (Object Linking and Embedding) はさまざまなプログラムでサポートされており、あるプログラムで作成されたコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入できます。挿入できるコンテンツの種類を確認するには、**物体**上で**入れる**メニュー。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムのみが**オブジェクトタイプ**箱。

### **ワークシートへの OLE オブジェクトの挿入**

Aspose.Cells は、ワークシートでの OLE オブジェクトの追加、抽出、および操作をサポートしています。このため、Aspose.Cells には[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)コレクション リストに新しい OLE オブジェクトを追加するために使用されるクラス。別のクラス、[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)、OLE オブジェクトを表します。いくつかの重要なメンバーがあります。

- の[**画像データ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)プロパティは、バイト配列型のイメージ (アイコン) データを指定します。画像が表示され、ワークシートに OLE オブジェクトが表示されます。
- の[**オブジェクトデータ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)プロパティは、バイト配列の形式でオブジェクト データを指定します。このデータは、OLE オブジェクト アイコンをダブルクリックすると、関連するプログラムに表示されます。

次の例は、OLE オブジェクトをワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **ワークブックでの OLE オブジェクトの抽出**

次の例は、ブック内の OLE オブジェクトを抽出する方法を示しています。この例では、既存の XLS ファイルからさまざまな OLE オブジェクトを取得し、OLE オブジェクトのファイル形式の種類に基づいてさまざまなファイル (DOC、XLS、PPT、PDF など) を保存します。

コードを実行した後、それぞれの OLE オブジェクト形式の種類に基づいてさまざまなファイルを保存できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **埋め込まれた MOL ファイルの抽出**

Aspose.Cells は、MOL (原子と結合に関する情報を含む分子データ ファイル) のような珍しいタイプのオブジェクトの抽出をサポートします。次のコード スニペットは、埋め込まれた MOL ファイルを抽出し、これを使用してディスクに保存する方法を示しています。[サンプルエクセルファイル](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **先行トピック**
- [リンクされた Ole オブジェクトの表示ラベルにアクセスして変更する](/cells/ja/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cells を使用して Microsoft Excel 経由で OLE オブジェクトを自動的に更新する](/cells/ja/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ブックから OLE オブジェクトを抽出する](/cells/ja/net/extract-ole-objects-from-workbook/)
- [埋め込み OLE オブジェクトのクラス識別子を取得または設定します](/cells/ja/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [WAV ファイルを Ole オブジェクトとして挿入する](/cells/ja/net/inserting-a-wav-file-as-an-ole-object/)

