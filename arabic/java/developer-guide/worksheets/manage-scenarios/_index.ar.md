---
title: إنشاء أو معالجة أو إزالة السيناريوهات من أوراق العمل
linktitle: إدارة السيناريوهات
type: docs
weight: 120
url: /ar/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى إنشاء سيناريوهات أو معالجتها أو حذفها في جداول البيانات. السيناريو عبارة عن نموذج مسمى ماذا لو يتضمن خلايا إدخال متغيرة مرتبطة ببعضها البعض بواسطة صيغة واحدة أو أكثر. قبل إنشاء سيناريو ، صمم ورقة عمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يوضح المثال التالي كيفية إنشاء السيناريوهات وإزالتها من ورقة العمل باستخدام واجهات برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

 يوفر Aspose.Cells بعض الفئات المفيدة ، على سبيل المثال[**مجموعة سيناريو**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**سيناريو**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**السيناريو InputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) و[**سيناريو InputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . كما يوفر[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)خاصية. يفتح نموذج التعليمات البرمجية أدناه ملف XLSX Excel (الذي يحتوي على بعض السيناريوهات) ويزيل سيناريو موجود من ورقة العمل. كما يضيف سيناريو جديدًا قبل حفظ ملف Excel. يستخدم ملف قالب بسيط للغاية يحتوي على سيناريو.

بعد تنفيذ التعليمات البرمجية ، تتم إزالة سيناريو موجود وإضافة سيناريو جديد إلى ورقة العمل.

**ملف الإخراج**

![ما يجب القيام به: image_بديل_نص](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
