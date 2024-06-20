---
title: テーブルソート構成
type: docs
weight: 90
url: /ja/reportingservices/table-sorting-configuration/
---

構成には5種類のプロパティが含まれます。これにはレポート名、テーブル名、行オフセット値、列インデックス、および順序タイプが含まれます。

- **name** はレポート名およびテーブル名を表します。nameが空白の場合、nameはレポート全体を表します。
- **value** は行オフセットを表します。
- **Index** はテーブル内の列位置を表します。
- **Order** はソート順序タイプを表します。

テーブルソート構成の例:

*<TableSorted>
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
