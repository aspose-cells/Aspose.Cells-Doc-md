---
title: テーブルの並べ替え構成
type: docs
weight: 90
url: /ja/reportingservices/table-sorting-configuration/
---
構成には、5 種類のプロパティが含まれます。これらには、レポート名、テーブル名、行オフセット値、列インデックス、および順序タイプが含まれます。

- **名前**レポート名とテーブル名を表します。 name が空白の場合、name はレポート全体を表します。
- **価値**行オフセットを表します。
- **索引**テーブル内の列の位置を表します。
- **注文**ソート順のタイプを表します。

TableSorted 構成例:

*<並べ替えられたテーブル>
<Report name=”report name” >
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
<Table name="table name">
<RowOffset value="1"/>
<Column Index="1" Order="Descending" />
<Column Index="2" Order="Ascending" />
……
</Table>
</Report>
</TableSorted>*
