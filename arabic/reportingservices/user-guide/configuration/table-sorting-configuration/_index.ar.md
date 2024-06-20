---
title: تكوين فرز الجدول
type: docs
weight: 90
url: /ar/reportingservices/table-sorting-configuration/
---

التكوين يشمل 5 أنواع من الخصائص. تشمل هذه الاسماء اسم التقرير واسم الجدول وقيمة الإزاحة الصف ومؤشر العمود ونوع الامر.

- **الاسم** يمثل اسم التقرير واسم الجدول. يمثل الاسم التقرير بأكمله عندما يكون الاسم فارغًا.
- **القيمة** تمثل إزاحة الصف.
- **المؤشر** يمثل موضع العمود في الجدول.
- **الامر** يمثل نوع ترتيب الفرز.

مثال على تكوين الجدول المرتب

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
