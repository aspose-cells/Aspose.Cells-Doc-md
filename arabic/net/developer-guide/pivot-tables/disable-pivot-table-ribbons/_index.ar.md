﻿---
title: تعطيل شرائط الجدول المحوري
type: docs
weight: 90
url: /ar/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

تعد التقارير المستندة إلى الجدول المحوري مفيدة ولكنها عرضة للخطأ إذا لم يكن لدى المستخدمين المستهدفين معرفة تفصيلية ببرنامج Excel لتكوين هذه التقارير. في هذه الظروف ، سترغب المؤسسات في تقييد المستخدمين من القدرة على تغيير التقرير المستند إلى الجدول المحوري. لا يُنصح في الغالب لكل مستخدم بميزات الجدول المحوري الشائعة مثل إضافة عوامل تصفية إضافية أو مقسمات طرق عرض أو حقول أو تغيير ترتيب أشياء معينة في التقرير. من ناحية أخرى ، يجب أن يكون هؤلاء المستخدمون قادرين أيضًا على تحديث التقرير واستخدام عوامل التصفية أو مقسمات طرق العرض الموجودة. قدم Aspose.Cells هذه القدرة للمطورين لتقييد المستخدمين من تغيير هذه التقارير أثناء إنشاء هذه التقارير. لهذا الغرض ، يوفر Excel ميزة لتعطيل شريط الجدول المحوري ويتم توفير نفس الشيء بواسطة Aspose.Cells ، أي يمكن للمطور تعطيل الشريط الذي يحتوي على عناصر تحكم لتعديل هذه التقارير.

{{% /alert %}}

## **تعطيل Pivot Table Ribbon باستخدام PivotTable.EnableWizard**

يوضح الكود التالي هذه الميزة من خلال الوصول إلى جدول محوري من ورقة ثم الإعداد[**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) إلى**خاطئة** . يمكن تنزيل نموذج ملف جدول محوري من هذا[حلقة الوصل](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
