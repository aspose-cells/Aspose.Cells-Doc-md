---
title: إنشاء، تلاعب أو إزالة السيناريوهات من الأوراق العمل
linktitle: إدارة السيناريوهات
type: docs
weight: 120
url: /ar/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى إنشاء أو تلاعب أو حذف سيناريوهات في جداول البيانات. السناريو هو نموذج وهمي مسمى يتضمن خلايا متغيرة متصلة ببعضها بواسطة إحدى الصيغ أو أكثر. قبل إنشاء سيناريو، قم بتصميم ورقة عمل بحيث تحتوي على على الأقل صيغة واحدة تعتمد على الخلايا التي يمكن إدخال قيم مختلفة إليها. يُوضح المثال التالي كيفية إنشاء وإزالة السيناريو من ورقة عمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

تقدم Aspose.Cells بعض الفئات المفيدة، على سبيل المثال [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection)، [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario)، [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) و[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). كما توفر خاصية [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). يفتح الكود العيني أدناه ملف Excel XLSX (الذي يحتوي على بعض السيناريوهات) ويزيل سيناريو موجود من الورقة. كما يضيف سيناريو جديد قبل حفظ ملف Excel. يستخدم ملف قالب بسيط يحتوي على سيناريو.

بعد تنفيذ الكود، يتم إزالة سيناريو موجود ويتم إضافة سيناريو جديد إلى ورقة العمل.

ملف الإخراج

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
