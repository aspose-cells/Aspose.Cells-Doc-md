---
title: مراقبة البرامج الجارية
type: docs
weight: 20
url: /ar/python-net/monitor-running-programs/
---

## **كيفية مراقبة برنامج جاري**

الكود النموذجي التالي يوضح كيفية مراقبة تشغيل برنامج. يمكن استخدام هذا الكود لمراقبة تشغيل الكود المرتبط بـ [الدفتر](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) المرتبط. يكفي استخدام فصل [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) لإنشاء كائن مراقبة، استخدام دالة [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) لإضافتها إلى معلمات التشغيل الخاصة بـ [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) ومن ثم استخدام الدالة [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) لتعيين الزمن المتوقع للانقطاع (بالمللي ثانية). إذا تجاوز وقت التشغيل للكود المراقب الوقت المتوقع، سيتم انقطاع البرنامج وستتم طرح استثناء.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
