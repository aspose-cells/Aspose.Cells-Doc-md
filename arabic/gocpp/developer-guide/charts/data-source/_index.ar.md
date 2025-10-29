---
title: ضبط مصدر البيانات للمخطط مع Golang عبر C++
linktitle: مصدر البيانات
type: docs
weight: 10
url: /ar/go-cpp/data-formatting-in-charts/
description: تعرف على مصادر البيانات المدعومة بواسطة Aspose.Cells for C++. سيرشدك دليلنا خلال الأنواع المختلفة من مصادر البيانات المتاحة ويعرض لك كيفية الاتصال بها واسترجاع البيانات منها لملء أوراق العمل الخاصة بك.
keywords: Aspose.Cells for C++، رسم المخططات، تنسيق البيانات، التسميات، الألوان، الخطوط، المظهر، قابلية الاستخدام.
---

في موضوعاتنا السابقة، قدمنا العديد من الأمثلة لشرح كيف يمكنك ضبط مصدر البيانات لمخططك. في هذا الموضوع، سنوفر مزيدًا من التفاصيل حول أنواع البيانات التي يمكن تعيينها لمخطط.

## **ضبط بيانات الرسم البياني**

هناك نوعان من البيانات التي يتعين التعامل معها أثناء العمل على الرسوم البيانية باستخدام Aspose.Cells وهي كما يلي:

- بيانات الرسم البياني.
- بيانات الفئة.

### **بيانات الرسم البياني**

بيانات الرسم البياني هي البيانات التي نستخدمها كمصدر لبناء الرسوم البيانية الخاصة بنا. يمكننا إضافة مجموعة من الخلايا (تحتوي على بيانات الرسم البياني) عن طريق استدعاء [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) إلى [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **بيانات الفئة**

تُستخدم بيانات الفئة لوسم بيانات الرسم البياني ويمكن إضافتها إلى [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) باستخدام خاصية [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/). يتم تقديم مثال كامل أدناه لتوضيح استخدام بيانات الرسم البياني والفئة. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل كما هو موضح أدناه.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **الموضوعات المتقدمة**
- [تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق](/cells/ar/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [إنشاء رسوم بيانية ديناميكية](/cells/ar/cpp/create-dynamic-charts/)
- [طريقة سهلة لضبط الرسوم البيانية باستخدام طريقة Chart.SetChartDataRange](/cells/ar/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [البحث عن نوع قيم X وY لنقاط في سلسلة الرسم البياني](/cells/ar/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
