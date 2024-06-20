---
title: テーブルまたはリストオブジェクトのコメントを設定する
type: docs
weight: 60
url: /ja/python-java/set-the-comment-of-table-or-list-object/
---

## **ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください**
Aspose.Cells for Python via Javaでは、リストオブジェクトのコメントを追加することができます。このために、APIは[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)プロパティを提供しています。[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)プロパティによって追加されたコメントは、*xl/tables/tableName.xml*ファイル内で表示されます。

以下のスクリーンショットは、サンプルコードによって作成されたコメントを赤い四角で示しています。

![todo:image_alt_text](setting-list-object-comment.png)

以下のサンプルコードは、[ソースExcelファイル](source.xlsx)をロードし、ワークシート内の最初のテーブルまたはリストオブジェクトのコメントを設定しています。 

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
