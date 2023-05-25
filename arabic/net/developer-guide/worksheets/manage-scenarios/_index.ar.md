---
title: إنشاء أو معالجة أو إزالة السيناريوهات من أوراق العمل
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: في هذه المقالة ، ستتعلم كيفية إنشاء السيناريوهات أو معالجتها أو إزالتها من أوراق عمل Excel برمجيًا باستخدام C# Library مع .NET API.
keywords: create scenario worksheet c#, remove scenario excel worksheet c#, manipulate scenario worksheet c#
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى إنشاء سيناريوهات أو معالجتها أو حذفها في جداول البيانات. السيناريو يسمى "ماذا لو؟" نموذج يتضمن خلايا إدخال متغيرة مرتبطة بصيغة واحدة أو أكثر. قبل إنشاء سيناريو ، صمم ورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يوضح المثال التالي كيفية إنشاء سيناريوهات وإزالتها من ورقة عمل في مصنف عبر Aspose.Cells APIs.

{{% /alert %}}

يوفر Aspose.Cells بعض الفئات المفيدة ، على سبيل المثال ،[**مجموعة سيناريو**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**سيناريو**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**السيناريو InputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) ، و[**سيناريو InputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) الطبقات. كما يوفر[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)ملكية. يفتح نموذج التعليمة البرمجية أدناه ملف XLSX Excel يحتوي على بعض السيناريوهات ويزيل سيناريو موجود. كما يضيف سيناريو جديدًا إلى ورقة العمل قبل حفظ ملف Excel. يستخدم المثال ملف قالب بسيط للغاية يحتوي على سيناريو.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
