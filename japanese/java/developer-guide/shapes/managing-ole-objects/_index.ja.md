---
title: OLE オブジェクトを管理する
type: docs
weight: 30
url: /ja/java/managing-ole-objects/
---

## **紹介**

OLE (Object Linking and Embedding) は、Microsoft の複合ドキュメントテクノロジーのフレームワークです。簡単に言うと、複合ドキュメントとは、テキスト、カレンダー、アニメーション、音声、動画、3D、定期的に更新されるニュース、コントロールなど、あらゆる種類の視覚的および情報オブジェクトを含む表示デスクトップのことです。各デスクトップオブジェクトは、ユーザーと相互作用し、他のデスクトップ上の他のオブジェクトとも通信できる独立したプログラムエンティティです。

OLE (Object Linking and Embedding) は、さまざまなプログラムでサポートされており、あるプログラムで作成したコンテンツを別のプログラムで利用できるようにするために使用されます。たとえば、Microsoft Word ドキュメントを Microsoft Excel に挿入することができます。挿入可能なコンテンツの種類を確認するには、**挿入** メニューで **オブジェクト** をクリックします。コンピュータにインストールされ、OLE オブジェクトをサポートするプログラムだけが **オブジェクトの種類** ボックスに表示されます。

## **ワークシートに OLE オブジェクトを挿入**

Aspose.Cells は、ワークシートに OLE オブジェクトを追加、取り出し、操作することをサポートしています。このために、Aspose.Cells には新しい OLE オブジェクトをコレクションリストに追加するための [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection) クラスがあります。別のクラスである [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject) は OLE オブジェクトを表します。いくつか重要なメンバーがあります。

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) はバイト配列型のイメージ（アイコン）データを指定します。イメージは、ワークシートに OLE オブジェクトとして表示されます。
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)はバイト配列形式でオブジェクトデータを指定します。このデータはOLEオブジェクトアイコンをダブルクリックすると関連プログラムで表示されます。

以下の例では、OLEオブジェクトをワークシートに追加する方法を示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **ワークブックからOLEオブジェクトを抽出**

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。

これはテンプレートXLSファイルのスクリーンショットであり、最初のワークシートに異なるOLEオブジェクトが埋め込まれています。

テンプレートファイルには4つのOLEオブジェクトが含まれています 

![todo:image_alt_text](managing-ole-objects_1.png)

コードを実行した後、各々のOLEオブジェクトのフォーマットに基づいて異なるファイルを保存できます。作成されたファイルの一部を以下に示します。

抽出されたXLSファイル 

![todo:image_alt_text](managing-ole-objects_2.png)

抽出されたPPTファイル 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **埋め込まれたMOLファイルの抽出**

Aspose.CellsはMOL（原子や結合に関する情報を含む分子データファイル）のような一般的でない種類のオブジェクトの抽出をサポートしています。以下のコードスニペットは埋め込まれたMOLファイルの抽出とそれをディスクに保存する方法を示しています。[サンプルExcelファイル](EmbeddedMolSample.xlsx)を使用しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **高度なトピック**
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する](/cells/ja/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/java/extract-ole-objects-from-workbook/)
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}
