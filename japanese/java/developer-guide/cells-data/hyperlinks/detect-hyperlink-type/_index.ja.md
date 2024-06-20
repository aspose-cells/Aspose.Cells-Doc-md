---
title: ハイパーリンクタイプの検出
type: docs
weight: 180
url: /ja/java/detect-hyperlink-type/
---

## **ハイパーリンクタイプの検出**

Excelファイルには、外部、セル参照、ファイルパスなどの異なるタイプのハイパーリンクが存在します。Aspose.Cellsはハイパーリンクのタイプを検出する機能をサポートしています。ハイパーリンクのタイプは[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)列挙型によって表されます。[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)列挙型には、次のメンバーがあります。

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): 外部リンク
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): ローカルファイルまたはフォルダへの完全なパス
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): メール
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): セルまたは名前付き範囲へのリンク

ハイパーリンクのタイプをチェックするには、[**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)クラスが[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)プロパティを提供し、戻り値が[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)であることを確認します。次のコードスニペットは、この[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)プロパティの使用をデモンストレーションします。

## ソースコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

上記のコードスニペットによって生成された出力は以下の通りです。

## コンソール出力
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
