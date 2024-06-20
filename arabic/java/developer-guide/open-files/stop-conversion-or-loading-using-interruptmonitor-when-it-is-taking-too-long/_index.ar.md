---
title: توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً
type: docs
weight: 100
url: /ar/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **سيناريوهات الاستخدام المحتملة**

يُسمح لـ Aspose.Cells بإيقاف تحويل الدفتر إلى تنسيقات مختلفة مثل PDF، HTML، إلخ باستخدام الكائن [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) عندما يستغرق وقتًا طويلاً. عملية التحويل غالبًا ما تكون مكثفة جدًا من حيث استخدام وحدة المعالجة المركزية والذاكرة، ومن المفيد في كثير من الأحيان إيقافها عندما تكون الموارد محدودة. يمكنك استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) للتوقف عن التحويل وكذلك لإيقاف تحميل دفتر العمل الضخم. يرجى استخدام خاصية [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) للتوقف عن التحويل والخاصية [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) لتحميل دفتر العمل الضخم.

## **توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح الكود عينة التالي استخدام الكائن [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor). يقوم الكود بتحويل ملف إكسل كبير إلى ملف PDF. سيستغرق عدة ثوانٍ (أكثر من 30 ثانية) لتحويله بسبب هذه السطور من الكود.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

كما ترون، الخلية **AB1000000** بعيدة إلى حد ما في ملف XLSX. ومع ذلك، يقوم طريقة *WaitForWhileAndThenInterrupt()* بتقطيع عملية التحويل بعد 10 ثوانٍ وينتهي/يُنهي البرنامج. يرجى استخدام الكود التالي لتنفيذ الكود عينة.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
