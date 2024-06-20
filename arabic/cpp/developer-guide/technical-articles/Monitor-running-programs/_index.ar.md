---
title: مراقبة البرامج الجارية
type: docs
weight: 20
url: /ar/cpp/Monitor-running-programs/
---

## **كيفية مراقبة برنامج جاري**

يعرض الكود العينة التالي كيفية رصد برنامج تشغيل. يمكن استخدام هذا الكود لمراقبة تنفيذ [الفصول الدراسية](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) المتعلق بالبرنامج. ببساطة، استخدم فئة [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) لإنشاء كائن مراقبة، استخدم وظيفة [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) لإضافتها إلى [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) معلمات التشغيل، ثم استخدم وظيفة [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) لتعيين الوقت المتوقع للانقطاع (بالميلي ثانية) . إذا تجاوز وقت تشغيل الكود المراقب الوقت المتوقع، سيتم إيقاف التشغيل وسيتم رمي استثناء.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
