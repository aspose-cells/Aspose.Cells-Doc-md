---
title: OLE オブジェクトの管理
type: docs
weight: 30
url: /ja/java/managing-ole-objects/
---
## **序章**

OLE (Object Linking and Embedding) は、Microsoft の複合文書技術のフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、サウンド、モーション ビデオ、3D、継続的に更新されるニュース、コントロールなど、あらゆる種類のビジュアル オブジェクトと情報オブジェクトを含むことができるディスプレイ デスクトップのようなものです。各デスクトップ オブジェクトは、ユーザーとやり取りしたり、デスクトップ上の他のオブジェクトと通信したりできる独立したプログラム エンティティです。

 OLE (Object Linking and Embedding) はさまざまなプログラムでサポートされており、あるプログラムで作成されたコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入できます。挿入できるコンテンツの種類を確認するには、**物体**上で**入れる**メニュー。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムのみが**オブジェクトタイプ**箱。

## **ワークシートへの OLE オブジェクトの挿入**

Aspose.Cells は、ワークシートでの OLE オブジェクトの追加、抽出、および操作をサポートしています。このため、Aspose.Cells には[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)コレクション リストに新しい OLE オブジェクトを追加するために使用されるクラス。別のクラス、[**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)、OLE オブジェクトを表します。いくつかの重要なメンバーがあります。

- [**画像データ**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)バイト配列型の画像（アイコン）データを指定します。画像が表示され、ワークシートに OLE オブジェクトが表示されます。
- [**オブジェクトデータ**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)オブジェクトデータをバイト配列の形式で指定します。このデータは、OLE オブジェクト アイコンをダブルクリックすると、関連するプログラムに表示されます。

次の例は、OLE オブジェクトをワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **ワークブックでの OLE オブジェクトの抽出**

次の例は、ブック内の OLE オブジェクトを抽出する方法を示しています。この例では、既存の XLS ファイルからさまざまな OLE オブジェクトを取得し、OLE オブジェクトのファイル形式の種類に基づいてさまざまなファイル (DOC、XLS、PPT、PDF など) を保存します。

テンプレート XLS ファイルのスクリーンショットを次に示します。最初のワークシートにさまざまな OLE オブジェクトが埋め込まれています。

**テンプレート ファイルには 4 つの OLE オブジェクトが含まれています** 

![todo:画像_代替_文章](managing-ole-objects_1.png)

コードを実行した後、それぞれの OLE オブジェクト形式の種類に基づいてさまざまなファイルを保存できます。以下は、作成されたファイルの一部のスクリーンショットです。

**抽出されたXLSファイル** 

![todo:画像_代替_文章](managing-ole-objects_2.png)

**抽出されたPPTファイル** 

![todo:画像_代替_文章](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **埋め込まれた MOL ファイルの抽出**

Aspose.Cells は、MOL (原子と結合に関する情報を含む分子データ ファイル) のような珍しいタイプのオブジェクトの抽出をサポートします。次のコード スニペットは、埋め込まれた MOL ファイルを抽出し、これを使用してディスクに保存する方法を示しています。[サンプルエクセルファイル](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **先行トピック**
- [リンクされた Ole オブジェクトの表示ラベルにアクセスして変更する](/cells/ja/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cells を使用して Microsoft Excel 経由で OLE オブジェクトを自動的に更新する](/cells/ja/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ブックから OLE オブジェクトを抽出する](/cells/ja/java/extract-ole-objects-from-workbook/)
- [埋め込み OLE オブジェクトのクラス識別子を取得または設定します](/cells/ja/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
