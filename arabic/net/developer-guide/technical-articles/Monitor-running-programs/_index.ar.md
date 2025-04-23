---
title: مراقبة البرامج الجارية
type: docs
weight: 20
url: /ar/net/Monitor-running-programs/
---

## **كيفية مراقبة برنامج جاري**

يلقي الشيفرة المثالية التالية الضوء على كيفية مراقبة برنامج جاري. يمكن استخدام هذه الشيفرة لمراقبة تشغيل الشيفرات المتعلقة بـ [الدفتر](https://reference.aspose.com/cells/net/aspose.cells/workbook/) . ببساطة استخدام فئة [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) لإنشاء كائن مراقبة، استخدام الدالة [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) لإضافته إلى معايير التشغيل لـ [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/)، ثم استخدام الدالة [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) لتعيين الوقت المتوقع للانقطاع (بالميللي ثانية). إذا تجاوز وقت التشغيل للشيفرة المراقبة الوقت المتوقع، سيتم انقطاع البرنامج وإثارة استثناء.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
{{< app/cells/assistant language="csharp" >}}
