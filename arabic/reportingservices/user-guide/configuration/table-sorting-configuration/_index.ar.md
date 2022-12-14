---
title: تكوين فرز الجدول
type: docs
weight: 90
url: /ar/reportingservices/table-sorting-configuration/
---
يتضمن التكوين 5 أنواع من الخصائص. وهي تشمل اسم التقرير واسم الجدول وقيمة إزاحة الصف وفهرس العمود ونوع الأمر.

- **اسم** يمثل اسم التقرير واسم الجدول. يمثل الاسم التقرير بأكمله عندما يكون الاسم فارغًا.
- **القيمة** يمثل إزاحة الصف.
- **فِهرِس** يمثل موضع العمود في الجدول.
- **ترتيب** يمثل نوع ترتيب الفرز.

مثال تكوين TableSorted:

* <TableSorted>
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
