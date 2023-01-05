---
title: ハイパーリンク タイプの検出
type: docs
weight: 180
url: /ja/java/detect-hyperlink-type/
---
## **ハイパーリンク タイプの検出**

Excel ファイルには、外部、セル参照、ファイル パスなど、さまざまな種類のハイパーリンクを含めることができます。Aspose.Cells は、ハイパーリンクの種類を検出する機能をサポートしています。ハイパーリンクの種類は、[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)列挙。の[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Enumeration には次のメンバーがあります。

- [**外部の**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL)： 外部リンク
- [**ファイルパス**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH)ファイル\フォルダーへのローカルおよびフル パス。
- [**Eメール**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL)： Eメール
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): セルまたは名前付き範囲へのリンク。

ハイパーリンクの種類を確認するには、[**ハイパーリンク**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)クラスは[**リンクタイプ**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)戻り値の型を持つプロパティ[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType).次のコード スニペットは、[**リンクタイプ**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)これを利用したプロパティ[ソースエクセルファイル](LinkTypes.xlsx).

## ソースコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

以下は、上記のコード スニペットによって生成された出力です。

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
