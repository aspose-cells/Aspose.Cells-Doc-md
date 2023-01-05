---
title: Tablo Sıralama Yapılandırması
type: docs
weight: 90
url: /tr/reportingservices/table-sorting-configuration/
---
Yapılandırma 5 tür özellik içerir. Bunlar arasında rapor adı, tablo adı, satır ofset değeri, sütun dizini ve sipariş türü bulunur.

- **isim** rapor adını ve tablo adını temsil eder. ad boş bırakıldığında raporun tamamını temsil eder.
- **değer** satır ofsetini temsil eder.
- **dizin** tablodaki sütun konumunu temsil eder.
- **Emir** sıralama düzeni türünü temsil eder.

TableSorted Yapılandırma Örneği:

*<TabloSıralı>
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
