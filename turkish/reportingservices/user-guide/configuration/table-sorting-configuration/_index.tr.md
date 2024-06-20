---
title: Tablo Sıralama Yapılandırması
type: docs
weight: 90
url: /tr/reportingservices/table-sorting-configuration/
---

Yapılandırma 5 çeşit özelliği içerir. Bunlar rapor adı, tablo adı, satır ofset değeri, sütun dizini ve sıra tipidir.

- **ad**, rapor adını ve tablo adını temsil eder. ad boş olduğunda tüm raporu temsil eder.
- **değer**, satır ofsetini temsil eder.
- **İndeks**, tablodaki sütun konumunu temsil eder.
- **Sıra**, sıralama düzeni türünü temsil eder.

TableSorted Yapılandırma Örneği:

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
