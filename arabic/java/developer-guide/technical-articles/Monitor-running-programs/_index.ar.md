---
title: مراقبة البرامج الجارية
type: docs
weight: 20
url: /ar/java/Monitor-running-programs/
---

## **كيفية مراقبة برنامج جاري**

يوضح الكود العيني التالي كيفية مراقبة تشغيل برنامج. يمكن استخدام هذا الكود لمراقبة تشغيل الكود المتعلق بـ [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/). ببساطة قم باستخدام فئة [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) لإنشاء كائن مراقب، استخدم الدالة [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) لإضافته إلى المعلمات الجاري تشغيلها لـ [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/)، ثم استخدم الدالة [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) لتعيين الوقت المتوقع للانقطاع (بالميلي ثانية). إذا تجاوز وقت تشغيل الكود المراقب الوقت المتوقع، سيتم انقطاع البرنامج وسيتم رمي استثناء.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
