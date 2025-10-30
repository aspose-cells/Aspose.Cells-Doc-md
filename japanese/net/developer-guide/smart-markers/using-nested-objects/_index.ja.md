---
title: ネスマークを用いたExcelへのスマートなネストオブジェクトのインポート
type: docs
weight: 30
url: /ja/net/how-to-import-nested-objects-with-smart-markers/
---

## **スマートマーカーにおけるネストされたオブジェクトの使用理由**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. 階層的データ表現：実世界のデータは本質的にネストされている（例：注文は顧客を含み、その顧客は住所を持つ）。ネストされたオブジェクトはこの構造を反映し、顧客_cityのような平坦または人工的なフィールドを避ける。
2. 名前の衝突回避：平坦な構造は衝突のリスクがある（例：product_name対はさみname）。ネストは自然に名前空間を分離し次のようにスコープを限定：
<<product.name>> vs. <<supplier.name>>.
3. モジュール性と再利用性：サブオブジェクトの再利用、住所オブジェクトは顧客、販売者、従業員のマーカーに埋め込むことができ、住所の変更は全体に伝播する。
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. フレームワーク/ツールのサポート：最新のエンジン（例：Handlebars、React、FoxPro）はネストされたパスをネイティブに解決。JSON/APIの標準的なネストされたデータと整合している。

## **スマートマーカーを用いた匿名型またはカスタムオブジェクトのインポート方法**
Aspose.Cellsでは、スマートマーカー内で匿名型またはカスタムオブジェクトもサポートしています。以下の例では、これがどのように機能するかを示しています。スマートマーカーを使用して動的オブジェクトからデータをインポートする場合は、次の記事を参照してください：

[動的オブジェクトをデータソースとしてインポートする](/cells/ja/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **ネストされたオブジェクトをスマートマーカーでインポートする方法**
Aspose.Cellsはスマートマーカーでネストされたオブジェクトをサポートし、ネストされたオブジェクトはシンプルである必要があります。単純なテンプレートファイルを使用します。一部のネストされたスマートマーカーを含むデザイナースプレッドシートを参照してください。

|**SM_NestedObjects.xlsxファイルの最初のワークシートには、ネストされたスマートマーカーが表示されています。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下の例は、これがどのように動作するかを示しています。


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **ジェネリックリストをネストされたオブジェクトとしてスマートマーカーでインポートする方法**
Aspose.Cellsは今やネストオブジェクトとして一般的なリストの使用もサポートしています。以下のコードで生成された出力エクセルファイルのスクリーンショットをご確認ください。スクリーンショットでは、Teacherオブジェクトが複数のネストされたStudentオブジェクトを含んでいるのが確認できます。

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **ネストされたオブジェクトを行ごとではなくSmart Markersでインポートする方法**
現在のデフォルトの処理方法は、スマートマーカーを行ごとに処理することです。しかし、データテーブルの同じスマートマーカーを、行が同じであるかどうかに関係なく一緒に処理する必要がある場合は、処理を呼び出す前に名前付き範囲"_CellsSmartMarkers"を指定し、WorkbookDesigner.LineByLineをfalseに指定する必要があります。 
スマートマーカーと一緒にデータをマージする際の通知の取得

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
