---
title: مراقبة البرامج الجارية
type: docs
weight: 20
url: /ar/python-java/monitor-running-programs/
---

## **كيفية مراقبة برنامج جاري**

يُظهر الكود العينة التالي كيفية مراقبة برنامج تشغيل. يمكن استخدام هذا الكود لمراقبة تشغيل رموز ذات صلة بـ [الدفتر](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). ما عليك سوى استخدام فئة [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) لإنشاء كائن مراقبة، استخدام الوظيفة [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) لإضافتها إلى معلمات تشغيل [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)، ثم استخدام الوظيفة [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) لتعيين وقت الانقطاع المتوقع (بالميللي ثانية). إذا تجاوز وقت التشغيل للرمز المراقب المدة المتوقعة، سيتم توقيف البرنامج وسيتم رمي استثناء.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
