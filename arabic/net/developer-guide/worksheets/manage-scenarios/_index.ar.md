---
title: إنشاء، تلاعب أو إزالة السيناريوهات من الأوراق العمل
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: في هذا المقال، ستتعلم كيفية إنشاء، التلاعب أو إزالة السيناريوهات من أوراق العمل في إكسل برمجياً باستخدام مكتبة C# مع واجهة برمجة التطبيقات .NET.
keywords: إنشاء سيناريو الورقة العمل سي#، إزالة سيناريو إكسل لورقة العمل سي#، التلاعب بسيناريو الورقة العمل سي#
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى إنشاء، التلاعب أو حذف السيناريوهات في جداول البيانات. السيناريو هو نموذج 'ماذا لو؟' يتضمن خلايا إدخال متغيرة مرتبطة بواحد أو أكثر من الصيغ. قبل إنشاء سيناريو، صمم الورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يظهر المثال التالي كيفية إنشاء وإزالة السيناريوهات من ورقة عمل في مصنف باستخدام واجهات Aspose.Cells.

{{% /alert %}}

توفر Aspose.Cells بعض الفصول المفيدة، على سبيل المثال، [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection)، [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario)، [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)، و [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell). كما توفر الخاصية [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). يفتح الكود المصدري العينة أدناه ملف إكسل XLSX الذي يحتوي على بعض السيناريوهات ويزيل السيناريو الحالي. كما يضيف سيناريوًا جديدًا إلى الورقة العمل قبل حفظ ملف إكسل. يستخدم المثال ملف قالب بسيط جدًا يحتوي على سيناريو.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
