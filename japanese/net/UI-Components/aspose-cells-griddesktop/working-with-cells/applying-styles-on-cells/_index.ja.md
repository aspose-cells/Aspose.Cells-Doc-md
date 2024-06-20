---
title: セルにスタイルを適用
type: docs
weight: 50
url: /ja/net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop,format,style,number formats,number format,NumberFormat
description: この記事では、GridDesktopのワークシートのセルに対してスタイル形式を取得または設定する方法について紹介しています。
---

{{% alert color="primary" %}} 

このトピックでは、セルにスタイル形式を適用することに焦点を当て、セルに適用できるほぼすべての関連するプロパティについて説明します。基本的な書式設定に加えて、境界線の描画やセルの数値形式の設定についても詳しく説明します。

{{% /alert %}} 
## **セルにカスタムスタイルを適用する - 例**
Aspose.Cells.GridDesktopを使用してセルのフォントと色を変更するには、以下の手順に従ってください:

- 任意の **Worksheet** にアクセスします
- 適用する **Style** のある **Cell** にアクセス
- **Cell** の **Style** を取得
- カスタムの必要に応じて **スタイル** プロパティを設定
- 最後に、更新された **Style** を **Cell** に設定

開発者が要件に応じてスタイルをカスタマイズするために使用できる **Style** オブジェクトには、多くの有用なプロパティやメソッドが提供されています。以下のコードでは、セルにカスタムスタイルを適用する方法を示しています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **セルの境界線の描画**
 **Style** オブジェクトを使用すると、セルの境界線を非常に簡単に描くことができます。境界線の色を自由に選択することができます。また、開発者は、セルの周囲に描画する特定のタイプの線を選択する柔軟性も持っています。開発者は、**Style** オブジェクトの **SetBorderLine** および **SetBorderColor** メソッドを使用して、任意のタイプと色の境界線を描画することができます。同様に、任意のセルの境界情報を取得するには、**Style** オブジェクトの **GetBorderLine** および **GetBorderColor** メソッドを使用することもできます。
### **境界線の種類**
Aspose.Cells.GridDesktop でサポートされている境界線の種類は次の通りです:

- **左** : 左の境界線を表します
- **右** : 右の境界線を表します
- **上** : 上の境界線を表します
- **下** : 下の境界線を表します
- **DiagonalDown** : 対角線向けの境界線を表します
- **DiagonalUp** : 対角線向けの境界線を表します
### **境界線の種類**
境界線は線で構成されます。線の種類を変更すると、境界線の外観が変わります。Aspose.Cells.GridDesktop でサポートされている多くの種類の境界線が以下にリストされています:

- **None** : 境界線がないことを示します
- **薄い** 、実線の境界を表します
- **中** 、実線の線幅が2fに等しい境界を表します
- **点線** 、点線の境界を表します
- **点線** 、点線の境界を表します
- **太い** 、実線の線幅が3fに等しい境界を表します
- **中太** 、線幅が2fに等しい点線の境界を表します
- **薄い点線点** 、破線点線の境界を表します
- **中点線点** 、線幅が2fに等しい破線点線の境界を表します
- **薄い点線破線点** 、点線破線の境界を表します
- **中点線破線点** 、線幅が2fに等しい点線破線の境界を表します
## **全体をまとめる - 例**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **数値形式の設定**
Aspose.Cells.GridDesktopは、さまざまな数値書式の設定も提供しています。Aspose.Cells.GridDesktopで提供される58種類の組み込み数値書式があります。すべてのサポートされている数値書式の完全なリストを表示するには、[サポートされている数値書式のリスト](/cells/ja/net/list-of-supported-number-formats/)を参照してください。

すべての組み込み数値書式には**インデックス**番号が割り当てられています。**たとえば**、**0.00E+00**数値書式の**インデックス**番号は**11**です。任意のセルで組み込みの数値書式を使用するには、開発者は**Style**オブジェクトのNumberFormatプロパティをその特定の数値書式の**インデックス**番号に設定することができます。ただし、開発者が独自のカスタム数値書式が必要な場合は、**Style**オブジェクトのCustomプロパティも使用できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
