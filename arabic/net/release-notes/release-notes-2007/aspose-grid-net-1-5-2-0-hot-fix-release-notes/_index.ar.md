---
title: Aspose.Grid صافي 1.5.2.0 ملاحظات إصدار الإصلاح السريع
type: docs
weight: 50
url: /ar/net/aspose-grid-net-1-5-2-0-hot-fix-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Grid صافي 1.5.2.0 الإصلاح السريع](https://downloads.aspose.com/cells/net/new-releases/aspose.grid-.net-1.5.2.0-hot-fix/)

{{% /alert %}} 

 لقد أصدرنا Aspose.Grid 1.5.2!

 ملاحظات الإصدار

 Aspose.Grid.ويب

- ثابت: خطأ لون ضبط جانب العميل
- ثابت: لا تأخذ خاصية TableStyle / TableItemStyle CssClass تأثير الخطأ
- دعم إنشاء تقارير الجدول المحوري
- دعم متعدد الخلايا من جانب العميل تحديد / نسخ / قص / لصق / ضبط النمط
- دعم عمليات قائمة النقر بزر الماوس الأيمن من جانب العميل: تجميد / إلغاء التجميد ؛ إدراج / حذف صف / عمود ؛ دمج / إلغاء دمج الخلايا ؛
- دعم الارتباطات التشعبية (عرض نص أو صورة أو UrlLink أو إجراء CellCommand)
- الخصائص المضافة: ActiveCell ، EnableClientColumnOperations ، EnableClientFreeze ، EnableClientMergeOperations ، EnableClientRowOperations ، SelectCells
- الطرق المضافة: WebCells.GetColumnReadonly ، WebCells.SetColumnReadonly ، WebCells.GetRowReadonly ، WebCells.SetRowReadonly
- الأحداث المضافة: SheetDataUpdated ، LoadCustomData (لاستعادة بيانات الوضع بدون جلسة) ، CellCommand ، ColumnDeleted ، ColumnInserted ، RowDeleted ، RowInserted ، PageIndexChanged
- تم التغيير: الآن ليس هناك حاجة إلى مسار الويب لملف العميل (/ agw_client) وملفات العميل (htc ، gif ، إلخ) في بيئة النشر. هذه الملفات مضمنة الآن في عنصر التحكم. هذا يبسط عمليات النشر والترقية.

 سطح المكتب ` `Aspose.Grid

  المحسن:

- نص رأس العمود معتمد.
- قائمة السياق المدعومة.
- دعم الارتباطات التشعبية والتعليقات والصور المصدرة.
- Cell زر ، مربع الاختيار ، combox مدعوم.
- دعم أحداث CellClick و CellDoubleClick و CellKeyPressed.
- يتم دعم تطبيق النمط على نطاق من الخلايا.
- دعم التحقق من صحة البيانات.

 مُثَبَّت:

- تصغير النموذج الذي يحتوي على عنصر تحكم GridDesktop الذي عيّن تعبئة خاصية Dock ، يتم طرح استثناء.
- الضغط على مفتاح "حذف" ، لا يقوم عنصر التحكم GridDesktop برفع حدث CellDataChanged.
- عندما يكون رقم الصف أكبر من 4 أرقام رقمية ، فإن عرض رأس الصف لا يكفي.
- عند التحميل من ملف Excel ، يختلف خط الحرف الذي يتم إدخاله في الخلية عن خط الخلية.
- لا يمكن إدخال إدخال في خلية ، استخدم الآن مفاتيح Control + Enter.
- إذا لم تكن هناك خلايا مركزة ، فسيتم وضع عنصر التحكم في مربع النص في موضع الخطأ عند إدخال حرف.
- يوجد تعليق في خلية ، ثم يتم التركيز على الخلية اليمنى ؛ عند الإشارة إلى الخلية التي تحتوي على تعليق ، ستضيء الخلية المركزة دائمًا.
- لا يعمل إخفاء عمود الصف.
