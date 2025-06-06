---
title: تعطيل شريط جدول الدوران
type: docs
weight: 90
url: /ar/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

تعتبر التقارير القائمة على جداول الدوران مفيدة ولكنها عرضة للخطأ إذا لم يكن لدى المستخدمين المستهدفين معرفة تفصيلية ببرنامج Excel لتكوين هذه التقارير. في هذه الظروف، سترغب المؤسسات في تقييد المستخدمين من القدرة على تغيير تقرير مبني على جدول الدوران. عادةً ما لا تكون الميزات الشائعة لجدول الدوران مثل إضافة عوامل تصفية إضافية، أو مفاتيح الفرز، أو تغيير ترتيب بعض الأشياء في التقرير موصى بها لكل مستخدم. من ناحية أخرى، يجب أن يكون بإمكان هؤلاء المستخدمين أيضاً تحديث التقرير واستخدام الفلاتر أو المفاتيح الحالية. قدمت Aspose.Cells هذه القدرة للمطورين لتقييد المستخدمين من تغيير هذه التقارير أثناء إنشاء هذه التقارير. لهذا الغرض، يوفر Excel ميزة لتعطيل شريط جدول الدوران ويتم توفير نفس الأمر من قبل Aspose.Cells أي يمكن للمطور تعطيل الشريط الذي يحتوي على عناصر التحكم لتعديل هذه التقارير.

{{% /alert %}}

## **تعطيل شريط الأدوات لجداول الدوران باستخدام PivotTable.EnableWizard**

يوضح الكود التالي هذه الميزة عن طريق الوصول إلى جدول دوران من ورقة ومن ثم ضبط [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) إلى **false**. يمكن تنزيل ملف جدول الدوران المثالي من هذا [الرابط](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
{{< app/cells/assistant language="csharp" >}}
